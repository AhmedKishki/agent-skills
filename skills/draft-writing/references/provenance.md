# Provenance

## Purpose

Define authorship declarations, basis records and the test for reconstructing selected wording.

## Inputs

The exact output wording, original human spans actually used, their locations, and the ordered white-box operations applied to them.

## Compact declaration

Use this field order:

```markdown
**Provenance:** Mixed · Human wording: 100% · Method: white-box synthesis · Basis: A4, user-21, user-22
```

- **Provenance:** `Human` for unchanged wording from one human original; `Mixed` for human wording arranged from multiple spans; `AI` for assistant-authored wording; `Unverified` when origin is unresolved.
- **Human wording:** `100%` only when every meaning-bearing span passes the reconstruction test; `0%` for wholly assistant-authored wording; `Unverified` when the check is incomplete.
- **Method:** use exactly `white-box synthesis`, `verbatim user wording`, `verbatim source excerpt`, `AI drafting` or `unknown`. Use `unknown` only for accepted retained prose whose actual construction method cannot be verified; never infer `white-box synthesis` from an incomplete historical record.
- **Basis:** for verified construction, list only source and user codes actually used, once each, in first-use order. For accepted unverified prose, list only stable source and user codes recovered, reconstructed or feasible as bases; this does not claim a verified execution history. Write source codes as `A4`, not `src:A4`. Use `Unverified` only when no stable basis code can be identified.

## Reconstruction test

Wording is reconstructable only when every meaning-bearing output span maps to quoted original spans and a finite ordered sequence of operations permitted by [white-box synthesis](white-box-synthesis.md), with no unrecorded substitution, insertion, inference or change of scope.

Preserve these distinctions:

- **Authorship:** who supplied the wording.
- **Evidence:** what a source establishes in context.
- **Interpretation:** the user's claim made with or about that evidence.
- **Selection:** the user's approval of the exact result.

## Procedure

1. Map every meaning-bearing output span to its exact original and location.
2. Record every operation in execution order.
3. Verify source scope, modality and qualifications separately from authorship.
4. Deduplicate basis codes in first-use order.
5. Derive the four compact fields from these checks; do not derive authorship or method from approval. For accepted retained prose that fails reconstruction, declare `Provenance: Unverified · Human wording: unverified · Method: unknown` and preserve the recovered, reconstructed or feasible stable basis codes.

## Output

The compact declaration and, when synthesis is presented, its complete construction record.

## Completion condition

Every basis resolves, every output span passes the reconstruction test, and evidence and interpretation remain distinct.

## Blocking condition

Return an `Unverified` declaration and block selection when an original, location, operation or authorship cannot be established.

## Next owner

Predraft saves an approved passage with its compact declaration; drafting records approved connectors in its process appendix.