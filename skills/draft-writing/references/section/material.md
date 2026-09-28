---
name: material.md
description: Keep one section's local author inputs, approved synthesis and permanently marked AI gap text.
---

# Section Material

`sections/section-n/material-section-n.md` owns exact local user inputs and approved passages for that section. Read its arc, requirements and progress before editing. Use [white-box synthesis](../tools/white-box-synthesis.md) for eligible wording and the separate [AI-authored procedure](../tools/ai-authored.md) for gap text.

```markdown
# Section 1 Material

## MAT-001
<Short descriptive title.>

### U-001
> <Exact local user wording, unchanged.>

### Passage
<Exactly approved synthesised text.>

**Basis:** [U-001](#u-001); [EXCERPT-001](../../sources/source-maps/author-title.md#excerpt-001).
**Provenance:** Human
**Constraint:** <Only a live limit or unresolved dependency.>
```

The example names are placeholders, not evidence. Use [local IDs](progress.md#local-identifiers). Keep the ID-only headings and valid relative references. `Basis` contains only input references, not operations or an approval history. `Provenance` is Human, Mixed or AI; it never substitutes for exact AI-span labels. Omit an absent constraint or unused field rather than filling it with boilerplate.

Preserve exact user spelling, punctuation and paragraph breaks separately from the transformed passage. Keep local inputs beside their destination, not in a separate user-wording section or file. An input awaiting synthesis can sit under its local arc passage ID without inventing an approved `MAT` passage. When it moves beside approved material, retain its `U` ID and repair affected local references.

Only approved output belongs in the passage block. Pending proposals belong in progress while needed for review. The arc owns purpose and order; do not copy its outline here. Do not create a global material pool, an intermediate argument record or another section's inputs by reference or copying.

Approved AI gap text may be stored here with its exact `⟦AI-AUTHORED: ...⟧` markers and limits. Human plus explicitly AI text is Mixed; wholly AI text is AI. Basis references can identify supporting evidence without claiming that it supplied the AI wording. For an AI-only gap with no eligible wording basis, omit Basis rather than inventing an input. Mark any relation that depends on an AI span in the live constraint so it cannot be mistaken for an eligible source relation.

White-box excludes every explicitly AI-authored span and dependent relation, even after approval or copying. Ordinary approved Mixed inputs remain eligible when their lineage is finite and recoverable; outputs using them remain Mixed. Do not turn the material file's permission to store AI text into permission to synthesise from it.

After saving, verify exact approval, wording, authorship, resolvable basis, markers and live limits. Update local progress. Material approval does not authorise draft insertion; propose insertion separately. Keep construction records in the approval proposal, never in this file.
