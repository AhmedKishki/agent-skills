# Article arc

Build the structural map in `{project}-article-arc.md`: sections contain paragraph claims; paragraphs contain supporting arguments.

Each section's claim depends on its paragraph claims; each paragraph's claim depends on its arguments. A section may be named by the governing question its paragraphs answer. Use concise claims for paragraph and argument names. Section labels guide composition; final article headings are selected separately.

## Collaboration

1. Read the accepted thesis and the user's current structure.
2. Propose section, paragraph and argument claims. Check what each child contributes to establishing its parent's claim or answering its question.
3. Ask for approval or comments; save accepted changes.
4. Resolve structural gaps with the user in conversation. Keep the pending decision in the tracker.

The prose supplies explanations, evidence and connections. [Predraft](predraft.md) selects and records the relevant sources and user wording for each argument.

## Output

```markdown
# Article arc

Status: Working
Thesis: [General picture](demo-thesis-and-vision.md#general-picture)

Arc: 1 → 2

## 1 — Why does apparent automation depend on human work?

### 1.1 — Human review sustains the service

1.1.1 — Flagged results require human checks

1.1.2 — Recurring checks enable continued operation

## 2 — Recurring review requires staffing

### 2.1 — Schedules must provide review time

2.1.1 — Daily checks require working time

2.1.2 — Staffing must make that time available
```

Use exactly this structure: Status, Thesis and one article Arc line, then H2 sections, H3 paragraphs and plain argument lines separated by blank lines. The Arc line lists section numbers once in reading order. Nesting records the dependence of parent claims on their children.

Number sections `1`, paragraphs `1.1` and arguments `1.1.1`, restarting each local sequence at 1. Predraft owns source/user fragment selection and the saved provenance trail.
