# Consent and state

## Purpose

Apply only the user's explicit decision to the exact object presented.

## Approval

Approval must unambiguously identify the exact proposal or revision. Silence, partial approval, lack of objection, “continue” and “next” do not approve. A changed object requires a new revision and approval.

## Argument states

Use exactly: `Unstarted`, `Inputs awaiting approval`, `Blocked by gap`, `Candidate awaiting decision`, `Revision requested`, `Rejected`, `Approved and saved`, `Invalidated`.

| Current | Event | Next | Action |
|---|---|---|---|
| Unstarted or Invalidated | Exact input set presented | Inputs awaiting approval | Wait. |
| Inputs awaiting approval | Exact inputs approved; candidate produced | Candidate awaiting decision | Save in predraft-working; present full record. |
| Inputs awaiting approval | Exact inputs approved; gap returned | Blocked by gap | Present gap; wait. |
| Inputs awaiting approval | Inputs changed | Inputs awaiting approval | Revise; present again. |
| Candidate awaiting decision | Exact candidate approved | Approved and saved | Copy to predraft; delete working file. |
| Candidate awaiting decision | Change requested | Revision requested | Route and revise. |
| Candidate awaiting decision | Candidate rejected | Rejected | Retire revision; keep argument active. |
| Revision requested | Revised inputs presented | Inputs awaiting approval | Wait. |
| Revision requested | Revised candidate from unchanged inputs presented | Candidate awaiting decision | Wait. |
| Approved and saved | Approved basis changes | Invalidated | Identify impact; reopen argument. |

## Procedure

1. Classify the response: approve, reject, revise prose, change inputs, change schema, change blueprint, change direction, confirm contradiction, make operative, supply wording, supply source or request explanation.
2. Route each class to its owner.
3. If new direction may contradict operational direction, present both commitments and consequences. Ask whether the contradiction is intended and whether the new commitment shall become operative. Wait for both confirmations.
4. Apply only the matching state transition.
5. Record the state and exact next action.

A rejected candidate does not remove its schema argument. Removal requires explicit schema approval. A request for explanation changes no state.

## Blocking

If one response could authorise incompatible actions, ask one focused question and wait.