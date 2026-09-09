# Shared file standard

## Purpose

Define shared filenames, headings, status placement, links and field order for draft-writing files.

## Inputs

The project name and the output schema in the active task module.

## Procedure

1. Prefix canonical files with stable `{project}-` filenames and edit them in place.
2. Follow the task module's exact heading levels and field order.
3. Use relative Markdown links. Link to section and passage headings; identify a plain-text argument by its full number through its passage link.
4. Form heading anchors by lowercasing and omitting dots: `1.1 — Passage` becomes `#11--passage`.
5. Create a canonical file only when its module has accepted content to store. Include an optional field only when the module names both the field and its inclusion condition.
6. In thesis-and-vision and user-wording, place an approved `**Status: Outdated** — <scope and approved replacement>` immediately after the exact superseded aspect. Preserve the original text; unmarked content remains operational.

| Content | Filename after the prefix |
|---|---|
| Governing direction | `thesis-and-vision.md` |
| Exact user language | `user-wording.md` |
| One source's excerpts | `source-map-{code}-{author-short-title}.md` |
| Structural plan | `article-arc.md` |
| Current unapproved passage | `predraft-working.md` |
| Approved raw passages | `predraft.md` |
| Connected article | `draft.md` |
| Resumption cursor and inventory | `activity-tracker.md` |

Thesis, arc and draft place `Status: Working | Needs review | Approved` immediately below the H1. The draft may use `Status: Complete` only after the user declares the article finished.

## Output

A file conforming exactly to the active module's schema and these shared conventions.

## Completion condition

All required fields occur once in the prescribed order, every relative link and heading anchor resolves, and each `Outdated` marker is adjacent to preserved superseded content and identifies its operative replacement.

## Blocking condition

Stop and ask one focused question when the project name, required schema or intended link target is ambiguous.

## Next owner

Return the conforming file to the module that requested it.
