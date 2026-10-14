# Governance

How content in this repo is created, approved, published, and retired.

## Roles

| Role | Who | Responsibility |
|---|---|---|
| Repo owner | Jen Jones (Rocket55) | Reviews every pull request, merges to `main`, owns sync to Profound |
| Account manager | Evan (Rocket55) | Flags client decisions from meetings that need to land here |
| Technical approver | Gus / Bill (AlumiPlate) | Confirms all product, performance, and approval claims |
| Contributors | Rocket55 team, Claude | Propose changes via pull request — never commit to `main` directly |

## Document status

Every document carries `status` in its header:

- `draft` — written, not yet confirmed by the client. **Not** loaded into Profound, **not** published.
- `client-approved` — confirmed by AlumiPlate. Record who and when in `approved_by` / `approved_date`.
- `superseded` — replaced by a newer version; kept for history.

## Change workflow

1. **Branch + pull request.** Every change, however small, goes through a PR using the PR template.
2. **Source it.** Every new fact needs a source (URL, Drive doc, Fathom call link, or client email) and an as-of date.
3. **Client confirmation** for any product, performance, certification, or approval claim. Send Gus/Bill a short PDF or Google Doc of the change; paste their approval (or a link to the email) into the PR.
4. **Owner review.** Jen approves and merges. Branch protection on `main` enforces this via `CODEOWNERS`.
5. **Log it.** Add a line to `CHANGELOG.md`.
6. **Sync.** After merge, upload changed `client-approved` docs to the Profound "AlumiPlate Core Context" knowledge base. Profound can't edit in place: upload as `<name>-v2`, then delete the old version in the Profound UI.

## Review cadence

- **Quarterly** full review (aligned with roadmap planning).
- **Immediately** when: approvals/certifications change (e.g., ISO or NADCAP achieved), products or capacity change, the Hawk partnership is announced, or a client meeting reverses a prior decision.
- Each doc has a `review_by` date; the validation check warns when it has passed.

## Decision stability

Client decisions recorded here are the reference point for planning. If a later meeting changes one, update the doc via PR and note the impact on timeline/results in the PR description — don't silently overwrite.

## What never goes in this repo

- Customer PII or other clients' data
- Unverified competitor claims
- Passwords, API keys, or access tokens
