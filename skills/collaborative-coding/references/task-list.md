# Task list

Use `<workspace-root>/collab-coding/TASKS.md` as the single shared list of remaining
work. Both the user and the agent may edit it. It is a plan, not code approval.

## Contents

Keep only the goal, chosen explanation level, and remaining tasks. Use a numbered
list in agreed execution order. Give each task a short action and a concrete
completion condition. Add short subtask bullets only where they help the current
discussion. Avoid speculative detail for later tasks.

Example during work:

```markdown
# Tasks

Goal: Reject invalid ages before saving a profile.
Explanation: Standard

1. Validate age input — accept integers from 0 through 130 only.
   - Agree on the error returned for invalid input.
   - Add the validator and check its boundary cases.
2. Connect validation to saving — invalid input must not reach storage.
```

Write clearly, directly, concisely, and plainly. Do not add progress essays,
approval logs, code blocks, explanations, timestamps, completed-item archives,
speculative backlogs, or duplicate status sections to the actual task file.

## Updating the file

- Propose the initial plan in chat. Write it only after agreement. That agreement
  authorizes creating the directory and task file, not implementation files.
- Immediately before every write, including completion cleanup, re-read the file.
  Preserve the user's wording and changes with a focused edit, not a replacement.
- Discuss additions, removals of unfinished work, changed goals, changed completion
  conditions, and reordering before editing. A direct user instruction to make
  an exact plan change is sufficient; clarify ambiguous edits or conflicts.
- Treat a user's direct file edit as a plan proposal: acknowledge it and reach
  agreement before treating it as settled. It still does not approve code edits.
- A user request to switch explanation level authorizes updating that field.
- Keep a task or subtask while its work is incomplete, checks fail or are pending,
  or the user has not accepted its result. Report checks that cannot be run;
  agree on any changed verification requirement rather than claiming success.
- After the agreed checks pass and the user accepts completion, automatically
  remove the completed item. No separate approval for that housekeeping is needed.
  Preserve unfinished subtasks; remove the parent only when its completion
  condition is satisfied and the user accepts it. Renumber remaining tasks.
- When no work remains, keep the heading, goal, and explanation level, followed by
  `No remaining tasks.` Do not invent more work or delete the shared file.

On resume, use the file to recover the plan and level, not as proof of an approved
patch. Re-establish approval when the conversation no longer shows what was agreed.
