---
name: draft-writing
description: Develop a source-grounded article through a dynamic draft thesis, exact user and source material, white-box synthesis, one draft plan, drafting and current progress.
---

# Draft writing

Help the user form the article they intend. The user is the authority over its inquiry, thesis, interpretations, arguments, structure, wording, voice and final form.

## Governing rules

- Apply a substantive proposal only after explicit approval of that exact object.
- Ask one focused question when intent, evidence, authorship, scope, connection or a contradiction is unclear.
- Use only user-authorised material from the user or sources. Do not add an AI claim, connection or article wording without disclosing and obtaining approval for the exact bounded addition.
- Preserve exact user wording in user material and exact source wording in source maps. Never attribute source or AI wording to the user.
- When relevant user material exists, include it in synthesis. Excluding it requires explicit user authorisation. When none exists, synthesis may proceed from other authorised Human inputs.
- Every claim and argument must state its real relation to the draft thesis. Do not use formulaic declarations of support.
- Point out incompatible facts, scopes, modalities, causes, interpretations, orientations, structures or wording. Stop only affected work and let the user resolve the contradiction.
- Keep one live owner for each function. Active files contain current operative information, not superseded decisions or process history; Git preserves history.
- Treat direct edits as user input. Preserve them, route their effects and review only affected dependants.
- Use simple Markdown with one H1, descriptive headings, paragraphs, bullets and blockquotes. Use no tables, repeated editing notes, empty fields or default-status announcements.

## Dynamic process

1. Establish or revise the article's goal and orientation in [Draft thesis](references/draft-thesis.md).
2. Preserve relevant exact contributions through [User material](references/user-material.md) and exact evidence through [Source mapping](references/source-mapping.md).
3. Form claims, arguments, connections and developing prose in [Draft material](references/draft-material.md).
4. Transform authorised inputs with [White-box synthesis](references/white-box-synthesis.md).
5. Arrange the current article in the sole [Draft plan](references/draft-plan.md).
6. Compose and verify reader-facing prose through [Drafting](references/drafting.md).
7. Keep the resumption state in [Draft progress](references/draft-progress.md).

The process is recursive rather than staged. New material or drafting may change any earlier owner after the user's decision; update the live state and affected dependants instead of preserving obsolete versions in active files.

## Canonical outputs

- `{project}-draft-thesis.md` — current goal, thesis, orientation and article-wide requirements.
- `{project}-user-material.md` — exact reusable user-authored wording.
- `sources/source-maps/{project}-source-map-{code}-{author-full-source-title}.md` — exact located source excerpts.
- `{project}-draft-material.md` — claims, arguments, their thesis relations, inputs and developing synthesis.
- `{project}-draft-plan.md` — sole current authority for article structure and order.
- `{project}-draft.md` — reader-facing article prose.
- `{project}-draft-progress.md` — current work, achieved state, next work, blockers and counters.

Create an output only when it has content. Prefix project files with the resolved project name. Keep stable IDs where references or provenance require identity. If a file becomes difficult to review, remove duplication, metadata and misplaced history before proposing a split.
