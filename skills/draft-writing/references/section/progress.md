---
name: progress.md
description: Keep one section's exact resume point, approval state, live blockers and local counters.
---

# Section Progress

**Owner:** `sections/section-n/progress-section-n.md`.
**Allowed:** Current object and task, current action-specific approval/save state, exact next action, live blockers, unfinished verification targets, readiness, local counters and the bounded pending object below.
**Excluded:** Source inventories, source quotations, source qualifications and locator corrections (source maps); passage constraints and saved inputs (material); argument development and passage order (arc); construction logs, approval history, completed task narratives and descriptions of other files' contents.

Read progress before local work or ID allocation. A verification target identifies an action and object, not the source evidence or qualification itself.

```markdown
# Section 1 Progress

## Current
**Object:** [P-001](arc-section-1.md#p-001)
**Task:** <The unfinished action.>
**Approval:** pending
**Next:** <The first exact action to take.>

## Blockers
<A live impediment, its exact object and the action needed to resolve it.>

## Counters
- Next passage: P-002
- Next user input: U-001
- Next material: MAT-001
```

This is a shape example, not initial state. Set actual values; omit empty fields and unused namespaces. Approval state is `pending`, `approved but unsaved`, or `saved`. An approved save failure remains `approved but unsaved`, with its exact object and failure recorded, not reported as completion.

Retain only the exact pending object required for the next unresolved decision or approved-but-unsaved failure, when no proper owner already preserves it. Keep its input references so the construction record can be rebuilt and re-presented; do not keep alternatives or an operation log. If the object cannot be recovered, ask rather than reconstructing it from memory as approved. Remove pending text after rejection, replacement or successful save. A ready section needs no fabricated task.

## Local Identifiers

Use `P-001` for an arc passage, `U-001` for exact local user wording and `MAT-001` for material. Full identity is owner file plus label; `MAT-001` in two sections is not the same object. Use ID-only headings for stable anchors and put titles below them. Source maps own their own `EXCERPT` counters, not this file.

1. Reread this counter and its owner before allocating; check for concurrent changes.
2. Allocate the next unused value and advance the counter immediately, even for a proposal later rejected. Never reuse a removed, rejected or retired ID or fill a gap.
3. If uncertain, check Git; if still uncertain, ask. Do not lower counters during cleanup.
4. On an allocation collision, preserve both objects and resolve the collision before saving. Do not assume parallel allocation is safe without coordination.

## Handoff And Readiness

Update current state after decisions, saves, blockers and focus changes; replace stale state, do not append a history. For unfinished citation or source reviews, state the remaining action and exact target only. Put the source qualification or correction directly in its map. Article-level pending decisions remain beside their article owner; the plan carries only current-section navigation.

A section is ready only when intended approved prose is inserted, its arc is checked, required smoothing and citations are complete, no blocker remains, and the user has approved the section. Record the current section approval here. Deferred review means review pending, not ready.

Before ending, check that another session can identify the current object, approval state, blockers and first action without chat history. Apply [retention](../rules/retention.md); omit completed activity narratives.
