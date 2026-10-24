# Minimal tailoring and review

## Match requirements before writing

Extract requirements from the complete posting into the plan, distinguishing
required from preferred. Mark each supported, partial, gap or unknown using
verified candidate evidence. Do not convert a gap into a skill claim to improve fit.
Record unresolved questions and limitations in `review.open_questions`/`notes`.

## Preserve the CV

Edit only registered paired `<!-- cv:id -->…<!-- /cv:id -->` regions containing
plain escaped text. The plan supplies the exact decoded baseline `before` text;
the script rejects stale text and escapes `after` when inserting it.
Keep edits to summary, bullet or skills wording that the cited evidence supports.
Default budgets are three changed blocks and 15% changed words relative to the
whole visible baseline; the script counts changed token spans, not characters.
Do not silently raise these limits. Prefer no edit to a gratuitous rewrite.

Do not remove content, roles or sections, change job titles/dates, reorder the CV,
or edit CSS/structure per vacancy. Give every edit candidate evidence IDs,
requirement IDs and a reason. Layout or factual baseline corrections belong in a
separately reviewed master update, not hidden inside an application patch.

## Draft the cover letter

Complete the Voice dialogue/capture gate first, then shape the user's words around
their supported examples and this job's requirements. Retained style guidance
helps with phrasing; it does not replace current-job motivation.

Use 2–6 paragraphs with at most 450 words of sentence text. Select specific,
relevant evidence rather than repeating the CV. Keep each sentence in one category:

- `candidate`: candidate claim with verified `evidence_ids` only.
- `company`: employer claim with `company_fact_ids` only.
- `bridge`: a defensible connection with both kinds of support; references alone
  do not prove that the proposed connection follows.
- `intent`: genuine application intent, without concealed factual qualifications
  or unsupported claims about the employer.

There is no default letter for an absent qualification profile. Ask for missing
candidate evidence or stop before drafting. With unavailable research, omit company
claims rather than filling them with boilerplate presented as researched facts.

## Audit and render

Run `check`, then audit each requirement mapping, CV edit and letter sentence
against its cited source and exact meaning. The code validates provenance links,
quote containment and numeric literals; it does not validate semantic truth,
entailment, source authenticity or the correctness of user verification flags.
Complete Voice's applicant review before declaring the letter approved.

Build a fresh revision. Review `cv.patch`, the standalone HTML and `report.json`.
PDF gates check page size/count and extracted text. Open every generated PNG for
both documents: inspect clipping, overflow, blank pages, line breaks, headings,
spacing, contact details and readability. Missing previews require fixing the
preview tool before declaring visual review complete. `--html-only` is a draft
fallback, not a successful PDF delivery. Failed staging files are not deliverables.

Validated documents disallow external resource loading through HTML/CSS checks
and CSP; Chrome runs with its sandbox enabled. These mitigations are not OS-level
hard network isolation. Do not render arbitrary unvalidated web HTML.

Keep finished build contents unchanged so manifest verification remains meaningful.
Record user/visual review outside that immutable build, then verify and archive the
chosen revision. Archiving copies files locally and does not submit anything.
