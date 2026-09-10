# Article arc

## Purpose

Define the article's ordered claim structure as sections containing passages and passages containing supporting arguments, with optional qualifications and broad fragment inventories.

## Inputs

The approved thesis and vision, the user's current structural instructions, and any existing arc.

## Structure

The hierarchy is `article → section → passage → argument`. Qualifications and fragment inventories annotate that hierarchy; they do not add claim levels.

- A section establishes one section claim or answers one governing question.
- A passage performs exactly one claim. It is independent of final paragraph boundaries.
- An argument performs one supporting step required to establish its parent passage claim.
- Every in-scope passage belongs to exactly one section and contains at least one argument.
- Every argument belongs to exactly one passage.
- A section, passage or argument may have an unlabelled `>` blockquote immediately below it. It may state a question, comment, direction, limit, boundary, specification or other qualification governing that object; it is not article prose or a synthesis input.
- Every argument ends with exactly one unlabelled bullet containing all known fragments that could help develop it. Use comma-separated stable `user-n` or `src:A4` codes, deduplicated in first-listed order, or `- None identified` when none is known.
- The fragment bullet is the argument's final element: it follows any argument comments and precedes the next argument, passage, section or end of file.
- An inventory is broad and user-revisable. Listing a fragment does not select it for prose, approve it for synthesis, establish its evidential scope or put it in provenance.
- The arc records fragment references, not exact source excerpts, user-wording spans or approved synthesis selections.

## Procedure

1. Read the approved direction and preserve the user's accepted structure.
2. Propose section claims or questions in reading order and obtain approval of the exact proposal.
3. For each approved section, propose its ordered single-claim passages and obtain approval.
4. For each passage, propose the ordered arguments, state how each argument establishes the passage claim, and propose one broad fragment inventory for each argument; obtain approval.
5. Add or revise a section, passage or argument qualification only under the user's direction. Put its content directly in an unlabelled `>` blockquote under its owner; do not add a header or treat it as article language.
6. Revise an inventory when the user adds, removes or reorders a potential fragment. The revision alone neither approves an input set nor triggers synthesis.
7. Save only approved structure, comments and inventories. Record one focused structural question in the tracker when a claim, dependency, order or boundary is unresolved.
8. After an approved change, apply [editing and reference integrity](editing-and-reference-integrity.md) and invalidate only affected selected passages.

## Output

```markdown
# Article arc

## 1 — Why does apparent automation depend on human work?

> Establish the section's material scope before addressing its ideological appearance.

### 1.1 — Human review sustains the service

> Limit this passage to recurring review work.

1.1.1 — Flagged results require human checks

> Distinguish routine checking from exceptional intervention.

- user-21, src:A1, src:B3

1.1.2 — Recurring checks enable continued operation

- user-22, src:A2

## 2 — Recurring review requires staffing

### 2.1 — Schedules must provide review time

2.1.1 — Daily checks require working time

- src:C4

2.1.2 — Staffing must make that time available

- None identified
```

Use exactly this structure: Status, Thesis and one Arc line, then H2 sections, H3 passages and plain argument lines separated by blank lines. Put an optional unlabelled `>` qualification immediately below the section, passage or argument it governs. End every argument with one unlabelled fragment bullet. The Arc line lists section numbers once in reading order. Number sections `1`, passages `1.1` and arguments `1.1.1`, restarting each local sequence at 1.

## Completion condition

Every in-scope section has an approved claim or question; every passage performs one approved claim; every passage has at least one approved ordered argument; every argument ends with exactly one valid fragment inventory; every qualification is attached to one identifiable object; and no structural question blocks the first unapproved passage.

## Blocking condition

An unresolved section purpose, passage claim, argument contribution, order, boundary or governing qualification blocks only dependent structure and predrafting. A lack of known fragments does not block arc completion when the inventory is `- None identified`; it may produce a predraft gap later.

## Next owner

[Predraft](predraft.md) proposes a limited input set from the broad inventories and develops every in-scope passage in arc order.
