---
name: "agent-md-refactor"
description: Refactor agent-generated markdown of any kind — instruction files, skills, plans, progress logs, reference material, drafts — into its shortest useful form. Holds operative decisions only, keeps one authoritative owner per rule and per type of information, states the file's purpose in its frontmatter, and audits that nothing load-bearing was lost. Use when a markdown file an agent reads or maintains has grown long, mixes unrelated concerns, duplicates rules, contradicts itself, repeats project-wide rules, or carries superseded state.
---

# Agent markdown refactor

- Rewrite one markdown file into its shortest useful form.
- Apply structural and language edits to operational scaffolding only. Quotations, approved passages, author comments, drafts and finite provenance require their own edit or relocation approval.

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

## Sections

- Divide the file into sections, and each section into subsections, wherever the entries fall into groups.
  - A flat list of entries that differ in kind needs sections before it needs bullets.
- Write each heading as a noun phrase or a question that describes what the section holds.
  - A reader who reads only the headings should learn the file's structure.
- Keep a heading honest. A heading promises what its section delivers.
  - Do not write "Overview" or "General" when the section holds specific rules.
  - Do not write "Next steps" when the section holds a decision record.
- Order the sections so the file reads in the order a reader needs it.
  - Put the purpose and the rules first, the detail last.
- Do not invent a section that holds one bullet. Promote it to a bullet of its parent.
- Grep the repository before renaming a heading. Another file may cite its anchor.

## Consolidation across files

- A rule that two files state belongs to the file that owns it.
  - Keep the complete rule and every unique qualification in the owner. Neither copy is a substitute when their limits or examples differ.
  - Remove other copies. Keep a link only when it navigates to an input, rule or next action the reader needs.
- Consolidate the entries that repeat a value or a list.
  - Define an item once, then refer to it by its identifier.
- Do not replace the owner's information or qualifications with a pointer. Do not add a sentence announcing where a removed copy went.
- Report every consolidation with the files it touched.

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

- Operational scaffolding holds current, operative decisions only.
  - Git holds the history.

- Remove superseded proposals, completed intervention narratives, audit diaries, file-by-file save accounts and chat-option captions. Keep live approval states and exceptions, not their agreement history.
- Keep a decision while it is in force, and state it as though it were always so.
  - Record both constraints when both are live; the one that is live when the other has lapsed.
  - Record the rule, not the moment it was agreed.
- Exception: content and evidence files, where the record is the content — drafts, material, source maps.
  - Preserve exact recorded wording, dates, locators, approval scope and provenance. Refactor only separable scaffolding; do not tighten protected wording without approval.
- Exception: files whose stated purpose is the record itself — a changelog, a session log.
  - Preserve the required record. Age alone is not a reason to delete it or split the file.

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
- Read the project's ownership contracts before planning edits. Classify every affected unit and its qualifications, and match them to one owner's allowed content.
  - Relevance, an existing heading or the file already open does not admit unlisted content.
  - If ownership is missing or ambiguous, ask before adding, deleting or relocating the unit. Protected misplaced records remain untouched until relocation is authorised; they do not permit new misplaced records.

## Phase 2 — Contradictions

- Find rules that conflict before restructuring.
- Report each conflict as a question. Leave the choice to the user.
- Re-read the surrounding sections before reporting. A conflict often resolves itself nearby.

## Phase 3 — Structural pass

- Make every statement a bullet, table row, or heading.
- Divide the file into sections wherever the entries fall into groups.
- Write each heading as a phrase that describes what its section holds.
- Split a long bullet. Nest the parts under the claim they share.
- Consolidate any rule that two files state into the file that owns it.
- Transfer every unique qualification to the receiving owner before removing the origin. Do not create a transfer diary or breadcrumb paragraph.
- Cut every line the purpose test rejects.
- Report every cut before making it. Never delete silently.

## Phase 4 — Semantic pass

- A merge reveals duplication that a structural pass leaves in place.
  - Read each file against the others.
  - Ask four questions of every statement.

- A unit must satisfy its owner's content contract. Move an authorised unit to its proper owner, not into a miscellaneous section or a file that merely links elsewhere.
- A line must say something the reader could not infer.
  - Cut a line the reader can already infer.
  - Cut a line whose only content is that something was checked, approved, confirmed or considered, with no live state attached.
  - Cut a line that describes a process rather than a state.
- Every kind of information, record and documentation has exactly one owner.
  - Move content that belongs elsewhere into the file that serves its purpose.
  - Do not leave the same content in two files.
