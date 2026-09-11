# Provenance

## Purpose

Declare authorship, method and basis without confusing authorship with approval.

## Compact declaration

Use exactly:

```markdown
**Provenance:** Human · **Method:** white-box synthesis · **Basis:** A4, user-21
```

Allowed provenance values:

- `Human`: wording comes only from verified Human inputs.
- `Mixed`: retained wording contains Human and AI authorship.
- `AI`: wording is assistant-authored.
- `Unverified`: authorship or construction cannot be recovered.

Allowed methods: `white-box synthesis`, `verbatim user wording`, `verbatim source excerpt`, `AI drafting` or `unknown`.

White-box synthesis accepts Human inputs only and always returns Human output. `Mixed`, `AI` and `Unverified` material cannot be a white-box input.

## Recursive lineage

An approved Human white-box output may be a later input as `arg:ARG-001`. The full record must identify that intermediate output and every operation. Compact `Basis` lists the ultimate source and user codes actually retained, once each in first-use order. A missing intermediate record, unresolved input or infinite/circular dependency blocks synthesis.

## Reconstruction test

Every meaning-bearing output span must map through a finite recorded operation chain to exact Human source or user wording. No unrecorded word, substitution, inference, scope change or deleted qualification is allowed.

Keep distinct:

- authorship: who supplied wording;
- evidence: what a source establishes;
- interpretation: the user's claim;
- selection: what the user approved.

Approval changes none of these.

## Procedure

1. Map every output span to exact inputs and locations.
2. Record every operation in order.
3. Resolve recursive inputs to ultimate Human bases.
4. Check source scope, modality and qualifications.
5. Derive the compact declaration.

For retained historical prose with unresolved construction, use `**Provenance:** Unverified · **Method:** unknown · **Basis:** <known codes or Unverified>`.

## Completion

Every basis and intermediate input resolves; every output span passes reconstruction; evidence and interpretation remain distinct.

## Blocking

Missing Human provenance, lineage, location or operation blocks white-box synthesis.