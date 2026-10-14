# Governance

How content in this repo is created, approved, published, and retired.

> Copy this file to `GOVERNANCE.md`, fill in the bracketed parts, and delete this `.template` file.

## Roles

| Role | Who | Responsibility |
|---|---|---|
| Repo owner | [Rocket55 owner] | Reviews every pull request, merges to `main`, owns sync to Profound |
| Account manager | [Rocket55 AM] | Flags client decisions from meetings that need to land here |
| Client approver(s) | [Client name/title] | Confirms product, performance, certification, and comparative claims |
| Client final approver | [Client decision-maker] | Approves strategic changes |
| Contributors | Rocket55 team, Claude | Propose changes via pull request; never commit to `main` directly |

**Client working style:** [e.g., "approvals stall on big reviews, so batch 3–5 facts per ask" or "engineers who expect evidence, so always cite data"]

## Document status

- `draft`: not yet confirmed by the client. **Not** loaded into Profound, **not** published.
- `client-approved`: confirmed by the client. Record who and when in `approved_by` / `approved_date`.
- `superseded`: replaced by a newer version, kept for history.

## Change workflow

1. **Branch + pull request** for every change, using the PR template.
2. **Source it.** Every fact needs a source (URL, Drive doc, Fathom link, or client email) and an as-of date.
3. **Client confirmation** for any product, performance, certification, approval, or comparative claim. Paste the approval (or a link to it) into the PR.
4. **Owner review.** `CODEOWNERS` plus branch protection enforce it.
5. **Log it** in `CHANGELOG.md`.
6. **Sync.** After merge, upload changed `client-approved` docs to Profound: "[Client] Core Context" for most folders, and "[Client] Compliance" for `compliance/`. Profound can't edit in place, so upload as `<name>-v2` and delete the old version in the Profound UI.

## Review cadence

- **Quarterly** full review, aligned with roadmap planning.
- **Immediately** when products, certifications, approvals, or capacity change, or when a meeting reverses a recorded decision.
- Every doc has a `review_by` date, and the validation check warns when it has passed.

## Decision stability

Recorded client decisions are the reference point for planning. If a later meeting changes one, update the doc via PR and note the impact on timeline and results in the PR description. Don't silently overwrite.

## What never goes in this repo

[Add client-specific exclusions, e.g., defense programs, customer names, export-controlled data.]

- Customer PII or other clients' data
- Unverified competitor claims
- Pricing, CRM, or lead data
- Large binaries (CAD, PDFs): index them in `resources/` instead
- Passwords, API keys, or access tokens
