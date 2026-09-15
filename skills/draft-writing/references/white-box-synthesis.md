---
name: white-box-synthesis.md
description: Defines reconstructable synthesis from authorised Human inputs.
---

# White-box synthesis

## Accepts

A finite set of exact, approved Human inputs identified directly by their stable labels, such as `U-012`, `F3` or `MAT-002`: user-material spans, source-map excerpts, or other approved outputs whose lineage resolves completely to Human user-material and source-map spans.

Relevant user material must be among the inputs when it exists. Excluding it requires explicit user authorisation. Source wording remains source-authored, and approval changes neither authorship nor evidentiary scope. AI-authored, Mixed and unverified material is permanently ineligible, including after approval.

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

Before presentation, compare every word and relation in the proposed output with its Human inputs. A white-box output must be wholly Human and use no AI marker. Any AI-authored word, including a connector, transition, join, framing phrase or conclusion, disqualifies the output from white-box synthesis.

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

<Complete Human-only proposed output.>
```

The construction record is required in the approval proposal. In active project files, retain only the smallest input record needed to verify or revise current material; do not preserve completed operation logs by default.

## Gaps

1. Stop at the smallest unreconstructable span or relation and classify the gap as missing wording, evidence, relation or authorisation.
2. Show the exact Human material available around the gap and explain why `COPY`, `INFLECT`, `NORMALISE`, `ORDER` and `DELETE` cannot fill it.
3. Ask the user to supply, clarify or resolve the missing content and work through that decision with them.
4. Do not originate or volunteer an AI-authored suggestion. State only that the user may explicitly request one as a separate option.
5. If the user explicitly requests an AI suggestion, handle it outside white-box synthesis. Mark it exactly, preserve AI provenance permanently, and never use it as synthesis material or a later white-box input.

Never use an AI suggestion to bypass a missing claim, interpretation, connection, qualification, evidence decision or authorisation. AI-authored material never becomes white-box synthesis, user material, source material or synthesis material, even after approval.

## Completion

Every meaning-bearing word and relation in the proposed output has finite Human lineage, relevant user material was included or explicitly excluded, and the exact output was approved.
