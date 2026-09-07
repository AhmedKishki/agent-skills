# User wording

## Purpose

Preserve exact reusable user-authored article language under stable IDs in `{project}-user-wording.md`.

## Inputs

Text authored by the user and intended or potentially intended to appear in the article.

## Procedure

1. Separate article language from instructions using the shared routing table.
2. Preserve exact spelling, punctuation, qualifications and paragraph breaks. Reuse an existing ID only for an exact duplicate; allocate a new ID for a revision or partial overlap.
3. Allocate `user-n` from the tracker's Next user number and advance it. Keep IDs stable and retain retired allocation limits.
4. Add the entry below. Ask about unclear authorship or whether a passage is intended as article language.

Do not capture procedural commands, approval or rejection statements, workflow comments, or source quotations. Capture is mechanical preservation; predraft selection requires explicit approval of the resulting passage.

## Output

```markdown
# User wording

## user-1 — Short topic

> Exact user passage.
>
> Its next paragraph.
```

Use one H1, then H2 entries in allocation order. Wrap every passage line, including blank lines, in one blockquote level. Removing that wrapper recovers the exact wording. References resolve to the passage.

For mixed or uncertain origin, add the [compact provenance line](provenance.md#compact-declaration) after the blockquote and a short `Note:` identifying the affected portion. Clarify unresolved authorship before using the entry.

Directions belong in thesis, structural choices in arc, and actual uses and selections in predraft. Execute routine commands such as “apply this” and “next” without allocating wording IDs.

## Earlier wording

Once approved provenance cites a `user-n`, its exact text is immutable. Give a later rewrite a new `user-n`; retain the earlier entry while any selected passage depends on it. Correct only a verified transcription error in place and invalidate affected passages when the correction changes saved wording.

## Completion condition

Every eligible contribution is preserved exactly once under a stable ID, and every cited original remains recoverable.

## Blocking condition

Unclear authorship or uncertainty about whether text is intended as article language blocks capture of that text only.

## Next owner

Predraft proposes exact `user-n` spans as passage inputs.
