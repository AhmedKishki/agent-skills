---
name: white-box-synthesis.md
description: Defines reconstructable synthesis from authorised Human inputs.
---

# White-box synthesis

## Accepts

A finite set of exact, user-authorised Human inputs identified directly by their stable labels, such as `U-012`, `F3` or `MAT-002`: user-material spans, source-map excerpts, or earlier outputs whose lineage resolves completely to such spans.

Relevant user material must be among the inputs when it exists. Excluding it requires explicit user authorisation. Source wording remains source-authored, and approval changes neither authorship nor evidentiary scope. Mixed, AI or unverified material is not a Human input.

## Produces

An output identified directly by its exact proposed label, such as `ARG-004` or `MAT-005`, whose meaning-bearing wording and relations are reconstructable from the authorised inputs through disclosed human-preserving operations. The output may be a claim, argument, connection, plan unit or prose passage and belongs in that output's canonical owner.

## Human-preserving operations

- **COPY** — copy one contiguous input span.
- **INFLECT** — change tense, number, grammatical case, article or an unambiguous pronoun only.
- **NORMALISE** — make meaning-neutral spelling, capitalisation, typography or punctuation changes only.
- **ORDER** — arrange spans only when an authorised input establishes their relation.
- **DELETE** — remove material only while subject, scope, modality, qualification and relation remain unchanged.

No operation may invent a join, causal relation, comparison, abstraction, conclusion, qualification, metaphor or interpretation.

## Procedure

1. Identify the bounded output and every exact input needed to form it.
2. Confirm that the user authorised those inputs for this synthesis.
3. Include relevant user material when present, or obtain explicit authorisation to exclude it.
4. Resolve every input through finite Human lineage.
5. Apply only the human-preserving operations and disclose each operation.
6. Verify every meaning-bearing word and relation in the complete output.
7. Present the inputs, operations and output together for explicit approval.
8. Save an approved output to its canonical owner with only the input record currently needed for verification or revision.

## Standard proposal

```markdown
## White-box-synthesis proposal — <output identity>

### Authorised inputs

- `U-012` — <exact span or stable reference>
- `F3` — <exact span or stable reference>

### Operations

1. COPY `U-012`: <span>
2. DELETE from `F3`: <material removed and why meaning is unchanged>
3. ORDER `U-012` before `F3`: <authorised relation>

### Proposed output `<exact output label>`

<Complete proposed output.>
```

The construction record is required in the approval proposal. In active project files, retain only the smallest input record needed to verify or revise current material; do not preserve completed operation logs by default.

## Gaps and AI proposals

If any word or relation in the proposed output cannot be reconstructed, stop and name the exact missing wording, evidence, relation or authorisation. Ask the user to supply it first. If the user requests AI help, present one exact bounded AI proposal, identify its AI authorship and obtain explicit approval. AI-authored material never becomes white-box synthesis or user material.

## Completion

Every meaning-bearing word and relation in the proposed output has finite Human lineage, relevant user material was included or explicitly excluded, and the exact output was approved.
