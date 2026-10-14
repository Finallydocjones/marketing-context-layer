# AlumiPlate Core Context

The governed source of truth for what Rocket55 and our AI tools say about **AlumiPlate** (pure aluminum electroplating, Coon Rapids, MN).

Everything in this repo is meant to be read by people *and* machines: Claude projects, Profound (FactCheck + agents), schema and page-copy work, and any other AI tool the team uses. If it's not in `main`, it isn't approved.

## Folder map

| Folder | What goes here | Main consumer |
|---|---|---|
| `brand-facts/` | Canonical, dated, sourced facts about the company and its approvals | Profound FactCheck, schema, all AI tools |
| `product-specs/` | One file per offering: what it is, who it's for, limits, comparisons | Page copy, agents, answer-engine content |
| `policy/` | Approved language, restricted claims, markets to de-emphasize | Every writer and every agent — read first |
| `faq/` | Real buyer questions with one approved answer each | FAQ pages, FAQ schema, FactCheck |
| `briefs/` | Current priorities: audience, markets, quarter goals | Planning, agents, content briefs |
| `templates/` | Blank templates for each document type | Copy when adding a new doc |
| `OPEN-QUESTIONS.md` | Facts that conflict or need client confirmation | Account lead — resolve before approval |

## Start here

1. Read `policy/claims-and-restrictions.md` before writing anything about AlumiPlate.
2. Read `GOVERNANCE.md` for how changes get approved.
3. Check `OPEN-QUESTIONS.md` — don't publish anything that depends on an open item.

## Status

All documents are currently **`status: draft`** (seeded 2026-10-13 from the website, Drive, and Fathom calls). They become `client-approved` only after AlumiPlate (Gus / Bill) confirms them. Drafts must not be loaded into Profound or published to the website.

## Owner

Jen Jones, Director of SXO, Rocket55 (account SXO lead).

## Setting up on GitHub (one time)

1. Create a **private** repo named `alumiplate-core-context`, ideally under a Rocket55 GitHub organization. Don't add a README.
2. Upload these files (GitHub web: **Add file → Upload files**, drag in the unzipped folder contents), or push from the command line:
   ```
   git remote add origin https://github.com/<org>/alumiplate-core-context.git
   git push -u origin main
   ```
3. In `CODEOWNERS`, replace the placeholder with your GitHub username.
4. **Settings → Branches → Add rule** for `main`: require a pull request, require approval, require review from Code Owners, and require the "Validate core context" check to pass.
5. Limit repo access to people working on AlumiPlate.
6. Optional: in Claude.ai, create an AlumiPlate project and add this repo as project knowledge.

## Validation

`python3 scripts/validate_frontmatter.py` checks every document's header. It runs automatically on every pull request.
