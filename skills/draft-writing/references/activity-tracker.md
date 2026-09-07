# Activity tracker

## Purpose

Persist the exact workflow cursor, allocation counters and file inventory required to resume.

## Inputs

The current workflow event and the actual project files after that event.

## Procedure

Update the tracker after every input proposal, input approval, gap, candidate presentation, user decision, approved save, invalidation, connector presentation and focus change. Verify listed paths and counters against actual files before saving.

## Output

```markdown
# Activity tracker

- **Project:** Demo
- **Stage:** Predrafting
- **Focus passage:** 1.1
- **Focus connector:** None
- **Focus state:** Candidate awaiting decision
- **Candidate revision:** 1.1-r1
- **Blocking question:** None
- **Now:** Passage 1.1 revision 1 has been presented with its full construction record.
- **Next after approval:** Save passage 1.1 with inline provenance, then open passage 1.2.
- **Next after comments:** Route comments and prepare passage 1.1-r2.
- **Next source code:** B
- **Next user number:** 23

| Tracked filename | Role/state |
|---|---|
| demo-user-wording.md | Original user language |
| demo-article-arc.md | Accepted argument plan |
| demo-predraft.md | Approved raw passages through 1.0 |
| demo-predraft-working.md | Unapproved passage 1.1-r1 and full record |
| demo-source-map-a-service-log.md | Source A; pages 1–12 checked; next item A5 |
| original-file.pdf | Source original |
```

Keep all twelve header fields and the table in this order. During drafting, set `Focus passage: None`, use `Focus connector: C01`, and use connector revision IDs such as `C01-r1`.

List existing files needed to resume, using paths relative to the tracker. Include required originals, conversions and every retained wording basis named in saved provenance. The inventory consists of working inputs and outputs.

Each map row owns checked coverage, access limits and next excerpt ID. Record an unavailable original in that map row, and in Now/Next when it blocks current work.

Advance source codes, user numbers and excerpt IDs on allocation. Recover their highest allocated values from reliable history before replacing a missing counter; retired IDs remain retired. Arc numbers follow current positions.

On resumption, check inventory paths and pending work against actual files. Re-present the exact working candidate before interpreting a later approval.

## Completion condition

The fields identify one current state, one candidate revision or `None`, one blocking question or `None`, and exact next actions for approval and comments; every required file is listed.

## Blocking condition

A missing working candidate, unresolved counter or mismatch between tracker and files blocks continuation until recovered from reliable history or resolved with the user.

## Next owner

The module named by `Stage` and the current state.
