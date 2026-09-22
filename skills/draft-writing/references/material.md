---
name: material.md
description: Defines synthesized passages formed from one or more arguments.
---

# Material

## Accepts

One or more approved eligible arguments, their authorized Human or Mixed bases, relevant user material, and passage needs established by the thesis or plan.

Do not accept unapproved argument candidates, explicitly AI-authored or AI-marked spans, unverified inputs, independent claims without argument IDs, article order as authority, reader-facing final prose, completed process history or superseded decisions. Ordinary approval makes Mixed inputs eligible unless the user excludes them, while their provenance remains Mixed.

## Owns

`{project}-material.md` owns synthesized passages from which the draft will be formed. Material may be distributed into section working sets: the authoritative file keeps every passage’s text and whatever has no section yet, while `material-section-n.md` holds the material a section draws on, with a passage that serves more than one section copied into each of them. A change lands in the authoritative file first and is recopied into the affected section files. Each passage is made from one or more eligible arguments; argument definitions and bases remain in arguments, and Human or Mixed provenance remains recoverable.

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

An entry keeps only its arguments line, its passage, the one-line provenance naming its inputs, and a constraint where a live limit stands. Construction and operation records belong in the approval proposal rather than in the file.

Each passage has a monotonic `MAT-nnn` ID and names every argument it uses. Its exact internal form remains flexible. File order does not establish article order.

## Procedure

1. Select one or more approved arguments needed for a bounded passage.
2. Resolve each argument through its recorded basis and verify that every input has finite Human or Mixed lineage and contains no explicitly AI-authored or AI-marked span. Include relevant user material unless the user explicitly authorises exclusion.
3. Identify the relation joining the arguments. If no authorised input establishes it, report a gap rather than inventing a transition or conclusion.
4. Develop the complete passage through white-box synthesis, classify it as Mixed if it uses any Mixed input, state its provenance accurately, and present it for explicit approval.
5. After approval, use the separate smoothing procedure. Provenance-preserving smoothing may revise material; user-requested AI smoothing belongs only in the draft and its explicitly AI-authored spans never return to material.
6. Save the approved passage with its argument IDs and only live constraints needed for revision or use.
7. Update affected plan and draft uses when a passage changes. Remove obsolete versions rather than retaining a revision history.
8. Never reuse a removed or retired material ID; allocate the next historical value from progress.

## Completion

The current passage names all constituent arguments, preserves their limits and finite Human or Mixed lineage, states provenance accurately, and contains no explicitly AI-authored, AI-marked, unverified or unsupported wording or relation.
