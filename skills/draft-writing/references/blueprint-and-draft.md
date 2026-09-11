# Blueprint and draft

## Purpose

Collaboratively form the article from approved raw arguments, then draft it section by section. The user decides every substantive choice.

## Inputs

Current thesis-and-vision, user wording, predraft schema, predraft, required source maps, authorial voice and tracker.

Predraft-schema and predraft have no article order. Blueprint is the sole authority for passages, paragraphs, sections and order.

## Blueprint

Use `{project}-blueprint-working.md`.

1. List every article-level, passage-level, section-level and raw-material decision required to draft without guessing.
2. Ask one focused question at a time. Quote or link exact material. State the consequences of real alternatives. The user may reject every alternative.
3. Record only approved decisions.
4. Give every active `ARG-nnn` or migration `RAW-nnn` one explicit treatment: include, combine, divide, condense, recur, reserve or omit.
5. For every use, identify its destination, exact span, function, qualifications and relation to surrounding material.
6. Define the proposition, passages, paragraph boundaries, sections, headings, order, connectors, protected wording and drafting order.
7. Present the complete `WB-rN`. Ask: **“Do you approve blueprint revision WB-rN as blueprint vN, or what should change?”**
8. After approval, copy it unchanged to `{project}-blueprint-vN.md` with `Status: Approved`.

```markdown
# Blueprint working

Status: Working | Awaiting approval | Blocked
Revision: WB-rN
Current approved version: None | blueprint-vN.md
Basis: <links>

## Article proposition
<Approved decisions>

## Draft structure
### 1 — <working heading>
- **Function:** <one contribution>
- **Passages:** <BP-P01...>
- **Paragraph plan:** <exact plan>
- **Opening and close:** <approved movement>
- **Connection:** <approved relation>
- **Protected:** <wording and qualifications>
- **Open:** <question or None>

## Raw-material treatment
| Raw argument | Destination/use | Treatment | Function | Status |
|---|---|---|---|---|

## Required relations
| From | To | Relation | Basis | Wording status |
|---|---|---|---|---|

## Open questions
<Questions or None>
```

Working states are `Working`, `Awaiting approval` and `Blocked`. Approved blueprint versions are immutable.

## Draft

Create `{project}-draft-working.md` only when the first section candidate exists.

1. Work in approved blueprint order, one complete section at a time.
2. Present the section requirements, selected raw material, relations and unresolved needs. Ask until no substantive guess remains.
3. Ask the user to supply missing wording before offering AI wording. Use AI wording only after approval of its exact bounded span.
4. Save the current candidate and all previously approved sections in draft-working.
5. Present the complete section as `S<section>-rN` with blueprint version, bases, realised requirements, approved AI wording and validation result.
6. Ask: **“Do you approve section candidate S<section>-rN, reject it, or what should change?”** Wait.
7. After every section is approved, assemble them without adding prose. Present the complete draft for approval.
8. After approval, copy it unchanged to `{project}-draft-vN.md` with `Status: Finalised`. Delete draft-working only when no current drafting state remains.

Draft-working contains reader-facing prose first, then a process appendix:

```markdown
---

# Process appendix — outside the article

Status: Working | Assembling | Awaiting approval | Blocked
Revision: WD-rN
Blueprint: blueprint-vN.md
Current section: <number | None>
Current candidate: <S<section>-rN | None>

| Draft section | Blueprint section | Raw material | Approved AI wording |
|---|---|---|---|
```

Section states are `Unstarted`, `Questions open`, `Candidate awaiting decision`, `Revision requested`, `Rejected`, `Approved and saved` and `Invalidated`.

## Validation

Verify explicit treatment of every active raw unit; approved selection, omission, recurrence, boundaries, order and relations; exact conformance to blueprint; approval of every section and AI-authored span; no prose added during assembly; preserved voice and qualifications; resolved mappings.

## Blocking

Any missing decision, relation, wording basis, approval or required raw material blocks affected work. Ambiguity never grants discretion.