# Provenance

## Purpose

Define minimal authorship, method and basis declarations and the test for reconstructing selected wording.

## Inputs

The exact output wording, original human spans actually used, their locations, and the ordered white-box operations applied to them.

## Compact declaration

Use this field order:

```markdown
**Provenance:** Mixed · **Method:** white-box synthesis · **Basis:** A4, user-21, user-22
```

- **Provenance:** `Human` for unchanged wording from one human original; `Mixed` for wording arranged from multiple human originals; `AI` for assistant-authored wording; `Unverified` when authorship is unresolved.
- **Method:** use exactly `white-box synthesis`, `verbatim user wording`, `verbatim source excerpt`, `AI drafting` or `unknown`. Use `unknown` only for accepted retained prose whose actual construction method cannot be verified; never infer `white-box synthesis` from an incomplete historical record.
- **Basis:** list source and user codes actually used, once each, in first-use order. For accepted unverified prose, list only stable codes recovered, reconstructed or feasible as bases; this does not claim a verified execution history. Write source codes as `A4`, not `src:A4`. Write `Unverified` only when no stable basis code can be identified.

Do not declare a human-wording percentage. The reconstruction test verifies wording directly; it is not a percentage calculation.

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
5. Derive the three compact fields from these checks; do not derive authorship or method from approval. For accepted retained prose whose authorship or method cannot be verified, declare `**Provenance:** Unverified · **Method:** unknown · **Basis:** <codes or Unverified>`.

## Output

The compact declaration and, when synthesis is presented, its complete construction record.

## Completion condition

Every basis resolves, every output span passes the reconstruction test, and evidence and interpretation remain distinct.

## Blocking condition

Return an `Unverified` declaration and block selection when an original, location, operation or authorship cannot be established.

## Next owner

Predraft saves an approved passage with its compact declaration; drafting records approved connectors in its process appendix.