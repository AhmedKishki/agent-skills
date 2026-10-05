# Best practice

## Scope

- Apply structural and language edits to operational scaffolding only.
- Quotations, approved passages, author comments, drafts and finite provenance require their own edit or relocation approval.

## Remedy by file type

- Identify the type before proposing. The type chooses the remedy; a wrong remedy damages the file.

| Type | Remedy |
|---|---|
| Instruction or context file — `AGENTS.md`, `CLAUDE.md`, `.cursorrules` | Merge the duplicate rules. Move reference material out only when nothing cites the file by name |
| Skill — `SKILL.md` with `references/` | Keep a single-file skill's procedure in `SKILL.md`. In a multi-file skill, make `SKILL.md` the meta view, put the procedure and reference in files that do not link each other, and keep the README short |
| Plan or spec | Leave the file whole in most cases. Split a section only when it stands on its own |
| Progress or handoff log | Do not split. Prune to live state |
| Content or evidence — draft, material, source map | Leave the structure alone. Treat duplication as a content question |
| Reference or appendix | Remove the duplication and keep one owner |

- Treat splitting as a last resort. Consolidating in place and leaving a file alone both give a correct result.

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

## Bullets

- No paragraphs. Every statement is a bullet, a table row, or a heading.
- One bullet makes one contribution.
  - If it carries a second, split it and nest the second under it.
  - Split any bullet long enough to hide two claims.
- Nest every bullet under a parent that states the claim they share.
  - A flat list of unrelated items is a set of sections, not a list.
- Four levels is the working limit. Past that, use a table or a subheading.
- Use the fewest words that keep the meaning unambiguous.

## Cut criteria

- A line must say something the reader could not infer. Cut a line on any of these criteria.

| Criterion | Example |
|---|---|
| Rarely needed | Reference a reader opens occasionally |
| Inert detail | Framework- or topic-specific detail that changes no behaviour |
| Vague | "Write clean code" |
| Overly obvious | "Do not introduce bugs" |
| Redundant | "Use TypeScript" in a TypeScript project |

## Anti-patterns

| Avoid | Instead |
|---|---|
| Defaulting to a split | Choose the remedy by type |
| Splitting a file during a subtask | Refactor the file when the user asks |
| Optimising a line-count target | Judge by what the reader needs |
| A paragraph where a bullet would do | One bullet, one contribution |
| A bullet carrying two claims | Split and nest |
| A flat list of entries that differ in kind | Divide the list into sections |
| A flat list of unrelated items | Nest the items under the claim they share |
| A heading that promises what the section does not hold | Write the heading the section earns |
| A README restating its `SKILL.md` | Point to the skill |
| Padding a vague line with words | Cut the line instead |
