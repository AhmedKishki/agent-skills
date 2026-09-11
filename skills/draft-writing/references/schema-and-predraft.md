# Schema and predraft

## Purpose

Define unordered arguments and develop approved Human raw material. Do not form article passages or order.

## Inputs

Approved thesis-and-vision, user wording, source maps, tracker, predraft schema, predraft and any predraft-working candidate.

## Predraft schema

Use `{project}-predraft-schema.md`:

```markdown
# Predraft schema

Status: Working | Needs review | Approved
Thesis: <relative link>
Next argument ID: ARG-003

## ARG-001 — Human review sustains the service

> Optional qualification, dependency, limit or specification.

- user-21, src:A1, src:B3, arg:ARG-002
```

The heading states the argument claim. Its final bullet is the broad candidate-input inventory. Use Human `user-n`, `src:A1` and approved Human `arg:ARG-001` codes, or `- None identified`. File order and adjacency have no meaning. Record dependencies explicitly. Inventory membership neither approves use nor establishes provenance.

For each new or revised argument, present its exact ID, claim, qualification, dependencies and inventory. Ask: **“Do you approve this schema argument, or what should change?”** Save only after explicit approval.

## Predraft procedure

1. Select one approved argument by user priority, dependency or blueprint need.
2. Present a limited Human input set. For each input, quote the exact span and state its code, location, Human provenance, intended use, support and limits.
3. Ask: **“Do you approve this input set for {ARG-ID}, or what should change?”** Wait.
4. After approval, run [white-box synthesis](white-box-synthesis.md) for that argument only.
5. Save the unapproved result and full record in `{project}-predraft-working.md`.
6. Present the complete candidate and record. Ask: **“Do you approve {ARG-ID} revision {revision}, reject it, or what should change?”** Wait.
7. After approval, copy the exact raw material and compact provenance to `{project}-predraft.md`, then delete the working file.

## Predraft output

```markdown
# Predraft

## ARG-001 — Human review sustains the service

Reviewers check flagged results every day.

**Provenance:** Human · **Method:** white-box synthesis · **Basis:** A1, user-21
```

Predraft is unordered raw argument material. It contains no article passages, headings, connectors, section transitions or final paragraph boundaries.

## States and blocking

Use `Unstarted`, `Inputs awaiting approval`, `Blocked by gap`, `Candidate awaiting decision`, `Revision requested`, `Rejected`, `Approved and saved` or `Invalidated`.

A pending argument blocks itself, explicit dependants and blueprint decisions that require it. It does not block unrelated arguments. A non-Human input, missing approval, unresolved dependency or synthesis gap blocks the affected argument.

## Migration exception

During an approved legacy migration, preserve unsplittable approved prose as `RAW-nnn` with exact provenance and covered `ARG-nnn` IDs. This records old approval; it does not approve new argument boundaries. Split it later only through this module.

## Completion

The schema is complete when every active argument has an approved claim, qualification, dependencies and valid broad inventory. Predraft is sufficient for blueprint finalisation when every included blueprint use resolves to approved raw material. Blueprint discussion may begin earlier when available material is sufficient for its current question.

## Next owner

[Blueprint and draft](blueprint-and-draft.md) forms passages and all reader-facing structure.