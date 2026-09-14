---
name: material.md
description: Defines synthesized passages formed from one or more arguments.
---

# Material

## Accepts

One or more approved arguments, their authorized bases, relevant user material, and passage needs established by the thesis or plan.

Do not accept unapproved argument candidates, independent claims without argument IDs, article order as authority, reader-facing final prose, completed process history or superseded decisions.

## Owns

`{project}-material.md` owns synthesized passages from which the draft will be formed. Each passage is made from one or more arguments; argument definitions and bases remain in arguments.

## Standard structure

```markdown
---
name: "{project}-material.md"
description: Holds synthesized passages formed from one or more arguments.
---

# Material

## MAT-001 — <Passage label>

**Arguments:** ARG-001, ARG-004

### Passage

<Current synthesized passage.>

### Constraint

<Only when the passage has a live qualification, unresolved join or use limit.>

```

Each passage has a monotonic `MAT-nnn` ID and names every argument it uses. Its exact internal form remains flexible. File order does not establish article order.

## Procedure

1. Select one or more approved arguments needed for a bounded passage.
2. Resolve each argument through its recorded basis and include relevant user material unless the user explicitly authorises exclusion.
3. Identify the relation joining the arguments. If no authorised input establishes it, report a gap rather than inventing a transition or conclusion.
4. Develop the complete passage through white-box-synthesis and present it for explicit approval.
5. Save the approved passage with its argument IDs and only live constraints needed for revision or use.
6. Update affected plan and draft uses when a passage changes. Remove obsolete versions rather than retaining a revision history.
7. Never reuse a removed or retired material ID; allocate the next historical value from progress.

## Completion

The current passage names all constituent arguments, preserves their limits and authorized lineage, and adds no unsupported wording or relation.
