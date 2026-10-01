---
name: "agent-md-refactor"
description: Refactor agent-generated markdown of any kind — instruction files, skills, plans, progress logs, reference material, drafts — into its shortest useful form. Holds operative decisions only, keeps one authoritative owner per rule and per type of information, states the file's purpose in its frontmatter, and audits that nothing load-bearing was lost. Use when a markdown file an agent reads or maintains has grown long, mixes unrelated concerns, duplicates rules, contradicts itself, repeats project-wide rules, or carries superseded state.
---

# Agent markdown refactor

- Rewrite one markdown file into its shortest useful form.

## Purpose

- State the file's purpose in one sentence.
  - Write the purpose into the frontmatter `description` when the file does not state it there.
- Keep a line only if it serves that purpose.
  - Cut a line that serves no purpose. Do not trim it and keep it.
- If the purpose is unclear or wrong, ask. Do not invent one.
- The purpose governs every later decision in this skill. Nothing is kept against it.

## Language

- Short sentences, plain words, one claim each.
- A bullet beats a sentence that only asserts a fact.
- A table beats bullets when rows share one shape.
- Nest a header or bullet only as deep as the content requires.
- Cut adjectives and intensifiers that carry no argument.
- Keep the author's voice and wording. Change structure and length, not tone.

## Sentences

- Write every bullet as a sentence that stands on its own. The parent bullet supplies the context.
- Every sentence names its subject, verb and object. Never leave the actor unnamed.
- Name the actor instead of "this", "it", "they" or "the above" when the referent is not the subject's own parent.
  - A pronoun pointing at the parent bullet is clear. A pronoun pointing across the file is not.
- Use the active voice. A sentence beginning "It should be" or "Can be" names no actor.
- Cut announcements, throat-clearing and hedges.
  - Cut "Note that", "It is important to", "It should be noted", "This is key".
  - Cut "may", "might", "could" where the rule is unconditional. Keep them where the uncertainty is real.
- Describe rather than sell. A markdown explains what the file does. A markdown does not persuade.
  - Cut "powerful", "robust", "seamless", "comprehensive", "effortless", "delightful", "game-changing".
  - Cut "we" and "our". Name the actor or the file.
- Stay humble. A file explains its own behaviour and states its own limits.
  - A file does not announce that it is powerful, complete or the best available.
  - Where a limit exists, the file states the limit rather than the claim.

## Bullets

- No paragraphs. Every statement is a bullet, a table row, or a heading.
- One bullet makes one contribution.
  - If it carries a second, split it and nest the second under it.
  - Split any bullet long enough to hide two claims.
- Nest every bullet under a parent that states the claim they share.
  - A flat list of unrelated items is a set of sections, not a list.
- Four levels is the working limit. Past that, use a table or a subheading.
- State a repeated rule once, at its widest scope.
- Use the fewest words that keep the meaning unambiguous.

## State

- A markdown file holds current, operative decisions only.
  - Git holds the history.

- Delete dates, times, "as discussed on", decision logs, superseded versions, completed task lists, and abandoned alternatives.
- Keep a decision while it is in force, and state it as though it were always so.
  - Record both constraints when both are live; the one that is live when the other has lapsed.
  - Record the rule, not the moment it was agreed.
- Exception: content and evidence files, where the record is the content — drafts, material, source maps.
  - Cut nothing there. Tighten the wording only.
- Exception: files whose stated purpose is the record itself — a changelog, a session log.
  - Prune to the live state. Never split the file.

## Additions and removals

- Add a line only when the file cannot do its job without it. Cut by default.
- Cut a line when the content is superseded, duplicated or owned elsewhere.

## Phase 1 — Type

- Identify the type before proposing. The type chooses the remedy; a wrong remedy damages the file.

| Type | Remedy |
|---|---|
| Instruction or context file — `AGENTS.md`, `CLAUDE.md`, `.cursorrules` | Merge the duplicate rules. Move reference material out only when nothing cites the file by name |
| Skill — `SKILL.md` with `references/` | Keep the body procedural, move the deep reference into linked files, keep the README short |
| Plan or spec | Leave the file whole in most cases. Split a section only when it stands on its own |
| Progress or handoff log | Do not split. Prune to live state |
| Content or evidence — draft, material, source map | Leave the structure alone. Treat duplication as a content question |
| Reference or appendix | Remove the duplication, keep one owner, and link to that owner |

- Treat splitting as a last resort. Consolidating in place and leaving a file alone both give a correct result.
- Search the repository for citations of the filename before moving anything.

## Phase 2 — Contradictions

- Find rules that conflict before restructuring.
- Report each conflict as a question. Leave the choice to the user.
- Re-read the surrounding sections before reporting. A conflict often resolves itself nearby.

