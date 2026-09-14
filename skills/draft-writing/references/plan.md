# Plan

## Accepts

User decisions about article movement, order, sections, passages, paragraph purposes, placement, connections, transitions, recurrence, inclusion, omission and condensation; current material IDs; and structural problems exposed during drafting.

Do not accept component claims as established merely by placing them, draft prose, parallel blueprints, architectural-decision logs or superseded plans.

## Owns

`{project}-plan.md` is the sole current authority for article structure. Material-file order has no structural authority.

## Standard structure

```markdown
# Plan

## Article movement

<Current movement through the inquiry.>

## Section 1 — <Working heading>

**Purpose:** <Its contribution to the user thesis and article movement.>

### Passage 1 — <Working label>

**Purpose:** <One current function.>

**Material:** ARG-001, ARG-004

**Movement:**

1. <Current step.>
2. <Current step.>

**Connection:** <Why the following unit follows, when needed.>

**Blocking question:** <Only when unresolved.>

## Unplaced material

- ARG-010 — <Current reason or question.>
```

Use only fields needed by each unit. Sections and passages may emerge, merge, divide, move or disappear as writing develops.

## Procedure

Develop consequential structural choices with the user. State alternatives when more than one real movement is possible and apply only the approved choice. Every placed unit needs a purpose that relates it to the user thesis or article movement, and every connection must come from authorised material or explicit approval.

When a decision changes, replace the affected live plan and review dependent prose. Do not retain the old plan, a decision ledger or immutable snapshots in active files; Git preserves them.

## Completion

The current plan is sufficient for the next drafting unit, its material and connections are explicit, and blocking structural questions are visible.
