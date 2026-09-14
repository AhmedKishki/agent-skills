# Argument synthesis

## Purpose

Create and approve raw prose for one argument from its approved synthesis material, then record it in `{project}-argument-drafts.md`.

## Method

Use only Human inputs approved in synthesis material. Permitted operations are:

### COPY

Copy one contiguous Human span.

### INFLECT

Change tense, number, grammatical case, article or an unambiguous pronoun only.

### NORMALISE

Change meaning-neutral spelling, capitalisation or punctuation only.

### ORDER

Arrange spans only when an approved input establishes their relation.

### DELETE

Remove repetition only when subject, scope, modality and qualification remain unchanged.

Every output word, including joins, must occur in an approved Human input in the required sense. Otherwise return a gap or obtain approval for another disclosed method.

## Procedure

1. Verify that the argument definition and synthesis material were approved together as one package.
2. Resolve recursive argument inputs to finite Human lineage.
3. Construct one candidate using only permitted operations.
4. Record construction steps outside the candidate in `{project}-synthesis-material.md` under that argument's `### Construction record`.
5. Present the complete candidate and record.
6. Ask whether the user approves the candidate or what should change.
7. Save approved prose in argument drafts. Keep article order and transitions out of it.

## Argument-draft format

```markdown
# Argument drafts

> **Editing note:** You may edit this file directly. These drafts are unordered and do not determine article order.

## ARG-001 — Short claim name

**Status:** Approved

### Draft

<Approved raw argument prose.>

### Basis

- U-003
- A4
```

## Gaps

Name one precise gap: missing user wording, missing evidence, unsupported connection, source ambiguity, source–user conflict, schema inconsistency or constraint conflict. State what is missing and ask one focused question.

## Completion

The approved raw prose establishes only the approved argument, preserves qualifications and has finite Human lineage.