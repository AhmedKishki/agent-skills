---
name: source-mapping.md
description: Defines how exact relevant source wording and locations are preserved.
---

# Source mapping

## Accepts

An identified source, an accessible original, a defined reading scope and exact contiguous passages relevant to current work. A user-supplied quotation is accepted here as source-authored material when its identity and location can be established.

Do not accept user interpretation, argument assignments, intended uses, synthesized wording, approval history or broad inventories.

## Owns

One source map per source owns exact relevant source wording and its location.

## Procedure

1. Confirm source identity and reading scope.
2. Read the accessible original independently.
3. Select a contiguous passage only when it supplies evidence, context, a qualification, definition or counterclaim needed by current work.
4. Include enough context to preserve subject, scope, modality and qualification.
5. Present one exact excerpt batch for approval.
6. Save only approved excerpts in source order under stable codes.
7. Record checked coverage and the next excerpt code in progress, not in the map.

## Standard structure

```markdown
---
name: "{project}-source-map-{code}-{author-full-source-title}.md"
description: Preserves exact relevant excerpts and locations from one source.
---

# Author, Full Source Title

## A1 — Short topic

**Location:** Page 4

> Exact source wording.
>
> Its next paragraph.
```

Use one H1, then one H2 per excerpt. Add no interpretation, role, intended use, argument, approval history or workflow metadata. A source quotation remains source-authored even when supplied by the user.

## Corrections

A verified transcription or locator correction retains its ID. Different wording, a split or a merge receives a new ID. Never reuse a removed or retired source or excerpt code; advance the counter in progress. Reopen the original when intended use changes or context is insufficient.

## Completion

Every excerpt is approved, exact, located and in source order.
