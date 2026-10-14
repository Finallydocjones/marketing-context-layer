#!/usr/bin/env python3
"""Validate a marketing context layer repo.

Errors (fail the check):
  - content doc missing its header block or a required field
  - invalid intent, status, or date format
  - client-approved doc without approved_by / approved_date
  - markdown file in an unknown top-level folder (e.g. "faqs/" instead of "faq/")
  - two docs with the same title (catches a file pasted over another)
  - required core files missing (skipped in the blank template repo)

Warnings (don't fail):
  - docs still in draft
  - review_by date has passed

Usage: python3 scripts/validate_frontmatter.py
"""
import datetime, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Folders whose .md files must carry a governance header.
CONTENT_FOLDERS = ["brand-facts", "product-specs", "policy", "faq", "briefs",
                   "compliance", "resources"]
# Folders allowed to hold .md files without headers.
OTHER_FOLDERS = {"templates", "scripts", ".github"}
# Core files every client repo needs (not checked in the blank template).
REQUIRED_FILES = ["README.md", "GOVERNANCE.md", "CHANGELOG.md", "OPEN-QUESTIONS.md",
                  "CODEOWNERS", "policy/claims-and-restrictions.md",
                  "brand-facts/company-facts.md"]
IS_TEMPLATE = (ROOT / "TEMPLATE_REPO").exists()

REQUIRED = ["title", "intent", "audience", "source", "effective_date",
            "related_documents", "owner", "status", "review_by"]
INTENTS = {"brand-facts", "product-spec", "faq", "policy", "brief"}
STATUSES = {"draft", "client-approved", "superseded"}
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def header(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


errors, warnings = [], []
today = datetime.date.today()
titles = {}

# 1. Unknown folders
for f in ROOT.rglob("*.md"):
    rel = f.relative_to(ROOT)
    if ".git" in rel.parts[:1] or len(rel.parts) == 1:
        continue
    top = rel.parts[0]
    if top not in CONTENT_FOLDERS and top not in OTHER_FOLDERS:
        errors.append(f"{rel}: unknown folder '{top}/' (expected one of: {', '.join(CONTENT_FOLDERS)})")

# 2. Required core files
if not IS_TEMPLATE:
    for req in REQUIRED_FILES:
        if not (ROOT / req).exists():
            errors.append(f"missing required file: {req}")

# 3. Content doc headers
for folder in CONTENT_FOLDERS:
    d = ROOT / folder
    if not d.exists():
        continue
    for f in sorted(d.rglob("*.md")):
        if f.name == "README.md":
            continue
        rel = f.relative_to(ROOT)
        h = header(f.read_text())
        if h is None:
            errors.append(f"{rel}: missing header block"); continue
        for k in REQUIRED:
            if not h.get(k):
                errors.append(f"{rel}: missing '{k}'")
        if h.get("intent") and h["intent"] not in INTENTS:
            errors.append(f"{rel}: bad intent '{h['intent']}'")
        if h.get("status") and h["status"] not in STATUSES:
            errors.append(f"{rel}: bad status '{h['status']}'")
        for k in ("effective_date", "review_by"):
            if h.get(k) and not DATE.match(h[k]):
                errors.append(f"{rel}: '{k}' must be YYYY-MM-DD")
        if h.get("status") == "client-approved" and not (h.get("approved_by") and h.get("approved_date")):
            errors.append(f"{rel}: client-approved but approved_by/approved_date empty")
        if h.get("title"):
            if h["title"] in titles:
                errors.append(f"{rel}: duplicate title (same as {titles[h['title']]}); was a file pasted over another?")
            else:
                titles[h["title"]] = rel
        if h.get("status") == "draft":
            warnings.append(f"{rel}: still draft (do not sync to Profound)")
        if h.get("review_by") and DATE.match(h["review_by"]):
            if datetime.date.fromisoformat(h["review_by"]) < today:
                warnings.append(f"{rel}: review_by {h['review_by']} has passed")

for w in warnings: print("WARN ", w)
for e in errors: print("ERROR", e)
print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)" + ("  [template repo]" if IS_TEMPLATE else ""))
sys.exit(1 if errors else 0)