## Phase 3 — Structural pass

- Make every statement a bullet, table row, or heading.
- Split a long bullet. Nest the parts under the claim they share.
- Cut every line the purpose test rejects.
- Report every cut before making it. Never delete silently.

## Phase 4 — Semantic pass

- A merge reveals duplication that a structural pass leaves in place.
  - Read each file against the others.
  - Ask four questions of every statement.

- A rule enforced elsewhere is not restated. Name the owner and link, or cut the line.
  - Reference a fact that the linked owner already implies.
- A line must say something the reader could not infer.
  - Cut a line the reader can already infer.
  - Cut a line whose only content is that something was checked, approved, confirmed or considered, with no live state attached.
  - Cut a line that describes a process rather than a state.
- Every kind of information, record and documentation has exactly one owner.
  - Move content that belongs elsewhere into the file that serves its purpose.
  - Do not leave the same content in two files.

### Authoritative rules

- Put each project-wide rule in exactly one file — this skill, `AGENTS.md`, or another declared authority.
  - Let every other file link the owner instead of restating the rule.
  - An approval, eligibility or exclusion rule that appears in several files is the common defect. Keep the fullest statement in the owner and delete the rest.
- A standing rule states how it handles its own exceptions.
  - The rule owns the exception policy. An entry carries only its own exception.
  - An entry that must deviate says so where the reader meets it, and cites the rule.
- Some duplication earns its place.
  - Keep a second copy only where a reader meets the file without the owner.
  - Link rather than restate even then.

## Phase 5 — Apply

- Keep the file's existing formatting and frontmatter conventions.
- Give output files only `name` and `description` frontmatter, `name` equal to the filename.
- Locate each edit by content. Assert the content exists before writing.

## Cut criteria

- Apply the purpose test first. Then cut on any of these.

| Criterion | Example |
|---|---|
| Superseded | A replaced rule kept alongside its replacement |
| Historical | A date, a decision log, a finished task |
| Duplicated | The same rule stated twice |
| Owned elsewhere | A rule whose canonical owner is another file |
| Rarely needed | Reference a reader opens occasionally |
| Inert detail | Framework- or topic-specific detail that changes no behaviour |
| Vague | "Write clean code" |
| Overly obvious | "Do not introduce bugs" |
| Redundant | "Use TypeScript" in a TypeScript project |

## Verification

- Always verify. A reader can check a structure by eye and still miss a lost rule.

1. Capture a baseline: the line count, the word count and the section list.
2. List the file's content units as a checklist: each rule, owner, command, override, exception and path.
3. After editing, search the new file for a distinctive phrase from every unit.
4. Confirm that every removed line duplicates another line, merges into another line, or appears in your cut report.
5. Confirm that every rule the file used to state still has one owner somewhere.
6. Confirm that every link and citation still resolves.
7. Report the line count, the word count and the percentage change.

- Report a small reduction as the honest result when every remaining line carries weight. Do not describe a small reduction as a cleanup.

## Anti-patterns

| Avoid | Instead |
|---|---|
| Defaulting to a split | Choose the remedy by type |
| Optimising a line-count target | Judge by what the reader needs |
| A paragraph where a bullet would do | One bullet, one contribution |
| A bullet carrying two claims | Split and nest |
| A flat list of unrelated items | Nest the items under the claim they share |
| The same rule at two scopes | State it once at the widest scope |
| Restating a project-wide rule | Link the authoritative owner |
| An entry repeating its own rule | Rule states the policy, entry the deviation |
| A README restating its `SKILL.md` | Point to the skill |
| Growing a log forever | Prune to live state |
| Silent deletion | Report the cut, then delete it on approval |
| Adding words to fill a gap | Cut the line instead |
| Keeping history in the body | Leave the history to Git |
| Claiming success without a measurement | Report the counts and the percentage |
| Splitting a file during a subtask | Refactor the file when the user asks |

## Checklist

- [ ] The purpose appears in one sentence and in the frontmatter
- [ ] The type is identified and the citations are searched
- [ ] Every contradiction is surfaced for the user
- [ ] The remedy matches the type and the trade-off is stated
- [ ] The file is applied with its voice and conventions preserved
- [ ] The file has no paragraphs, and every bullet makes one contribution under a shared claim
- [ ] Each repeated rule is stated once
- [ ] No file restates a project-wide rule, and no line states no live condition
- [ ] Each kind of information has one owner; no file holds what serves another file
- [ ] Every standing rule states how it handles its own exceptions
- [ ] Every cut appears in the report
- [ ] Every content unit is re-checked, and the counts and percentage are reported
- [ ] The submodule is committed and pushed before the parent pointer