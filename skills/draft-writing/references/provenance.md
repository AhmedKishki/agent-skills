# Provenance

## Purpose

Preserve authorship and evidence lineage without burdening the user with process metadata.

## Principles

- Keep authorship, evidence, interpretation and approval distinct.
- Source wording remains source-authored.
- User material remains user-authored.
- Approval changes neither authorship nor evidentiary scope.
- Argument synthesis using only verified Human inputs produces Human prose when every output span is reconstructable.
- Mixed, AI or unverified material cannot enter Human-only synthesis.

## Display

Use the smallest basis record sufficient to recover the argument draft:

```markdown
### Basis

- U-003
- A4
- ARG-002
```

Keep detailed construction steps in synthesis material only while they are needed for approval or later reconstruction. Do not repeat them in thesis, article arc or draft.

For historical prose whose construction cannot be recovered, state:

```markdown
### Basis

- Unverified
```

## Recursive use

An approved Human argument draft may be used in another argument only after the user approves the exact span. Resolve it through a finite chain to its source and user-material bases.

## Reconstruction

Every meaning-bearing synthesized span must map through recorded operations to approved Human wording. Missing lineage, source location or operation blocks Human-only synthesis.

## Completion

The basis is recoverable, authorship is accurate and project-facing files contain no unnecessary provenance commentary.