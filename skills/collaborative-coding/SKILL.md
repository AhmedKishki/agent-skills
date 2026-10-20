---
name: collaborative-coding
description: >-
  Collaborate on coding through a shared, ordered task list and explicit approval
  of each small code patch before applying it. Use when the user asks for
  collaborative coding, anti-vibe-coding, or step-by-step coding with explanations
  and approval before edits. Supports Beginner, Standard, and Expert explanations.
---

# Collaborative Coding

The user directs the work. Turn their goal into agreed tasks, then work through
one small step at a time. Do not treat a goal as permission to implement it.

## Suggested code

Make all suggested code self-documenting. Name variables, functions, and classes
for their purpose. Prefer short names and familiar abbreviations when their
meaning stays clear; use a longer name when shortening it would obscure intent.
Clarity takes priority over brevity. Do not rely on comments or chat explanations
to compensate for unclear names.

## Start or resume

1. Identify the target workspace root, not the installed skill directory. Ask if
   it is ambiguous. Read applicable project instructions and relevant code.
   Keep this inspection read-only and limited to understanding the requested work.
2. Read [Task list](references/task-list.md) before creating or editing
   `<workspace-root>/collab-coding/TASKS.md`. Read the existing file before planning.
3. Confirm the goal, constraints, and what counts as success. Ask only about gaps.
4. Read [Explanations](references/explanations.md) before proposing code; follow
   its guidance for choosing a level and explaining the patch.
5. Propose concise tasks in chronological execution order, with prerequisites
   first. Ask the user to approve or revise the plan before writing it.
6. On resume, reconcile the current task list with the user's latest instructions
   and working files. Ask about conflicts; do not overwrite user changes or infer
   code approval from task-list edits. Do not repeat settled setup questions.

## Work through one step

1. Select the first remaining task and propose its next small, logical subtask.
   Resolve any missing decision with a concise question and a recommendation.
2. Show the exact proposed patch, its file paths, purpose, and intended check.
   Include additions, replacements, deletions, and any test or configuration edits.
   For a new file, show its proposed contents. Keep each patch to one purpose and
   split larger changes into smaller reviewable steps rather than hiding parts.
3. Explain that code at the chosen level. State material risks or alternatives,
   recommend an approach, and ask a clear question such as:
   "Apply this patch and run this check, or revise it?" Wait for the user's reply.
4. Establish agreement using the approval rules below. Do not edit while waiting.
5. Re-read affected files before applying the patch. If their contents changed,
   reconcile the differences and present a revised patch for approval. Otherwise,
   apply only the agreed patch and perform only the agreed checks or actions.
6. Report the actual result briefly, including failures or checks not run. Ask
   whether the step is accepted. Handle completion through the task-list rules.
   Return to step 1 for the next subtask; never silently continue coding.

## Approval rules

- Approval covers one exact, currently presented patch and the stated actions,
  not a whole task, file, goal, or future change. A short "yes" is enough only
  when it unambiguously answers the current approval question.
- A user suggestion is a proposal, not automatic authority for an unseen patch.
  If you agree, reflect it in the exact patch and ask for confirmation. If the
  user supplied the complete exact change, explicitly asked you to apply it, and
  you agree with it, state your agreement; no redundant confirmation is needed.
- If you disagree, explain the concrete concern and suggest an alternative.
  Keep discussing until both sides accept the same change. Do not silently
  substitute your preference or agree to something you know is incorrect.
- A revised patch or expanded action needs fresh approval. A question, silence,
  a task-list edit, or approval of an earlier version is not approval of this one.
- If a check fails, explain the failure and propose the fix as a new step. Do not
  quietly repair, reformat, refactor, or add dependencies beyond the approved work.
- Name commands and their material effects in the proposal. Approval to inspect
  or test is not permission to install, migrate, delete data, commit, push, or
  deploy. Obtain explicit agreement for those actions and obey host permissions.
- Do not delegate implementation to bypass these gates. Any delegated analysis
  must stay read-only; its suggestions still need the same user approval.
- If the user asks to skip approvals, explain that this leaves collaborative
  coding and ask whether they intend to exit it. Do not silently disable the gates.
  On explicit exit, leave `TASKS.md` intact and follow the newly agreed workflow.

## Keep the collaboration lean

Ask one focused question at each decision point. Offer a concrete recommendation
and only meaningful alternatives. Keep proposals and discussion in chat; keep the
task file short. Explain uncertainty plainly and let the user decide trade-offs.
