# Editing and reference integrity

## Purpose

Apply an approved edit without losing user wording, provenance, IDs, links or downstream review state.

## Inputs

The exact approved change and every file directly or transitively affected by it.

## Procedure

1. Read every affected current file and preserve the immediate pre-edit state in a temporary snapshot.
2. Preserve direct user edits and apply only the approved substantive change plus its necessary mechanical consequences.
3. Route newly identified content through [ownership and routing](ownership-and-routing.md).
4. After an approved move, insertion, removal, split or merge, update positional passage and argument numbers and every dependent reference in the same change.
5. Preserve stable source and user IDs. Retire an allocated ID instead of reusing it.
6. For an approved contradictory replacement, preserve the earlier text and place the approved `Outdated` marker immediately beside the exact superseded aspect before applying the new operative commitment.
7. Identify every approved downstream passage affected by a changed thesis constraint, arc claim, argument, governing qualification, source basis or user original; mark each one `Invalidated`.
8. Validate operational and outdated status, exact wording, source context, argument coverage, basis codes, claim dependencies, numbering, links and states.
9. Update the tracker with the completed edit and exact next action.

Changing a broad arc inventory alone does not select an input, trigger synthesis or invalidate prose. Adding or reordering an unused candidate fragment has no effect on approved prose. Removing an actual approved basis, changing its original, or changing a qualification that governs approved prose requires impact review and invalidation of every affected passage. Do not invalidate a passage for a qualification change that leaves its governing directions, limitations, boundaries and specifications unchanged.

During an authorized migration, preserve stable IDs and originals required by current provenance, follow the user's retention scope, and apply the current schemas only within the approved migration scope.

## Output

The approved edit, repaired dependent references and explicit invalidation of affected downstream passages.

## Completion condition

The diff contains no unapproved substantive change, every superseded aspect is preserved and marked `Outdated` beside its operative replacement, all references resolve and every affected downstream passage has the correct state.

## Blocking condition

Stop before editing when intent, origin, correspondence, migration scope or the operative status of contradictory direction is ambiguous.

## Next owner

Return changed content to its authoritative module and invalidated passages to predraft.