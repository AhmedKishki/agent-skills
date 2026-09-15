---
name: material.md
description: Defines synthesized passages formed from one or more arguments.
---

# Material

## Accepts

One or more approved Human-only arguments, their authorized Human bases, relevant user material, and passage needs established by the thesis or plan.

Do not accept unapproved argument candidates, AI-authored, Mixed or unverified inputs, independent claims without argument IDs, article order as authority, reader-facing final prose, completed process history or superseded decisions. Approval does not make AI or Mixed material eligible.

## Owns

`{project}-material.md` owns Human-only synthesized passages from which the draft will be formed. Each passage is made from one or more Human-only arguments; argument definitions and bases remain in arguments.

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
2. Resolve each argument through its recorded basis and verify that every input has complete Human lineage. Include relevant user material unless the user explicitly authorises exclusion.
3. Identify the relation joining the arguments. If no authorised input establishes it, report a gap rather than inventing a transition or conclusion.
4. Develop the complete Human-only passage through white-box synthesis and present it for explicit approval.
5. After approval, use the separate smoothing procedure. Human-only smoothing may revise material; user-requested AI smoothing belongs only in the draft and never returns to material.
6. Save the approved passage with its argument IDs and only live constraints needed for revision or use.
7. Update affected plan and draft uses when a passage changes. Remove obsolete versions rather than retaining a revision history.
8. Never reuse a removed or retired material ID; allocate the next historical value from progress.

## Completion

The current passage names all constituent arguments, preserves their limits and complete Human lineage, and contains no AI-authored, Mixed, unverified or unsupported wording or relation.
