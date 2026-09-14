# File names

## Purpose

Give each article-making function one predictable file or file family.

## Canonical files

### Thesis

`{project}-thesis.md`

### Draft direction

`{project}-draft-direction.md`

### Exact user material

`{project}-user-material.md`

### Source maps

`sources/source-maps/{project}-source-map-{code}-{author-full-source-title}.md`

### Unordered arguments

`{project}-arguments.md`

### Inputs selected for synthesis

`{project}-synthesis-material.md`

### Approved raw argument prose

`{project}-argument-drafts.md`

### Sole structural plan

Live file: `{project}-article-arc.md`

Approved snapshot: `{project}-article-arc-vN.md`

### Article prose

Live file: `{project}-draft.md`

Finalised snapshot: `{project}-draft-vN.md`

### Citation work

`{project}-citations.md`

Approved cited draft: `{project}-cited-draft-vN.md`

### Current workflow state

`{project}-progress.md`

## Rules

- Prefix every canonical project file with the resolved project name.
- Keep immutable approved snapshots unchanged. Make revisions in the live file.
- Use relative Markdown links and stable IDs in headings.
- Create a file only when it has material to store.
- Keep canonical files lean by omitting empty sections, `None` fields, default statuses, repeated instructions and duplicated content. Do not fragment one conceptual owner merely because boilerplate inflated it.
- If a canonical file becomes difficult to review, diagnose misplaced material and repetition first. Split it only when distinct coherent owners genuinely exist or the user explicitly requests a split.
- Never route archives, migration reports, broad research inventories or completed workflow history into active project files. Preserve recoverability in version control and retain only current actionable state.
- Store provenance and basis metadata with one owner. Link to it rather than duplicate it.
- Use no Markdown tables in active project files.
- Follow [Human-editable files](human-editable-files.md).

## Completion

Every file has one owner, every link resolves and no two live files claim the same function.