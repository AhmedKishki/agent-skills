# Source maps

Record a source's exact excerpts and locations in `{project}-source-map-{code}-{author-short-title}.md`.

## Procedure

1. Establish the source and reading scope with the user. Read the accessible original independently.
2. Propose relevant excerpts, preserving their subject, scope, modality and qualifications. Ask the user to confirm the selection or direct further extraction.
3. Save the accepted excerpts in source order. Update reading coverage and access limits in the source's tracker row.
4. Refresh the index after the accepted map changes.

Choose contiguous passages centred on one claim or topic. For omissions within one bounded passage, retain source order and mark the join with `[…]`. Give different occurrences separate entries. Preserve additional occurrences when they add context or qualification.

## Output

```markdown
# Source A — Full author, full title

Original: [Original](original-file.pdf)

| Code | Location | Excerpt |
|---|---|---|
| A1 | Page 8, paragraph 2 | Reviewers check flagged results every day. |
```

Use exactly the identity heading, Original reference and Code / Location / Excerpt table. Every excerpt is attributed by the source heading. Put keyword/theme labels in the index and actual article uses in predraft.

Preserve supplied original filenames; use lowercase codes in map filenames. Identify the edition in Original when needed. Use source-native pages, sections or paragraph positions. Represent literal pipes as `\|` and excerpt line breaks as `<br>`; decoding these recovers the quotation's text.

## IDs and corrections

Allocate source codes A–Z, then AA onward. Allocate excerpt IDs A1, A2 and onward from `next item A2` in the map's tracker row. Retain retired allocation limits and existing IDs.

A verified transcription or locator correction retains its ID. Different material, splits or merges receive new IDs. Check user-edited excerpts against the original and resolve changed meaning with the user. Preserve originals still needed by current records.

Reopen source context when the intended claim changes, a quotation lacks context, the original changes, or the user requests a rescan. Record actual checked coverage even when access is partial.
