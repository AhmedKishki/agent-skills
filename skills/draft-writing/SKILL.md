---
name: draft-writing
description: Develop a source-grounded article through a thesis, section-and-passage plan, source mapping, white-box synthesis, section drafts and footnotes. Use when planning, researching, drafting or revising an article with its author.
---

# Draft writing

The user decides the article's claims, structure, wording and final form. Use this layout for new projects. Do not migrate an existing project unless the user requests it; follow its established file ownership meanwhile.

## Rules

- Obtain approval of the exact substantive proposal before saving it. Ask one focused question when wording, evidence, placement or a connection is unclear.
- Form claims, connections and prose through [white-box synthesis](references/white-box-synthesis.md). Approval does not change authorship or evidence limits.
- Check user claims against sources. Explain unsupported claims and contradictions with exact evidence; stop only affected work. Do not present a user interpretation as a source finding.
- Preserve direct user edits and review affected uses. Keep one current owner for each function; use Git for history.
- Use short, direct language and simple Markdown. Omit empty fields, repeated rules and completed process logs. Give output Markdown files only `name` and `description` frontmatter, with the filename as `name`.

## Workflow

1. Read the [thesis](references/thesis.md) and current [progress](references/progress.md).
2. Develop the [plan](references/plan.md): sections divided into passages, each with a purpose tied to the thesis.
3. [Map sources](references/source-mapping.md) that answer the passage's evidence needs, including counterevidence.
4. Route exact user wording to its passage and propose white-box synthesis with a full construction record.
5. Save approved synthesis directly in `material-section-n.md`. Do not create an intermediate argument record or general material store.
6. [Draft](references/drafting.md) each section from its material; revise its prose and check its footnotes with the user.
7. Update the short handoff. Return to the thesis or plan when evidence or drafting exposes a problem.

## Files

- `{project}-thesis.md`: aim, thesis, orientation and article-wide requirements.
- `{project}-plan.md`: section and passage purposes, order and connections.
- `sources/source-maps/{project}-source-map-{code}-{author-title}.md`: approved exact excerpts and locators.
- `material-section-n.md`: section passages, exact local inputs, basis, provenance and live limits.
- `draft-section-n.md`: reader-facing section prose and footnotes.
- `{project}-draft.md`: combined sections, assembled only on request without new prose.
- `{project}-progress.md`: current task, next action, blockers and counters.

Resolve the project name from the user's project; ask if unclear. Create files only when needed. Do not create separate arguments, general material or user-wording files. Keep article-specific research settings and citation style in the thesis, not in this skill.
