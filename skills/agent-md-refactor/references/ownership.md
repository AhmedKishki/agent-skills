# Ownership

## Each file's job

- A file's job is the purpose its meta-view row states, within its owner's content contract.
- A file does its job sufficiently: it holds everything its job requires and nothing outside it.
  - The job governs every decision in this skill. Nothing is kept against it.
- Keep a line only if it serves the job.
  - Cut a line that serves no part of the job. Do not trim it and keep it.
- Cut by default. Add a line only when the file cannot do its job without it.
  - Report a missing requirement to the user as a question. Add only wording the user supplies or approves; never fill the gap yourself.

## One owner per information type

- Every kind of information, record and documentation has exactly one owner.
  - Move content that belongs elsewhere into the file that serves its purpose.
  - Do not leave the same content in two files.
- Match every affected unit and its qualifications to one owner's allowed content.
  - Relevance, an existing heading or the file already open does not admit unlisted content.
  - If ownership is missing or ambiguous, ask before adding, deleting or relocating the unit. Protected misplaced records remain untouched until relocation is authorised; they do not permit new misplaced records.
- A unit must satisfy its owner's content contract. Move an authorised unit to its proper owner, not into a miscellaneous section or a file that merely links elsewhere.
- A qualification stays with the rule it qualifies. Move it into that rule's file.
  - Keep source qualifications with sources, passage constraints with passages, and rule exceptions with their rules.
- State a repeated rule once, at its widest scope.

## Project-wide rules

- Put each project-wide rule in exactly one file — this skill, `AGENTS.md`, or another declared authority.
  - Cut every restatement of the rule in other files.
  - An approval, eligibility or exclusion rule that appears in several files is the common defect. Keep the fullest statement in the owner and delete the rest.
- A standing rule states how it handles its own exceptions.
  - The rule owns the exception policy. An entry carries only its own exception.
  - An entry that must deviate says so where the reader meets it, and cites the rule.
- Preserve explicitly authorised content copies and standalone outputs required by their own contracts. Convenience or an isolated reading context does not authorise another operational record.

## Consolidation

- A rule that two files state belongs to the file that owns it.
  - Keep the complete rule and every unique qualification in the owner. Neither copy is a substitute when their limits or examples differ.
  - Remove the other copies.
- Consolidate the entries that repeat a value or a list.
  - Define an item once, then refer to it by its identifier.

## Live state

- Operational scaffolding holds current, operative decisions only.
  - Git holds the history.
- Remove superseded proposals, completed intervention narratives, audit diaries, file-by-file save accounts and chat-option captions. Keep live approval states and exceptions, not their agreement history.
- Keep a decision while it is in force, and state it as though it were always so.
  - Record both constraints when both are live; the one that is live when the other has lapsed.
  - Record the rule, not the moment it was agreed.
- Cut a line whose only content is that something was checked, approved, confirmed or considered, with no live state attached.
- Cut a line that describes a process rather than a state.
- Progress contains a resume point, next action and live blockers, not source inventories or approval histories.
- Exception: content and evidence files, where the record is the content — drafts, material, source maps.
  - Preserve exact recorded wording, dates, locators, approval scope and provenance. Refactor only separable scaffolding; do not tighten protected wording without approval.
- Exception: files whose stated purpose is the record itself — a changelog, a session log.
  - Preserve the required record. Age alone is not a reason to delete it or split the file.

## Cut criteria

| Criterion | Example |
|---|---|
| Superseded | A replaced rule kept alongside its replacement |
| Historical | A date, a decision log, a finished task |
| Duplicated | The same rule stated twice |
| Owned elsewhere | A rule whose canonical owner is another file |

## Anti-patterns

| Avoid | Instead |
|---|---|
| The same rule stated in two files | Keep the owner; cut the copy |
| The same rule at two scopes | State it once at the widest scope |
| Restating a project-wide rule | Cut the restatement |
| An entry repeating its own rule | Rule states the policy, entry the deviation |
| Writing a missing requirement yourself | Ask the user for it |
| A source qualification in progress | Qualify the source in its map; keep only the verification action in progress |
| Growing a log forever | Prune to live state |
| Keeping history in the body | Leave the history to Git |
