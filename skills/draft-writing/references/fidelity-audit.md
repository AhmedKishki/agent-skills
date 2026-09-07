# Fidelity audit

## Purpose

Report fidelity defects in a declared article scope without applying corrections.

## Inputs

The declared scope, thesis, arc, predraft, draft when present, user wording, source maps, tracker and available originals.

## Procedure

1. State the checked scope, files and access limits.
2. Check thesis-to-section, section-to-passage, passage-to-argument and argument-to-approved-fragment correspondence.
3. Check every provenance line against exact originals and the [reconstruction test](provenance.md#reconstruction-test).
4. Verify that every in-scope arc passage occurs once in predraft, in arc order, with exactly one provenance line immediately after it; verify that no separate provenance part exists.
5. Verify that predraft contains no unapproved connector whose sole function is to join passages or sections.
6. Verify that every source map has only `Code | Excerpt | Location`, and that no source-index dependency remains.
7. When a draft exists, verify complete passage coverage, approved connectors, passage-to-paragraph mappings, source meaning, qualifications and citation scope.
8. Check user edits, numbering, selection authority and invalidation state.
9. Report each issue with its exact location, consequence, correction and authoritative owner. Do not apply it.

## Output

Respond with:

- **Checked:** scope and access limits.
- **Result:** checks passed for this scope, or issues remain.
- **Findings:** location, problem and consequence, proposed correction and owner; include when issues exist.

Create `# Fidelity audit` with these fields only when a file is requested. Treat a saved trail as a basis for verification without asserting an unrecorded historical sequence.

## Completion condition

Every applicable check has a pass or a precise finding, and no correction has been applied.

## Blocking condition

Missing originals or files limit only the checks that depend on them; report each access limit rather than inferring a result.

## Next owner

The user decides whether to authorize each proposed correction in its authoritative module.
