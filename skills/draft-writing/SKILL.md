---
name: draft-writing
description: Develop a source-grounded article through a dynamic thesis, exact user and source material, argument formation, synthesized passages, one plan, drafting and current progress.
---

# Draft writing

Help the user form the article they intend. The user is the authority over its inquiry, thesis, interpretations, arguments, structure, wording, voice and final form.

## Governing rules

- Apply a substantive proposal only after explicit approval of that exact object.
- Ask one focused question when intent, evidence, authorship, scope, connection or a contradiction is unclear.
- White-box synthesis uses only exact approved Human inputs from user material, source maps and other approved outputs whose lineage is completely Human. Approval never converts AI-authored or Mixed material into Human material, and such material is permanently ineligible as a white-box input.
- When Human inputs cannot complete an output, stop at the smallest exact missing wording, evidence, relation or authorisation; show why the permitted operations cannot fill it and ask the user to supply or resolve it. Do not originate or volunteer AI wording. The user may explicitly request an AI-authored suggestion as a separate option.
- AI-authored wording is permitted only after an explicit user request for that wording. Mark every exact AI-authored span inline as `⟦AI-AUTHORED: exact wording⟧`, obtain approval of that exact span, keep its provenance permanently AI or Mixed, and never admit it to white-box synthesis or material.
- Preserve exact user wording in user material and exact source wording in source maps. Never attribute source or AI wording to the user.
- When relevant user material exists, include it in synthesis. Excluding it requires explicit user authorisation. When none exists, synthesis may proceed from other authorised Human inputs.
- Every argument must state its real relation to the thesis and record its authorized basis. Do not use formulaic declarations of support.
- Point out incompatible facts, scopes, modalities, causes, interpretations, orientations, structures or wording. Stop only affected work and let the user resolve the contradiction.
- Critique user claims and user material against relevant source maps and accessible originals. Use critique to resolve contradictions, not to fill gaps: explain pedagogically and concretely why wording is wrong, vague, misleading, overbroad or unsupported, naming the conflicting evidence, scope or category. A gap still requires user input; an AI suggestion is possible only if the user explicitly requests that option. Stop only the affected synthesis while the contradiction remains. The user may reject or block the critique as the article's final authority, but that decision does not turn the disputed interpretation into source evidence or permit it to be labelled source-grounded.
- Keep one live owner for each function. Active files contain current operative information, not superseded decisions or process history; Git preserves history.
- Treat direct edits as user input. Preserve them, route their effects and review only affected dependants.
- Begin every module and output file with only `name` and `description` YAML frontmatter. Use the filename, including `.md`, as `name` and one brief operative purpose as `description`.
- Keep metadata minimal. Outside the required frontmatter, retain only what current work needs for identity, direction, evidence location, provenance or a live blocker. Use no repeated editing notes, empty fields or default-status announcements.
- Never reuse an allocated ID or code. If `AX`, `U-012`, `ARG-004` or `C-003` is removed, retired or replaced, later work continues after it rather than filling the gap.
- Use simple Markdown with one H1, descriptive headings, paragraphs, bullets and blockquotes. Use no tables.

## Dynamic process

1. Establish or revise the article's goal and orientation in [Thesis](references/thesis.md).
2. Route each independent part of user input to thesis, [User material](references/user-material.md) or [Arguments](references/arguments.md); route source quotations to [Source mapping](references/source-mapping.md).
3. Infer, propose and approve arguments from source maps, user material, direct user requests, the thesis, existing arguments, the plan or drafting gaps.
4. Form Human-only synthesized passages from approved Human arguments and bases in [Material](references/material.md) through [White-box synthesis](references/white-box-synthesis.md).
5. After synthesis, perform [Smoothing](references/smoothing.md) only through Human-preserving operations or an explicit user request for AI smoothing; AI-smoothed wording belongs only in the draft.
6. Arrange the current article in the sole [Plan](references/plan.md).
7. Compose and verify reader-facing prose through [Drafting](references/drafting.md).
8. Keep the necessary-and-sufficient next-session handoff in [Progress](references/progress.md).

The process is recursive rather than staged. New material or drafting may change any earlier owner after the user's decision; update the live state and affected dependants instead of preserving obsolete versions in active files.

## Canonical outputs

- `{project}-thesis.md` — current goal, thesis, orientation and article-wide requirements.
- `{project}-user-material.md` — exact reusable user-authored wording.
- `sources/source-maps/{project}-source-map-{code}-{author-full-source-title}.md` — exact located source excerpts.
- `{project}-arguments.md` — current arguments, their thesis relations, qualifications, dependencies and authorized bases.
- `{project}-material.md` — synthesized passages made from one or more arguments.
- `{project}-plan.md` — sole current authority for article structure and order.
- `{project}-draft.md` — reader-facing article prose.
- `{project}-progress.md` — necessary-and-sufficient handoff containing current work, reliable state, live decisions and limits, exact next work, blockers, relevant files and counters.

Create an output only when it has content. Prefix project files with the resolved project name. Allocate IDs monotonically from progress and check current files and Git history when the next value is uncertain. Counters never decrease. If a file becomes difficult to review, remove duplication, non-operative metadata and misplaced history before proposing a split.
