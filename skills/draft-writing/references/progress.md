---
name: progress.md
description: Defines the sole current resumption state and monotonic ID counters.
---

# Progress

## Accepts

Current workflow position, the presently achieved and reliable state, immediate next work, live blockers or contradictions, source-reading coverage and ID counters.

Do not accept a chronological activity log, superseded decisions, rejected proposals, full inventories, duplicate article material or session narrative.

## Owns

`{project}-progress.md` is the sole resumption file. It replaces separate handoff files and overlapping current-focus records.

## Standard structure

```markdown
---
name: "{project}-progress.md"
description: Holds current work, achieved state, next work, blockers and counters.
---

# Progress

## Current work

<Exact item, state and current task.>

## Completed state

- <Current achievement that later work may rely on.>

## Next

1. <Immediate next action.>
2. <Following action if already determined.>

## Blockers and contradictions

### C-001 — <Current blocker>

<Decision or material required.>

## Counters

- Next source code: B
- Next user-material ID: U-023
- Next argument ID: ARG-023
- Next material ID: MAT-014
- Next contradiction ID: C-004

## Source work in progress

### Source A

**Original:** sources/example.pdf

**Coverage:** Pages 1–12 checked.

**Next excerpt:** A5
```

Use only sections with current content. `Completed state` summarizes what is operative now; it does not narrate how it was reached.

Include only counters for namespaces the project uses. A counter records the next never-used value, not the lowest available gap. It advances beyond every ID allocated in current files or Git history and never decreases when an item is removed, retired, merged or replaced.

## Procedure

Update after a proposal, decision, gap, save, invalidation or focus change. Advance the relevant counter whenever an ID is allocated. Remove resolved blockers and obsolete next actions without reducing counters. Verify named files before resuming, and re-present an exact pending proposal before interpreting a later response as approval.

## Completion

Another session can identify what is happening, what is currently reliable and what comes next without consulting a historical log.
