# Project memory

`{project}-memory.md` is the project's context-preservation record: it stores everything a different AI, in a new chat, needs to resume the project seamlessly without the conversation that produced it — what the project is, where things stand, the plan, what is expected, and where everything lives. A new session reads it first and works from it. It is not a history log and holds no article content.

The project's actual memory is handled by MCP tooling outside this skill. This skill maintains only the markdown record — never read from or write to a memory server on the skill's behalf.

## What it holds

- **Resume** — everything a cold start needs, in this order: what the project is (subject, scope, the standing conventions, the governing skill and its path); where things stand, per workflow file (status and one line each); the plan (how the current stage proceeds, step by step); what is expected (the rules that govern the work); where everything lives (the file paths). Brought current at every session end, so the record is resumable at any stop.
- **Decisions** — agreed decisions, one line each, with origin marked (user instruction, user approval, the user's own synthesis). Newest first.
- **Questions** — open and closed questions with stable IDs (`Q1`, `Q2`, …). An ID is never reused; a closed question keeps its ID and gains its resolution. Long-lived research tasks live here as open questions.
- **Rejected** — formulations and directions set aside, each with its reason.

Record only what is substantial: an agreed decision, an opened or closed question, a rejection with its reason, a shift in focus. Keep out session chatter, transient task state, and anything a workflow file already states in full — reference it instead. The [activity tracker](activity-tracker.md) owns Now and Next; the resume section names the files and the plan, and never duplicates their detail.

## FIFO, from the top

The record is updated from the top: a new entry goes at the top of its section, so the newest substance is read first. As entries stop being useful — resolved, superseded, no longer load-bearing — they fall away from the bottom. First in, first out: the record keeps only what is still substantial, newest at the top.

## When to write

- **Session start** — read the record, with the tracker, to recover context; work from the resume section.
- **During** — as soon as the user states or approves something substantial, record it; open and close questions as they happen; record rejections with their reasons.
- **Session end** — bring the record current: the resume sections above all, so the handoff is seamless at any stop; decisions, questions, rejections.

## File shape

    # Writing memory

    [Lean process header]

    ## Resume — what a new session needs

    What the project is and its standing conventions · where things stand, per workflow file · the plan and the immediate next step · what is expected · where everything lives.

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
