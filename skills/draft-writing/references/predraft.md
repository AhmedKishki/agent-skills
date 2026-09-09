# Predraft

## Purpose

Collaboratively develop, revise, approve and save the raw material for every in-scope article-arc passage.

## Inputs

The approved article arc, thesis and vision, user wording, source maps, tracker, and any existing predraft or working candidate.

Predrafting must process every passage included in the approved article arc. The default order is arc reading order. Change the order or exclude a passage only after the user explicitly approves the corresponding arc change.

## Procedure

1. **Open.** Read the governing section, passage ID and claim, ordered arguments, their broad fragment inventories, applicable arc qualifications, thesis constraints, tracker and any existing selection. Set the passage to `Unstarted` or retain `Invalidated`.
2. **Propose inputs.** Begin with each argument's arc inventory and propose only a limited synthesis set for the passage. For every proposed `user-n` or source code, present its exact span, location, context, intended use, support and limits. Keep unselected inventory fragments available for later proposals; inventory membership is not input approval.
3. **Obtain input approval.** Ask: **“Do you approve this input set for passage {ID}, or what should change?”** Set `Inputs awaiting approval` and wait. Do not run synthesis before approval.
4. **Synthesize.** Run [white-box synthesis](white-box-synthesis.md) for this passage only. For a typed gap, set `Blocked by gap`, present its focused question and wait; route the answer before retrying.
5. **Persist and present the candidate.** Save the unapproved candidate and full record in `{project}-predraft-working.md`. Present passage ID and claim, complete prose, compact provenance, argument coverage, exact fragments, ordered operations, support, limits, qualifications and revision ID. Ask: **“Do you approve passage {ID}, reject it, or what should change?”** Set `Candidate awaiting decision` and wait.
6. **Classify the response.** Apply [consent and state](consent-and-state.md). Route prose, inputs, arc, wording and source changes to their owners. A request for explanation changes no candidate. Give every revision a new `{passage}-r{number}` ID and present its complete record.
7. **Save after approval.** Save the exact approved prose in arc order with its compact provenance immediately below it. Verify exact correspondence and every basis, clear the working candidate, set `Approved and saved`, update the tracker, then open the next passage.

Never prepare a later passage before the current one is approved and saved. Rejection retires only that revision. It does not skip or remove the passage.

Do not propose an unlisted fragment silently. Explain why it is needed, propose adding it to the relevant argument inventory, obtain approval for that arc revision, synchronize the arc, and then include it in a limited input proposal. Approval of an inventory revision does not approve the synthesis set. Compact provenance names only fragments actually used in the approved passage, not every inventory member.

## Raw-material boundary

Predraft includes the internal connections required for a passage's arguments to establish its single claim. It normally excludes wording whose sole function is to connect distinct passages or sections, reader-facing headings, final paragraph decisions, citation formatting and bibliography formatting. Include an inter-passage or inter-section connector only when the user explicitly assigns it to a passage's claim; then synthesize and approve it as part of that passage.

## Output

### Selected predraft

```markdown
# Predraft

## 1 — Human work

### 1.1 — Human review sustains the service

Reviewers check flagged results every day. Daily review keeps the service running.

**Provenance:** Mixed · **Method:** white-box synthesis · **Basis:** A1, user-21, user-22
```

Use one H1, H2 arc sections and H3 passages. Put exactly one compact [provenance](provenance.md) line immediately after each approved passage. Do not create separate prose and provenance parts or save the full construction record here.

### Working candidate

```markdown
# Predraft working candidate

Passage: 1.1
Revision: 1.1-r1
State: Candidate awaiting decision
Not selected: This candidate has not been approved for the article.

<Complete candidate, provenance and full construction record.>
```

Overwrite this file for a revised candidate of the same passage. Clear it only after approval, explicit abandonment, or removal of the passage from the approved arc. On resumption, re-present its exact candidate before acting on a later approval.

## Completion condition

Every in-scope arc passage is present once in arc order, has explicit approval and is followed immediately by exactly one resolving provenance line. No working candidate or invalidated passage remains.

## Blocking condition

An unapproved limited input set, an unsynchronized proposed inventory addition, typed gap, pending passage decision or invalidated passage blocks that passage and every later passage.

## Next owner

[Drafting](drafting.md) turns the complete raw predraft into a connected reader-facing article.
