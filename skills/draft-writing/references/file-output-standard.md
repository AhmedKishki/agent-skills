# Shared file standard

## Purpose

Define shared filenames, headings, status placement, links and field order for draft-writing files.

## Inputs

The project name and the output schema in the active task module.

## Procedure

1. Prefix canonical files with stable `{project}-` filenames and edit them in place.
2. Put a mutable state or immutable version after the base name: `{base}-working.md` or `{base}-vN.md`.
3. Follow the task module's exact heading levels and field order.
4. Use relative Markdown links. Link to exact argument, passage or section headings.
5. Form anchors from the exact heading text under standard Markdown rules.
6. Create a file only when its module has content to store. Do not create an empty working file.
7. In thesis-and-vision and user-wording, place an approved `**Status: Outdated** — <scope and approved replacement>` immediately after the exact superseded aspect. Preserve the original text; unmarked content remains operational.

| Content | Filename after the prefix |
|---|---|
| Governing direction | `thesis-and-vision.md` |
| Exact user language | `user-wording.md` |
| One source's excerpts | `source-map-{code}-{author-full-source-title}.md` |
| Argument schema | `predraft-schema.md` |
| Current unapproved argument | `predraft-working.md` |
| Approved raw arguments | `predraft.md` |
| Current blueprint | `blueprint-working.md` |
| Approved blueprint snapshot | `blueprint-vN.md` |
| Current draft | `draft-working.md` |
| Finalised uncited draft | `draft-vN.md` |
| Current citation work | `citation-working.md` |
| Approved cited draft | `cited-draft-vN.md` |
| Resumption cursor and inventory | `activity-tracker.md` |

Thesis and predraft schema place `Status: Working | Needs review | Approved` below the H1. Blueprint-working and draft-working use their module states. Versioned blueprints use `Approved`; uncited draft versions use `Finalised`; cited draft versions use `Approved` or `Complete`. Use `Complete` only when the user declares the article finished.

Use the listed names exactly. Do not write `working-blueprint.md`, `working-draft.md`, `working-predraft.md` or `working-citation.md`.

## Output

A file conforming exactly to the active module's schema and these shared conventions.

## Completion condition

All required fields occur once in the prescribed order, every relative link and heading anchor resolves, and each `Outdated` marker is adjacent to preserved superseded content and identifies its operative replacement.

## Blocking condition

Stop and ask one focused question when the project name, required schema or intended link target is ambiguous.

## Next owner

Return the conforming file to the module that requested it.