- Reject second-order documentation: sentences saying another file records, holds, contains or has received information. State the information directly in its owner, or cut a redundant report.
- Keep source qualifications with sources, passage constraints with passages, and rule exceptions with their rules. Progress contains a resume point, next action and live blockers, not source inventories or approval histories.
- Compare conditions, modality, attribution, scope and order before and after consolidation. A surviving label or distinctive phrase is not proof that the qualification survived.

### Authoritative rules

- Put each project-wide rule in exactly one file — this skill, `AGENTS.md`, or another declared authority.
  - Let every other file link the owner instead of restating the rule.
  - An approval, eligibility or exclusion rule that appears in several files is the common defect. Keep the fullest statement in the owner and delete the rest.
- A standing rule states how it handles its own exceptions.
  - The rule owns the exception policy. An entry carries only its own exception.
  - An entry that must deviate says so where the reader meets it, and cites the rule.
- Preserve explicitly authorised content copies and standalone outputs required by their own contracts. Convenience or an isolated reading context does not authorise another operational record.
- A link that routes the reader to the file holding a rule is navigation, not a second copy of the rule.
- A file states its own content. It does not describe what another file holds, and it does not replace its content with a link to it.
- A qualification stays with the rule it qualifies. Move it into that rule's file.

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
2. Inventory each unit's owner, allowed category, protected wording, command, override, qualification, exception and path. Record scope and ordering words such as "only", "unless", "first" and "much, though not all".
3. For each removal, identify the surviving owner and complete equivalent unit, or the approved obsolete content. Unmatched unique information fails verification.
4. Compare before/after qualifications semantically, not just by phrase presence. Check attribution, modality, conditions, approval extent, exclusions and order; match protected wording and counters exactly unless their change was approved.
5. Check each receiving owner's allowed content and confirm the actual information and its qualifications are present there, not only a link or a sentence about a move. Reject a duplicate operational record or an implicit ownership exception.
6. Audit changed scaffolding for second-order documentation, source inventories in handoffs, historical narration, boilerplate and unclear actors. Treat string matches as findings to review, not permission to rewrite quotations or records.
7. Check every inbound link and anchor after a heading or file change, including links in unchanged files; then check outgoing links, citations and identifier references.
8. Run the project's applicable checks. A preservation or routing failure blocks completion; repair it or ask the author, never hide it behind a word-count reduction.
9. Report the line count, word count and percentage change. Keep the audit and cut report out of the operational files being cleaned.

- Report a small reduction as the honest result when every remaining line carries weight. Do not describe a small reduction as a cleanup.

## Anti-patterns

| Avoid | Instead |
|---|---|
| Defaulting to a split | Choose the remedy by type |
| Optimising a line-count target | Judge by what the reader needs |
| A paragraph where a bullet would do | One bullet, one contribution |
| A bullet carrying two claims | Split and nest |
| A flat list of entries that differ in kind | Divide the list into sections |
| A heading that promises what the section does not hold | Write the heading the section earns |
| The same rule stated in two files | Keep the owner, link the other file |
| A flat list of unrelated items | Nest the items under the claim they share |
| The same rule at two scopes | State it once at the widest scope |
| Restating a project-wide rule | Link the authoritative owner |
| An entry repeating its own rule | Rule states the policy, entry the deviation |
| A README restating its `SKILL.md` | Point to the skill |
| Growing a log forever | Prune to live state |
| "The file records…" or "This was added…" | State the information in its owner |
| Replacing required information with a link | Keep the information and its qualifications at the expected point |
| A source qualification in progress | Qualify the source in its map; keep only the verification action in progress |
| A surviving ID treated as proof of preservation | Compare the full scope, conditions, attribution and order |
| Silent deletion | Report the cut, then delete it on approval |
| Adding words to fill a gap | Cut the line instead |
| Keeping history in the body | Leave the history to Git |
| Claiming success without a measurement | Report the counts and the percentage |
| Splitting a file during a subtask | Refactor the file when the user asks |

## Checklist

- [ ] The type is identified and the citations are searched
- [ ] Every contradiction is surfaced for the user
- [ ] The remedy matches the type and the trade-off is stated
- [ ] The file is applied with its voice and conventions preserved
- [ ] Every cut appears in the report
- [ ] Every content unit is re-checked, and the counts and percentage are reported
- [ ] The submodule is committed and pushed before the parent pointer
