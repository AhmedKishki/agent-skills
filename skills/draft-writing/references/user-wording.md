# User wording

## Purpose

Preserve exact reusable user-authored article language under stable IDs in `{project}-user-wording.md`.

## Inputs

Text authored by the user and intended or potentially intended to appear in the article.

## Procedure

1. Separate article language from instructions using the shared routing table.
2. Preserve exact spelling, punctuation, qualifications and paragraph breaks. Reuse an existing ID only for an exact duplicate; allocate a new ID for a revision or partial overlap.
3. Allocate `user-n` from the tracker's Next user number and advance it. Keep IDs stable and retain retired allocation limits.
4. Add the entry below. Ask when authorship or intended article use is unclear.
5. Treat each entry and each unaffected aspect as operational unless it is explicitly marked `Outdated`. When new wording may contradict it, follow [ownership and routing](ownership-and-routing.md) before changing currency.

Do not capture procedural commands, approval or rejection statements, workflow comments, or source quotations. Capture is mechanical preservation; predraft use requires separate approval.

## Output

```markdown
# User wording

## user-1 — Short topic

> Exact user wording.
>
> Its next paragraph.
```

Use one H1, then H2 entries in allocation order. Wrap every wording line, including blank lines, in one blockquote level. Removing that wrapper recovers the exact wording. References resolve to the entry.

After explicit confirmation that contradictory new wording shall become operative, preserve the earlier entry and add immediately below its blockquote:

```markdown
**Status: Outdated** — <exact affected aspect and approved replacement>
```

For partial supersession, name the exact outdated span or proposition; all unmarked aspects remain operational. The lack of an `Outdated` marker means the entry is operational.

For mixed or uncertain origin, add the [compact provenance line](provenance.md#compact-declaration) after the blockquote and a short `Note:` identifying the affected portion. Clarify unresolved authorship before using the entry.

Directions belong in thesis, arguments in predraft schema, article structure in blueprint and actual uses in predraft or draft. Execute routine commands such as “apply this” and “next” without allocating wording IDs.

## Earlier wording

Once approved provenance cites a `user-n`, its exact text is immutable. Give a later rewrite a new `user-n`; retain the earlier entry and mark only the superseded aspect `Outdated` after the user makes the replacement operative. Correct only a verified transcription error in place; invalidate affected raw arguments, blueprint uses and draft sections when the correction changes saved wording.

## Completion condition

Every eligible contribution is preserved exactly once under a stable ID, every cited original remains recoverable, and every superseded aspect has an adjacent `Outdated` marker that identifies its operative replacement.

## Blocking condition

Unclear authorship or uncertainty about whether text is intended as article language blocks capture of that text only.

## Next owner

Schema and predraft proposes exact `user-n` spans as Human argument inputs.
