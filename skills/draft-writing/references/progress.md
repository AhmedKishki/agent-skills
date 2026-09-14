---
name: progress.md
description: Defines the necessary-and-sufficient next-session handoff and monotonic ID counters.
---

# Progress

## Accepts

Current workflow position, the presently achieved and reliable state, operative user decisions, live evidence and provenance limits, pending approval state, immediate next work, live blockers or contradictions, files needed to resume, source-reading coverage and ID counters.

Do not accept a chronological activity log, superseded decisions, rejected proposals, full inventories, duplicate article material or session narrative.

## Owns

`{project}-progress.md` is the sole resumption file and the handoff to the next session. It must contain all and only the information necessary and sufficient to continue safely without relying on chat history. It replaces separate handoff files and overlapping current-focus records.

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

## Live decisions and limits

- <Operative decision, evidence limit, provenance rule or pending-approval state needed for the next work.>

## Blockers and contradictions

### C-001 — <Current blocker>

<Decision or material required.>

## Counters

- Next source code: B
- Next user-material ID: U-023
- Next argument ID: ARG-023
- Next material ID: MAT-014
- Next contradiction ID: C-004

## Resume from

- `{project}-plan.md` — <exact live unit needed next>.
- `{project}-arguments.md` — <active arguments or ranges>.
- `<other file>` — <specific material, source map or section needed>.

## Source work in progress

### Source A

**Original:** sources/example.pdf

**Coverage:** Pages 1–12 checked.

**Next excerpt:** A5
```

Use only sections with current content. `Completed state` summarizes what is operative now; it does not narrate how it was reached. `Live decisions and limits` records only constraints that the next work must apply. `Resume from` names the minimum files and exact units needed to continue; it is not a full project inventory.

Include only counters for namespaces the project uses. A counter records the next never-used value, not the lowest available gap. It advances beyond every ID allocated in current files or Git history and never decreases when an item is removed, retired, merged or replaced.

## Procedure

Update after a proposal, decision, gap, save, invalidation or focus change and at every session handoff. Advance the relevant counter whenever an ID is allocated. Remove resolved blockers, obsolete next actions and replaceable history without reducing counters. State whether an exact proposal is pending approval, approved but unsaved, rejected or superseded whenever ambiguity could cause an unauthorized save. Verify named files before resuming, and re-present an exact pending proposal before interpreting a later response as approval.

Before ending a session, test the handoff from the perspective of a new session: it must identify the exact current object and state, what is reliable, every live decision and limit needed for that object, unresolved blockers, the minimum files and units to read, counters, and the first action to take. Add missing information; remove narrative that does not change resumption.

## Completion

Another session can continue the process safely and correctly from this file and the files it names, without chat history, a separate handoff or a historical log.
