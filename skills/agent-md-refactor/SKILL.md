---
name: "agent-md-refactor"
description: Refactor agent-generated markdown of any kind — instruction files, skills, plans, progress logs, reference material, drafts — into its shortest useful form. Holds operative decisions only, keeps one authoritative owner per rule and per type of information, states the file's purpose in its frontmatter, and audits that nothing load-bearing was lost. Use when a markdown file an agent reads or maintains has grown long, mixes unrelated concerns, duplicates rules, contradicts itself, repeats project-wide rules, or carries superseded state.
---

# Agent markdown refactor

- Rewrite one markdown file into its shortest useful form.

## Purpose

- State the file's purpose in one sentence.
  - Write it into the frontmatter `description` if it does not state it there.
- Keep a line only if it serves that purpose.
  - A line serving none is cut, not trimmed.
- If the purpose is unclear or wrong, ask. Do not invent one.
- The purpose governs every later decision in this skill. Nothing is kept against it.

## Language

- Short sentences, plain words, one claim each.
- A bullet beats a sentence that only asserts a fact.
- A table beats bullets when rows share one shape.
- Nest headers and bullets only as deep as the content needs.
- Cut hedging, throat-clearing, restatement, and any sentence repeating what the reader just read.
- Cut adjectives and intensifiers that carry no argument.
- Keep the author's voice and wording. Change structure and length, not tone.

## Bullets

- No paragraphs. Every statement is a bullet, a table row, or a heading.
- One bullet makes one contribution.
  - If it carries a second, split it and nest the second under it.
  - Split any bullet long enough to hide two claims.
- Every bullet nests under a parent stating the claim they share.
  - A flat list of unrelated items is a set of sections, not a list.
- Four levels is the working limit. Past that, use a table or a subheading.
- Consolidate repetition to one statement.
- Say the thing in the fewest tokens that stays unambiguous.

## State

- A markdown file holds current, operative decisions only.
  - History belongs to Git.

- Delete dates, times, "as discussed on", decision logs, superseded versions, completed task lists, and abandoned alternatives.
- Keep a decision while it is in force, and state it as though it were always so.
  - Record both constraints when both are live; the one that is live when the other has lapsed.
  - Record the rule, not the moment it was agreed.
- Exception: content and evidence files, where the record is the content — drafts, material, source maps.
  - Cut nothing there; only tighten.
- Exception: files whose stated purpose is the record itself — a changelog, a session log.
  - Prune to live state; never split.

## Additions and removals

- Additions are conservative. Every added line must be load-bearing; the default answer is cut.
- Removals are encouraged when something is superseded, duplicated, or owned elsewhere.

## Phase 1 — Type

- Identify the type before proposing. The type chooses the remedy; a wrong remedy damages the file.

| Type | Remedy |
|---|---|
| Instruction or context file — `AGENTS.md`, `CLAUDE.md`, `.cursorrules` | Merge duplicate rules. Extract reference only if nothing cites the file by name |
| Skill — `SKILL.md` with `references/` | Body stays procedural, deep reference moves to linked files, README stays short |
| Plan or spec | Usually leave whole. Split only a section with independent coherence |
| Progress or handoff log | Do not split. Prune to live state |
| Content or evidence — draft, material, source map | Leave structure alone. Duplication is a content question |
| Reference or appendix | Dedupe. Keep one owner, link to it |

- Splitting is a last resort. Consolidating in place, and leaving a file alone, are both correct answers.
- Search the repository for citations of the filename before moving anything.

## Phase 2 — Contradictions

- Find rules that conflict before restructuring.
- Report each conflict as a question. Never pick a winner.
- Re-read the surrounding sections first; an apparent conflict is often already reconciled nearby.

## Phase 3 — Structural pass

- Make every statement a bullet, table row, or heading.
- Split long bullets and nest them under the claim they share.
- Cut what the purpose test rejects.
- Report every cut. Never delete silently.

## Phase 4 — Semantic pass

- A structural pass leaves duplication a merge reveals.
  - Read each file against the others and ask of every statement:

- Is it true here, and only here?
  - A rule enforced elsewhere is not restated. Name the owner and link, or cut the line.
  - A fact derivable from the owner it points at is referenced, not repeated.
- Is it meaningful at all?
  - Cut a line the reader could already infer.
  - Cut a line whose only content is that something was checked, approved, confirmed or considered, with no live state attached.
  - Cut a line describing a process rather than a state.
- Does it belong to another kind of file?
  - Every type of information, record, and documentation has one destination.
  - A file holds only what serves its purpose; content found elsewhere moves out, not stays in both.

### Authoritative rules

- Project-wide rules live in exactly one file — this skill, `AGENTS.md`, or another declared authority.
  - No other file restates them. It links the owner instead.
  - An approval, eligibility, or exclusion rule stated in several files is the common defect: keep the fullest statement in the owner and delete the rest.
- A standing rule states how its own exceptions are handled.
  - The rule owns the exception policy; an entry carries only its own exception.
  - An entry that must deviate says so where the reader meets it, citing the rule.
- Duplication is not always waste.
  - Keep a second copy only where the file is read in a context that does not include the owner.
  - Link rather than restate even then.

## Phase 5 — Apply

- Preserve existing formatting and frontmatter conventions.
- Give output files only `name` and `description` frontmatter, `name` equal to the filename.
- Locate each edit by content and assert it before writing.

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

- Verification is mandatory. Restructuring is easy to eyeball and easy to get wrong.

1. Capture a baseline: line count, word count, section list.
2. Enumerate the file's content units as a checklist — each rule, owner, command, override, exception, path.
3. After editing, find a distinctive phrase from every unit in the new file.
4. Confirm each removed line is a duplicate, a merge target, or a reported cut.
5. Confirm every rule the file used to state still has one owner somewhere.
6. Confirm every link and citation still resolves.
7. Report lines, words, and percentage change.

- A small reduction is a legitimate finding when everything left is load-bearing. An inflated success claim is not.

## Anti-patterns

| Avoid | Instead |
|---|---|
| Defaulting to a split | Choose the remedy by type |
| Optimising a line target | Judge by what the reader needs |
| A paragraph where a bullet would do | One bullet, one contribution |
| A bullet carrying two claims | Split and nest |
| A flat list of unrelated items | Nest under the claim they share |
| The same rule at two scopes | State it once at the widest scope |
| Restating a project-wide rule | Link the authoritative owner |
| An entry repeating its own rule | Rule states the policy, entry the deviation |
| A README restating its `SKILL.md` | Point to the skill |
| Growing a log forever | Prune to live state |
| Silent deletion | Report, then cut on approval |
| Adding to fill a gap | Cut instead |
| Keeping history in the body | Leave it to Git |
| Claiming success unmeasured | Report counts and percentage |
| Splitting during a subtask | Refactor when asked |

## Checklist

- [ ] Purpose stated in one sentence and in the frontmatter
- [ ] Type identified; citations searched
- [ ] Contradictions surfaced for the user
- [ ] Remedy chosen by type, trade-off stated
- [ ] Applied; voice and conventions preserved
- [ ] No paragraphs; every bullet one contribution and nested under a shared claim
- [ ] Repetition consolidated to one statement per rule
- [ ] Semantic pass: no rule restated from its owner, no line stating no live condition
- [ ] Each information type has one destination; no file holds what serves another
- [ ] Every standing rule states how its exceptions are handled
- [ ] Every cut reported
- [ ] Every content unit re-checked; counts and percentage reported
- [ ] Submodule committed and pushed before the parent pointer