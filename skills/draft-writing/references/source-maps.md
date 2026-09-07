# Source maps

## Purpose

Preserve one source's exact approved excerpts and locations under stable codes in `{project}-source-map-{code}-{author-short-title}.md`.

## Inputs

An accessible original, an agreed reading scope and the next source and excerpt codes from the tracker.

## Procedure

1. Confirm the source identity and reading scope, then read the accessible original independently.
2. Select a contiguous excerpt only when it contains wording required for a stated claim, qualification, counterclaim, definition or context. Include enough surrounding text to determine subject, scope, modality and qualification.
3. Present one excerpt batch for that source and scope; obtain approval of the exact excerpts.
4. Save approved excerpts in source order and update reading coverage, access limits and the next excerpt ID in the tracker.

Choose contiguous passages centred on one claim or topic. For omissions within one bounded passage, retain source order and mark the join with `[…]`. Give different occurrences separate entries. Preserve additional occurrences when they add context or qualification.

## Output

```markdown
| Code | Excerpt | Location |
|---|---|---|
| A1 | Reviewers check flagged results every day. | Page 8, paragraph 2 |
```

The file contains only one `Code | Excerpt | Location` table. Add no heading, Original field, second table, keyword, theme, role, qualification, interpretation, intended-use, argument, passage or selection-status column. The filename identifies the source; the tracker lists its original. Predraft's full approval record explains use, context, support and limits.

Preserve supplied original filenames in the tracker and use lowercase codes in map filenames. Include edition information in the tracker row when editions have different text or locators. Use source-native pages, sections or paragraph positions. Represent literal pipes as `\|` and excerpt line breaks as `<br>`; decoding these recovers the quotation's text.

## IDs and corrections

Allocate source codes A–Z, then AA onward. Allocate excerpt IDs A1, A2 and onward from `next item A2` in the map's tracker row. Retain retired allocation limits and existing IDs.

A verified transcription or locator correction retains its ID. Different material, splits or merges receive new IDs. Check user-edited excerpts against the original and resolve changed meaning with the user. Preserve originals still needed by current records.

Reopen source context when the intended claim changes, a quotation lacks context, the original changes, or the user requests a rescan. Record exact checked coverage even when access is partial.

## Completion condition

Every saved row was approved, reproduces the original exactly, has a resolving locator and follows source order.

## Blocking condition

Unavailable originals, ambiguous transcription, missing location or unapproved selection blocks the affected excerpt.

## Next owner

Predraft retrieves exact excerpts and inspects original context before proposing a passage use.
