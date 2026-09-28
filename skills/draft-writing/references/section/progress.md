---
name: progress.md
description: Keep one section's exact resume point, approval state, live blockers and local counters.
---

# Section Progress

`sections/section-n/progress-section-n.md` is that section's handoff. Read it before local work or ID allocation. It owns the current task, exact object, approval state, next action, unfinished verification, readiness and next local IDs. It does not duplicate the arc or approved prose.

```markdown
# Section 1 Progress

## Current
**Object:** [P-001](arc-section-1.md#p-001)
**Task:** <The unfinished action.>
**Approval:** pending
**Next:** <The first exact action to take.>

## Blockers
<Only live blockers and links to their owners.>

## Counters
- Next passage: P-002
- Next user input: U-001
- Next material: MAT-001
```

This is a shape example, not initial state. Set actual values; omit empty fields and unused namespaces. Approval state is `pending`, `approved but unsaved`, or `saved`. An approved save failure remains `approved but unsaved`, with its exact object and failure recorded, not reported as completion.

Retain an exact pending proposal only while needed to resume. Keep its input references so the full construction record can be rebuilt and re-presented; do not preserve a permanent operation log. If the proposal cannot be recovered, ask rather than reconstructing it from memory and treating it as approved. Remove pending text after rejection, replacement or successful save. A ready section may have a brief readiness record and counters without a fabricated next task.

## Local Identifiers

Use `P-001` for an arc passage, `U-001` for exact local user wording and `MAT-001` for material. Full identity is owner file plus label; `MAT-001` in two sections is not the same object. Use ID-only headings for stable anchors and put titles below them. Source maps own their own `EXCERPT` counters, not this file.

1. Reread this counter and its owner before allocating; check for concurrent changes.
2. Allocate the next unused value and advance the counter immediately, even for a proposal later rejected. Never reuse a removed, rejected or retired ID or fill a gap.
3. If uncertain, check Git; if still uncertain, ask. Do not lower counters during cleanup.
4. On an allocation collision, preserve both objects and resolve the collision before saving. Do not assume parallel allocation is safe without coordination.

## Handoff And Readiness

Update this file after decisions, saves, blockers and focus changes. Record unfinished citation or dependent-source reviews here with exact references, not repeated evidence. Article-level pending decisions belong beside their article owner; `plan.md` carries only the current-section navigation link.

A section is ready only when intended approved prose is inserted, its arc is checked, required smoothing and citations are complete, no blocker remains, and the user has approved the section. Record the current section approval here. Deferred review means review pending, not ready.

Before ending, check that another session can identify the current object, approval state, blockers and first action without chat history. Apply [retention](../rules/retention.md); omit completed activity narratives.
