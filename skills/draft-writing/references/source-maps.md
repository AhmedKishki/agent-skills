# Source maps

## Purpose

Preserve one source's exact approved excerpts and locations under stable codes in `{project}-source-map-{code}-{author-full-source-title}.md`.

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
# Author, Full Source Title

## A1 — Short topic, location

> Exact source wording
>
> Its next paragraph
```

The file contains one H1 naming the author and full source title, followed by one H2 and blockquote per approved excerpt. Add no Original field, table, keyword, theme, role, qualification, interpretation, intended-use, argument, passage or selection-status field. The filename identifies the source; the tracker lists its original. Predraft-working records proposed use, context, support and limits.

Preserve supplied original filenames in the tracker. In map filenames, use the lowercase source code followed by a lowercase hyphenated rendering of the author's full name and the full source title; omit punctuation but do not abbreviate either. Include edition information in the tracker row when editions have different text or locators. Use source-native pages, sections or paragraph positions in each excerpt heading. Preserve each source paragraph as a blockquote paragraph; represent a blank line between source paragraphs as an empty `>` line. Removing one blockquote marker and its following space from each quoted line must recover the exact source wording and paragraph breaks.

## IDs and corrections

Allocate source codes A–Z, then AA onward. Allocate excerpt IDs A1, A2 and onward from `next item A2` in the map's tracker row. Retain retired allocation limits and existing IDs.

A verified transcription, short-topic or locator correction retains its ID. Different source wording, splits or merges receive new IDs. Check user-edited excerpts against the original and resolve changed meaning with the user. Preserve originals still needed by current records.

Reopen source context when the intended claim changes, a quotation lacks context, the original changes, or the user requests a rescan. Record exact checked coverage even when access is partial.

## Completion condition

Every saved excerpt was approved, its blockquote reproduces the original exactly, its H2 has the stable code, short topic and resolving locator, and the excerpt headings follow source order.

## Blocking condition

Unavailable originals, ambiguous transcription, missing location or unapproved selection blocks the affected excerpt.

## Next owner

Schema and predraft retrieves exact excerpts and inspects original context before proposing an argument use.
