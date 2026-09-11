# Activity tracker

## Purpose

Preserve the exact workflow cursor, counters and files required to resume.

## Procedure

Update after every question, proposal, approval, gap, candidate, decision, save, invalidation, version and focus change. Verify every path and counter.

## Output

```markdown
# Activity tracker

- **Project:** Demo
- **Stage:** Schema | Predrafting | Blueprinting | Drafting | Citation
- **Focus object:** Argument ARG-014
- **Focus type:** Argument
- **Focus state:** Candidate awaiting decision
- **Candidate revision:** ARG-014-r1
- **Blocking question:** None
- **Now:** ARG-014-r1 has been presented with its complete record.
- **Next after approval:** Save ARG-014; select the next focus from dependencies, user priority or blueprint need.
- **Next after comments:** Route comments; prepare ARG-014-r2.
- **Next source code:** B
- **Next user number:** 23
- **Next argument ID:** ARG-023

| Tracked filename | Role/state |
|---|---|
| demo-predraft-schema.md | Approved unordered arguments; next ARG-023 |
| demo-predraft.md | Approved raw argument material |
| demo-predraft-working.md | Unapproved ARG-014-r1 and full record |
| demo-source-map-a-service-log.md | Source A; pages 1–12 checked; next A5 |
```

Keep these thirteen fields and the table in this order. Use `None` when no candidate or question exists. `Focus type` is `Argument`, `Blueprint`, `Section`, `Draft` or `Citation`.

List every file needed to resume, including originals and every retained provenance basis. A source-map row records coverage, limits and next excerpt ID.

Allocate source, user and argument IDs monotonically. Never reuse a retired ID. Schema and predraft file positions are not counters and have no article meaning.

On resumption, verify files and state. Re-present any exact pending proposal or candidate before interpreting a later response.

## Completion

The header identifies one current state and exact next actions; all required files and counters are present and correct.

## Blocking

A missing candidate, unresolved counter or file mismatch blocks continuation until recovered or resolved with the user.