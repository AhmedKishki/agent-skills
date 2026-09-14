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

Index: `{project}-arguments.md`

Definitions: `arguments/{project}-arguments-{first-ID}-{last-ID}.md`

### Inputs selected for synthesis

Index: `{project}-synthesis-material.md`

One bounded record per argument: `synthesis-material/{project}-synthesis-{ARG-nnn}.md`

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
- Keep indexes short. Split argument definitions into bounded range files and synthesis records into one file per argument; do not create monolithic substitutes elsewhere.
- Split an active index or range file before it exceeds either 250 lines or 20 KB. A file that crosses either limit requires immediate compaction or another bounded file; do not wait until the end of a stage.
- Never route archives, migration reports, broad research inventories or completed workflow history into active file families. Preserve recoverability in version control and retain only current actionable state.
- Store provenance and basis metadata with one owner. Link to it rather than duplicate it.
- Use no Markdown tables in active project files.
- Follow [Human-editable files](human-editable-files.md).

## Completion

Every file has one owner, every link resolves and no two live files claim the same function.