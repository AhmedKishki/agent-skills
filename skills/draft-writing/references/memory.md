# Project memory

`{project}-memory.md` preserves context between tasks so that a new session can pick up the project without the conversation that produced it: it is the handoff record of the substantial information the workflow files do not already state. It is not a history log and holds no article content.

The project's actual memory is handled by MCP tooling outside this skill. This skill maintains only the markdown record — never read from or write to a memory server on the skill's behalf.

## What it holds

Four sections, in this order:

- **Current focus** — one short paragraph: what the work is on and why it stopped there.
- **Decisions** — agreed decisions, one line each, with origin marked (user instruction, user approval, the user's own synthesis).
- **Questions** — open and closed questions with stable IDs (`Q1`, `Q2`, …). An ID is never reused; a closed question keeps its ID and gains its resolution. Long-lived research tasks live here as open questions.
- **Rejected** — formulations and directions set aside, each with its reason.

Record only what is substantial: an agreed decision, an opened or closed question, a rejection with its reason, a shift in focus. Keep out session chatter, transient task state, and anything a workflow file already says. The [activity tracker](activity-tracker.md) owns Now and Next; never duplicate them here.

## FIFO, from the top

The record is updated from the top: a new entry goes at the top of its section, so the newest substance is read first. As entries stop being useful — resolved, superseded, no longer load-bearing — they fall away from the bottom. First in, first out: the record keeps only what is still substantial, newest at the top.

## When to write

- **Session start** — read the record, with the tracker, to recover context.
- **During** — as soon as the user states or approves something substantial, record it; open and close questions as they happen; record rejections with their reasons.
- **Session end** — bring the record current: focus, decisions, questions, rejections.

## File shape

    # Writing memory

    [Lean process header]

    ## Current focus

    One short paragraph.

    ## Decisions

    - The decision, one line — origin. (newest first)

    ## Questions

    ### Q3 · short title — open

    - The question, what it blocks, what would close it.

    ### Q1 · short title — closed

    - The resolution.

    ## Rejected

    - The rejected formulation — the reason.

Save and track per the [shared output-file standard](file-output-standard.md).
