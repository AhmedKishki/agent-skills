# White-box synthesis

## Purpose

Transform one approved schema argument and one approved limited Human input set into Human raw material with a complete record, or return one gap.

## Inputs

- Exact `ARG-nnn` claim and qualifications.
- Only the limited input set approved for this run.
- Exact Human `user-n`, `src:A1` or approved Human `arg:ARG-001` spans, locations, lineage, context, intended use, support and limits.
- Authorial-voice and language constraints.

Do not use a broad schema inventory as the input set. Do not accept Mixed, AI or Unverified input.

## Operations

| Operation | Exact limit |
|---|---|
| COPY | Copy one contiguous Human span. |
| INFLECT | Change tense, number, grammatical case, article or an unambiguous pronoun only. |
| NORMALISE | Change meaning-neutral spelling, capitalisation or punctuation only. |
| ORDER | Arrange spans only when an approved input establishes their relation. |
| DELETE | Remove repetition only when subject, scope, modality and qualification are unchanged. |

Every output word, including words at joins, must occur in an approved Human input in the required sense. Record every operation. Preserve quotations, names, titles, URLs, codes and citation data exactly.

## Procedure

1. Verify that every input is Human. Resolve each `arg:ARG-nnn` input through a finite lineage to ultimate source/user codes.
2. Check every source input against user wording under the [source–user conflict protocol](ownership-and-routing.md#sourceuser-conflict). Stop on a possible conflict.
3. Match approved inputs to the argument claim and qualifications.
4. Apply only the permitted operations.
5. Check that the output establishes exactly the argument claim.
6. Return the candidate and full record, or one typed gap.

## Output

```markdown
Argument: ARG-001

Raw material: <complete candidate>

**Provenance:** Human · **Method:** white-box synthesis · **Basis:** A1, user-21

Record:

| Argument | Result span | Human inputs | Construction and support |
|---|---|---|---|
| ARG-001 | <complete output> | <exact spans, codes, locations and lineage> | <operations, support and limits> |
```

Flatten compact `Basis` to ultimate source/user codes. Keep intermediate `arg:ARG-nnn` references in the full record.

## Gaps

Use exactly one: `Missing user wording`, `Missing evidence`, `Unsupported connection`, `Source-context ambiguity`, `Source–user conflict`, `Schema inconsistency` or `Constraint conflict`. State the argument ID, missing requirement, owner, one focused question and allowed resolution paths.

Use `Constraint conflict` when required input is Mixed, AI or Unverified. Any alternative method must be separately disclosed and explicitly approved outside white-box synthesis.

## Completion

Every input is Human; every span is reconstructable; lineage is finite; qualifications remain; the output establishes only the approved claim; authorial voice passes validation.

## Next owner

Schema and predraft presents the complete candidate and record to the user.