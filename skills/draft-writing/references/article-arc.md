# Article arc

## Purpose

Define the article's ordered claim structure as sections containing passages and passages containing supporting arguments.

## Inputs

The approved thesis and vision, the user's current structural instructions, and any existing arc.

## Structure

The hierarchy is `article → section → passage → argument`.

- A section establishes one section claim or answers one governing question.
- A passage performs exactly one claim. It is independent of final paragraph boundaries.
- An argument performs one supporting step required to establish its parent passage claim.
- Every in-scope passage belongs to exactly one section and contains at least one argument.
- Every argument belongs to exactly one passage.
- The arc records no exact source excerpt or user-wording selection.

## Procedure

1. Read the approved direction and preserve the user's accepted structure.
2. Propose section claims or questions in reading order and obtain approval of the exact proposal.
3. For each approved section, propose its ordered single-claim passages and obtain approval.
4. For each passage, propose the ordered arguments and state how each argument establishes the passage claim; obtain approval.
5. Save only approved structure. Record one focused structural question in the tracker when a claim, dependency, order or boundary is unresolved.
6. After an approved structural change, apply [editing and reference integrity](editing-and-reference-integrity.md) and invalidate affected selected passages.

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

Use exactly this structure: Status, Thesis and one Arc line, then H2 sections, H3 passages and plain argument lines separated by blank lines. The Arc line lists section numbers once in reading order. Number sections `1`, passages `1.1` and arguments `1.1.1`, restarting each local sequence at 1.

## Completion condition

Every in-scope section has an approved claim or question; every passage performs one approved claim; every passage has at least one approved ordered argument; and no structural question blocks the first unapproved passage.

## Blocking condition

An unresolved section purpose, passage claim, argument contribution, order or boundary blocks only dependent structure and predrafting.

## Next owner

[Predraft](predraft.md) selects passage inputs and develops every in-scope passage in arc order.
