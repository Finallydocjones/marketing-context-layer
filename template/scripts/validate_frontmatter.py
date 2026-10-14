#!/usr/bin/env python3
"""Check every content doc has a complete governance header.

Fails on missing fields or invalid values; warns on drafts and past review dates.
Usage: python3 scripts/validate_frontmatter.py
"""
import datetime, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FOLDERS = ["brand-facts", "product-specs", "policy", "faq", "briefs"]
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
for folder in FOLDERS:
    for f in sorted((ROOT / folder).glob("*.md")):
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
        if h.get("status") == "draft":
            warnings.append(f"{rel}: still draft — do not sync to Profound")
        if h.get("review_by") and DATE.match(h["review_by"]):
            if datetime.date.fromisoformat(h["review_by"]) < today:
                warnings.append(f"{rel}: review_by {h['review_by']} has passed")

for w in warnings: print("WARN ", w)
for e in errors: print("ERROR", e)
print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)")
sys.exit(1 if errors else 0)
