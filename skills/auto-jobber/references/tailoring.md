# Tailor the documents to the opportunity

## Match requirements before writing

Read the complete posting and distinguish required from preferred qualifications. Map them to supported, partial, gap or unknown evidence. Do not convert a gap into a skill claim. Record useful requirements, questions and research in the agreed application records; use the native plan fields when those helpers are selected.

## Select and adapt the CV

Choose the relevant experience, skills, projects and academic material for this opportunity. Adapt their emphasis, supported wording, section order and appearance as needed with the applicant. Do not change the factual source merely to fit a vacancy, force every optional project into the document, or rewrite good wording gratuitously.

If using a native application snapshot, its text patcher accepts only registered paired markers with plain escaped text. Cite its evidence and requirement IDs and provide exact baseline text. Its default three-block/15-percent limits apply within that snapshot. A different selection, order or design belongs in a reviewed source/layout revision and a fresh snapshot, not a hidden rewrite of the captured baseline. Agree any baseline-policy changes explicitly; never silently raise limits on an existing application.

## Draft the cover letter

Follow [Voice](voice.md) for the required motivation-letter outcomes, personal-input gate and tone. Its incomplete-factual-skeleton exception applies only when explicitly requested. With native helpers, complete their job-specific wording capture before building the letter.

Follow Entry notes to select relevant applicant comments about individual records. A letter may use that context even when the associated detail is omitted from the CV; source-review any new factual claim before using it as qualification evidence.

Build the argument required by Voice within the applicant's agreed length and structure. The native letter renderer uses 2–6 paragraphs and at most 450 words, with each sentence in one category:

- `candidate`: candidate claim with verified `evidence_ids` only.
- `company`: employer claim with `company_fact_ids` only.
- `bridge`: a defensible connection with both kinds of support; references alone do not prove that the proposed connection follows.
- `intent`: genuine application intent, without concealed factual qualifications or unsupported claims about the employer.

There is no default letter for an absent qualification profile. Ask for missing candidate evidence or stop before drafting. With unavailable research, omit company claims rather than filling them with boilerplate presented as researched facts.

## Draft a research statement

Follow [Research statement](research-statement.md) when the offer asks for one. The native helpers have no research-statement renderer, so author it in an agreed editable source, such as HTML/CSS, and apply the audit and rendering checks below to it.

## Audit and render

Audit each requirement mapping, CV change and letter sentence against the source and exact meaning, then apply Voice's letter-completion review. With native helpers, run `check`; it validates provenance links, quote containment and numeric literals, not semantic truth, source authenticity, the motivation argument or user consent. Complete applicant review before declaring the letter approved.

Render a fresh revision and inspect every page for clipping, overflow, blank regions, line breaks, information order, dates and places, contact details, portrait framing and readability. For native builds, review `cv.patch`, HTML, `report.json` and every generated PNG. Their PDF gates check geometry and text, not design quality. `--html-only` is a draft fallback, not PDF delivery, and failed staging files are not deliverables.

Apply SKILL's PDF delivery default to each requested document, including working drafts. Preserve its selected editable sources and report the output paths and draft/approval status accurately. If PDF rendering or every-page visual inspection is blocked, report the task as incomplete with the actual blocker and any available source or partial output; do not present HTML alone or an uninspected PDF as completed delivery. Fix missing previews or use another suitable inspection tool before claiming visual review. Producing or inspecting a PDF never records approval or submission.

Validated documents disallow external resource loading through HTML/CSS checks and CSP; Chrome runs with its sandbox enabled. These mitigations are not OS-level hard network isolation. Do not render arbitrary unvalidated web HTML.

Keep finished build contents unchanged so manifest verification remains meaningful. Record user/visual review outside that immutable build, then verify and archive the chosen revision. Archiving copies files locally and does not submit anything.
