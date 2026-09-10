# Consent and state

## Purpose

Define proposal authority, shared response classes and predraft passage transitions. Later modules define their own object states.

## Inputs

The exact presented object, its current state and the user's response.

## Approval rule

Approval must name or unambiguously identify the exact presented object and revision. Silence, lack of objection, partial approval, and an ambiguous “continue” or “next” do not approve it. A changed object requires a new revision and approval. Approval selects a decision or wording without changing its authorship or authorising unlisted action.

## Passage states

Use exactly: `Unstarted`, `Inputs awaiting approval`, `Blocked by gap`, `Candidate awaiting decision`, `Revision requested`, `Rejected`, `Approved and saved`, `Invalidated`.

| Current state | Event | Next state | Required action |
|---|---|---|---|
| Unstarted or Invalidated | Agent presents the exact input proposal | Inputs awaiting approval | Wait for the user |
| Inputs awaiting approval | User approves the exact inputs and synthesis returns a candidate | Candidate awaiting decision | Persist and present the candidate and full record |
| Inputs awaiting approval | User approves the exact inputs and synthesis returns a gap | Blocked by gap | Present the typed gap and wait |
| Inputs awaiting approval | User changes or comments on inputs | Inputs awaiting approval | Route, revise and re-present inputs |
| Candidate awaiting decision | User explicitly approves the whole candidate | Approved and saved | Save it with inline provenance |
| Candidate awaiting decision | User requests any change | Revision requested | Route the change and revise |
| Candidate awaiting decision | User rejects it | Rejected | Retire that revision and keep the passage open |
| Revision requested | Agent presents revised inputs | Inputs awaiting approval | Wait for the user |
| Revision requested | Agent presents a revised candidate using unchanged approved inputs | Candidate awaiting decision | Wait for the user |
| Rejected | User supplies replacement direction | Revision requested | Route the direction and revise |
| Blocked by gap | User supplies a resolution | Inputs awaiting approval | Route the answer and present the revised input set |
| Approved and saved | An approved upstream basis changes | Invalidated | Identify the cause and reopen the passage |

## Procedure

1. Match the user's response to one or more classes: `Approve`, `Reject`, `Revise prose`, `Change inputs`, `Change arc`, `Change blueprint`, `Change direction`, `Confirm contradiction`, `Make operative`, `Supply new wording`, `Supply new source material`, `Request explanation`.
2. Route each class through [ownership and routing](ownership-and-routing.md). A structural decision, its resulting prose and its citation are separate approval objects.
3. When new direction may contradict an operational commitment, pause the passage transition. Present both commitments and their consequences, ask whether the contradiction is intended, and separately confirm that the new commitment shall become operative. Only then mark the superseded aspect `Outdated`, apply the replacement and invalidate affected downstream passages.
4. Apply only the transition in the table. A request for explanation changes no state.
5. Rejection does not remove or skip a passage. Remove or skip it only through an explicitly approved arc change.
6. Record the resulting state and next action in the tracker.

## Output

One recorded state transition and the exact next permitted action.

## Completion condition

The response is classified, routed and reflected in the tracker without inferring authority.

## Blocking condition

If the response could authorize more than one incompatible transition, or does not establish whether contradictory new direction shall become operative, ask one focused question and wait.

## Next owner

The module named by the classified response; predraft resumes after upstream changes are applied.