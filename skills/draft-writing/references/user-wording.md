# User wording

Preserve reusable human article language in `{project}-user-wording.md`: passages, definitions, arguments, titles and meaningful fragments supplied in conversation or identified direct edits.

## Capture

1. Separate article language from instructions using the shared routing table.
2. Preserve exact spelling, punctuation, qualifications and paragraph breaks. Reference an existing entry when its wording is already present.
3. Allocate `user-n` from the tracker's Next user number and advance it. Keep IDs stable and retain retired allocation limits.
4. Add the entry below. Ask about unclear authorship or whether a passage is intended as article language.

Capture is mechanical preservation. Predraft selection requires explicit approval of the resulting paragraph.

## Output

```markdown
# User wording

## user-1 — Short topic

> Exact user passage.
>
> Its next paragraph.
```

Use one H1, then H2 entries in allocation order. Wrap every passage line, including blank lines, in one blockquote level. Removing that wrapper recovers the exact wording. References resolve to the passage.

For mixed or uncertain origin, add the [compact provenance line](file-output-standard.md#compact-provenance) after the blockquote and a short `Note:` identifying the affected portion. Use verified basis codes when available; clarify the unresolved portion before using it. Source quotations remain source material; assistant arrangements retain their origin.

Directions belong in thesis, structural choices in arc, and actual uses and selections in predraft. Execute routine commands such as “apply this” and “next” without allocating wording IDs.

## Earlier wording

Preserve user edits in place. If a saved provenance trail still needs the previous exact passage, retain it under a final `## Earlier wording still in use`, using H3 `### user-n — Earlier wording of user-m` and the same blockquote format. Allocate from the same counter and update the affected Basis reference. Request recovery when the required original is unavailable.
