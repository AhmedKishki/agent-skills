# Article arc

Build the user's editable argument map in `{project}-article-arc.md`.

## Collaboration

1. Read accepted thesis and structural decisions.
2. Propose the next unresolved level: section progression, paragraph claims, or sentence arguments. Show each arrow's intended causal or explanatory relationship.
3. Ask for approval or comments on the exact proposal. Apply accepted changes.
4. Ask a focused question for any missing claim or relationship; keep it as `Open:` at that location.

Each paragraph makes one claim. Its sentence chain provides the argument for that claim. Use short planning propositions throughout; actual article prose and fragment-use codes belong in predraft.

## Output

```markdown
# Article arc

Status: Working
Thesis: [General picture](demo-thesis-and-vision.md#general-picture)
Arc: 1 — Recurring work → 2 — Conditions of that work

## 1 — Recurring work

Question: What sustains the apparent automation?
Arc: 1.1 — Review sustains service

### 1.1 — Review sustains service

Function: Establish the continuing work before examining its conditions.
Arc: 1.1.1 — Daily checking → 1.1.2 — Service continuity
Connection: 1.1.1 → 1.1.2 — recurring checks explain continued operation.

#### 1.1.1 — Daily checking

#### 1.1.2 — Service continuity

## 2 — Conditions of that work

Question: Under what conditions is that work performed?
Arc: Open
Open: What claim should this section establish?
```

Keep this field order: article Status / Thesis / Arc; section Question / Arc; paragraph Function / Arc; sentence heading. Optional `Connection:` explains an unclear arrow, `Boundary:` explains a necessary paragraph boundary, and `Open:` asks a concrete question. Put optional fields after required fields, before children.

## Numbering and arrows

- Sections: `1`, `2`; paragraphs: `1.1`, `1.2`; sentences: `1.1.1`, `1.1.2`.
- Number each level from 1 in reading order.
- Each Arc line repeats its direct children's exact numbers and short labels, once each, joined by ` → `.
- A single child stands alone. An unresolved chain uses `Arc: Open` and its question.
- Keep fragment identities in predraft's Used lists.

Check that each arrow expresses the accepted relationship and each chain matches its child blocks.

## Edits

After an accepted move, split or insertion, map old content to new positions and update affected arc chains, predraft headings, sentence references and draft links together. Carry wording and selection authority with their content. Ask about ambiguous correspondence.

Synchronise a clear direct user edit between chain and child blocks. Markdown anchors remove dots: `1.1 — Record` links as `#11--record`.
