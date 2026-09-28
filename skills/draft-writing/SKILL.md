---
name: draft-writing
description: Develop an author-led, source-grounded article in isolated sections, using white-box synthesis, approved AI gap text and collaborative smoothing. Use when planning, researching, drafting or revising an article with its author.
---
# Draft writing

The user decides the thesis, claims, structure, wording and final form. Explain evidence and alternatives; never decide those matters on the user's behalf.

Use this layout for new projects. Do not migrate an existing project unless the user requests it. In an existing project, follow its established owners, identifiers and provenance restrictions; do not create parallel files or silently relax its restrictions on AI material. A migration needs separate approval of content moves, ownership changes and reference repairs.

## Files

Resolve the article root; ask if ambiguous. Create files only when needed, not empty section sets. Use these unprefixed filenames:

```text
<article-root>/
  thesis-and-vision.md
  requirements.md
  plan.md
  sections/
    section-n/
      arc-section-n.md
      progress-section-n.md
      material-section-n.md
      draft-section-n.md
  sources/
    source-maps/
      <author-title>.md
  draft.md                   # Assembly only on explicit request
```

Sections share source maps and article-wide direction only. Do not copy or reference another section's user inputs, material or draft as synthesis inputs. Each section develops its own synthesis. A source correction may require inspecting affected uses, not borrowing their prose.

Working Markdown files have only `name` and `description` frontmatter; `name` equals the filename. Use one H1, plain headings, flat lists, exact quotation blocks and relative links. Omit empty fields. Do not create general material, global progress, separate arguments or user-wording stores. Keep project-specific theory, citation style and research settings out of this skill.

## Read By Task

Read the governing project rules first. Load the relevant modules below, not the full reference library or release changelog.

| Task | Module |
|---|---|
| Route a prompt or direct user edit | [User prompts](references/rules/user-prompts.md) |
| Propose a substantive decision or wording | [Decisions and author authority](references/rules/decisions.md) |
| Define or revise motivation, theory and thesis | [Thesis and vision](references/article/thesis-and-vision.md) |
| Set tone, style, citations or research requirements | [Requirements](references/article/requirements.md) |
| Order article sections or choose drafting sequence | [Article plan](references/article/plan.md) |
| Develop a section's argument and passage order | [Section arc](references/section/arc.md) |
| Resume, pause, record a blocker or allocate local IDs | [Section progress](references/section/progress.md) |
| Research or verify a quotation | [Source maps](references/supplement/source-maps.md) |
| Preserve local wording or save approved synthesis | [Section material](references/section/material.md) |
| Construct prose from eligible inputs | [White-box synthesis](references/tools/white-box-synthesis.md) |
| Combine paragraphs or reduce repetition | [Smoothing](references/tools/smoothing.md) |
| Resolve a gap with explicitly requested AI wording | [AI-authored gap filling](references/tools/ai-authored.md) |
| Insert prose, check notes or assemble sections | [Section draft](references/section/draft.md) |
| Replace content, remove resolved work or end a session | [Retention](references/rules/retention.md) |

## Section Loop

1. Read the three article files if present. Use the section named by the user, otherwise the current-section link in `plan.md`. Ask if neither identifies the section; do not scan every section to infer a resume point.
2. Read that section's progress and arc, then only the local material, draft passages and shared excerpts needed for the current task. Route the prompt and settle one decision at a time.
3. Identify the passage's purpose and missing wording or evidence. Map and approve necessary source excerpts; retrieval alone is not an eligible input.
4. Use white-box as the basis for synthesis. Show the exact passage and full construction record for approval. Save approved material; propose draft insertion separately. AI gap text follows its own request, marking and approval procedure, never white-box reuse.
5. Smooth the section one amendment at a time and verify affected footnotes. Ask for section review before drafting the next unless the user chooses later review.
6. Update local progress after a decision, save, blocker or focus change. Change the article's current-section link only when focus changes. Retain the exact next action, not a session narrative.
