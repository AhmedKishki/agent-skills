---
name: user-material.md
description: Preserves exact reusable user-authored wording.
---

# User material

## Accepts

Exact user-authored definitions, claims, interpretations, connections, qualifications, analogies, examples and candidate article wording that may orient or enter the article.

Do not accept procedural commands, approvals, source quotations, AI proposals or workflow commentary. A quotation remains source-authored even when the user supplies it.

## Owns

`{project}-user-material.md` owns exact reusable user wording so the user's thought, voice, style and tone are not distilled through synthesis.

## Procedure

1. Separate reusable wording from procedure and source-authored text.
2. Allocate a stable `U-nnn` ID from progress when identity is needed.
3. Preserve exact spelling, punctuation and paragraph breaks in a blockquote.
4. Link the ID from its current use rather than duplicating its wording.
5. When relevant user material exists for synthesis, include it. Excluding it requires explicit user authorisation.
6. If the user changes an entry that current work uses, keep the ID when its meaning remains; otherwise allocate a new ID, update current uses and rely on Git for the earlier text.
7. Never reuse a removed or retired user-material ID; allocate the next historical value from progress.

## Standard structure

```markdown
---
name: "{project}-user-material.md"
description: Preserves exact reusable user-authored wording.
---

# User material

## U-001 — Short description

> Exact user wording.
>
> Its next paragraph.
```

The description may state a present role when needed, but no routing or status field is required. Entries may be regrouped as the work develops while stable IDs remain intact.

## Completion

Every eligible contribution is preserved exactly once and remains available to current synthesis without source or AI wording being misattributed to the user.
