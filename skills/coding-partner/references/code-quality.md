# Code quality

## Readability

- Seek minimal sufficient code, not the shortest code or the fewest functions.
- Do not infer AI authorship from code patterns.
- Prefer direct control flow, clear data ownership, and self-documenting names.
  Use familiar short names where clear.
- Introduce a fragment or abstraction when it improves understanding, isolates
  a meaningful responsibility, keeps a mechanism manageable, or prevents
  consequential duplication. Avoid forwarding-only layers and helpers created
  merely to reduce line counts.

## Necessary complexity

- Justify material additions such as abstractions, safeguards, fallbacks,
  dependencies, and configuration options by the requirement or concrete
  failure they address. Preserve necessary safety checks and honest error
  reporting. Do not add generic defensive scaffolding or silently hide failure.

## Sufficiency and minimality

- A solution is sufficient when it meets the agreed behaviour and constraints,
  handles relevant failures, and has appropriate evidence of correctness.
- A solution is minimal when it introduces no unnecessary behaviours, concepts,
  dependencies, or indirection. More lines can be justified when they make the
  mechanism clearer.
