---
name: "agent-md-refactor"
description: Refactor bloated agent-generated markdown of any kind — instruction files, skills, plans, progress logs, reference material, drafts — using progressive disclosure, type-appropriate remedies and a no-content-lost audit. Use when a markdown file that agents read or maintain has grown long, mixes unrelated concerns, duplicates rules, contradicts itself, or repeats superseded state.
---

# Agent markdown refactor

Agent-generated markdown accumulates bloat in specific, recognisable ways: rules get restated in two places, reference material crowds out rules, append-only logs never shrink, and skills grow a README that duplicates their own body. Each kind needs a different remedy, so the first step is always to identify what kind of file is being refactored.

This skill generalises progressive disclosure beyond instruction files. It applies to any markdown that an agent reads, writes or maintains.

## When to use

Any markdown an agent reads, writes or maintains that has grown long, mixes unrelated concerns, duplicates rules, contradicts itself, or carries superseded state. Common requests: "refactor my `AGENTS.md`", "my skill file is too long", "this progress log keeps growing", "my README duplicates the skill", "my plan doc is a mess".

## Phase 0: Identify the type

Determine the file's type before proposing anything. The type decides the remedy, and applying the wrong one causes damage.

| Type | Examples | Bloat symptom | Correct remedy |
|---|---|---|---|
| **Instruction / context** | `AGENTS.md`, `CLAUDE.md`, `COPILOT.md`, `.cursorrules` | Loaded on every task; reference material competes with rules | Merge duplicate rules; extract reference material **only if** nothing cites the file by name |
| **Skill definition** | `SKILL.md` + `references/` | `SKILL.md` carries deep reference that is only read sometimes | Keep the body procedural; move deep reference to linked files; keep the README short |
| **Plan / spec** | plan, design doc, requirements | Sections sprawl past the document's own scope | Usually leave whole. Split only where a section has independent coherence |
| **Progress / handoff log** | progress files, session logs, changelogs | Append-only; completed and superseded entries never removed | **Do not split.** Prune to live state; Git preserves the history |
| **Content / evidence** | drafts, material, source maps, notes | Already section-isolated; duplication is a provenance question, not a structure one | Leave structure alone. Fix duplication at the content level |
| **Reference / appendix** | `references/*.md`, glossaries | Duplicated across files after copies diverged | Dedupe; keep one owner and link to it |

**Splitting is a last resort, not a default.** A single-file consolidation is a valid and often correct outcome.

**Check who cites the file.** Before moving or renaming anything, search the repository for references to it by name. If other files, skills, or a governing rules document name it, splitting or renaming breaks those citations, and the user must choose whether to update them.

## Phase 1: Find contradictions

Identify instructions that conflict with each other before restructuring. Examples: contradictory style guidance, incompatible workflow orders, mutually exclusive tool preferences.

Report each conflict as a question for the user to resolve. Do not pick a winner. Many apparent conflicts are already reconciled elsewhere in the file — re-read the surrounding sections before raising one.

## Phase 2: Identify the essentials

Extract what belongs where, judged by how often a reader needs it.

**Keep in the root:**
- One-sentence purpose
- Commands, paths, or identifiers that are non-obvious and load-bearing
- Rules that apply to every task
- Critical overrides of default behaviour
- Links to the detail

**Move or cut:**
- Reference material needed only sometimes
- Language-, framework- or topic-specific conventions
- Material that already has another canonical owner
- Completed or superseded state in append-only files

## Phase 3: Choose the remedy

Pick by type, from the Phase 0 table. State the choice and its trade-off rather than assuming the split. Typical outcomes:

- **Consolidate in place** — merge duplicates, tighten prose, keep one file. The right choice when citations point at the file or when the document is a single governing source.
- **Split into linked files** — when the root is read on every task but most content is not, and no citation prevents it.
- **Prune to live state** — for logs. Delete or compress completed entries; do not archive them into new files, because Git already holds them.
- **Dedupe against an existing owner** — point at the canonical file instead of restating its content.
- **Leave alone** — a legitimate and frequent answer. Say so rather than manufacturing work.

Aim for 3–8 linked files when splitting. Fewer is better; more is navigation overhead.

## Phase 4: Apply

- Keep the existing tone, formatting and frontmatter conventions. A refactor changes structure, not voice.
- Use simple Markdown: short direct sentences, no repeated boilerplate, no completed process logs in a document meant to be read going forward.
- Give output Markdown files only `name` and `description` frontmatter, with the filename as `name`.
- Locate every edit by content and assert it before writing.

## Phase 5: Flag for deletion

Identify content that should go entirely. Report it; do not delete silently.

| Criterion | Example | Why cut |
|---|---|---|
| Redundant | "Use TypeScript" in a TypeScript project | Agent already knows |
| Too vague | "Write clean code" | Not actionable |
| Overly obvious | "Don't introduce bugs" | Wastes context |
| Default behaviour | "Use descriptive names" | Standard practice |
| Outdated | References a removed command or file | No longer applies |
| Already owned elsewhere | Restating a rule that has a canonical home | Two copies drift apart |
| Superseded state | A resolved decision, a finished task | Append-only drift |

## Verification: no content lost

This is the step that makes a refactor trustworthy, and it is mandatory. Structure changes are easy to eyeball and easy to get subtly wrong.

1. **Capture a baseline** before editing — word and line counts, plus the list of sections.
2. **Enumerate the content units** the file carries, as a checklist: each rule, each owner, each command, each override, each exception.
3. **After editing, re-check every unit** by searching for a distinctive phrase from it, in the new file.
4. **Confirm the removals are intended** — that each deleted line is a duplicate, a merge target, or a flagged deletion, and not an accident.
5. **Verify links and references** resolve, and that citations to the refactored file still point at something real.
6. **State the result numerically** — lines, words, and percentage change. If a refactor did not measurably reduce size, say so plainly rather than describing it as a cleanup.

Report honestly: if the reduction is small, say the reason. "Everything here is load-bearing" is a legitimate finding; an inflated claim of success is not.

## Anti-patterns

| Avoid | Why | Instead |
|---|---|---|
| Defaulting to a split | Breaks citations, fragments a single source of truth | Choose the remedy by file type |
| Prescribing a line target as a goal | Optimises the metric, not the document | Judge by what a reader needs per task |
| Restating a skill's body in its README | The README becomes a second copy that drifts | Short README: purpose, usage, license |
| Keeping a README that duplicates `SKILL.md` | Two copies, two futures | Point to the skill |
| Growing a log forever | History is Git's job | Prune to live state |
| Silent deletion | Irreversible, and hides judgement | Flag, then delete on approval |
| Claiming success without measuring | Unverifiable | Report counts and percentage |
| Splitting during a subtask | Scope creep | Refactor when asked |

## Execution checklist

- [ ] Phase 0: type identified; citing references found
- [ ] Phase 1: contradictions surfaced and resolved by the user
- [ ] Phase 2: essentials separated from reference material
- [ ] Phase 3: remedy chosen by type, with trade-offs stated
- [ ] Phase 4: applied, tone and conventions preserved
- [ ] Phase 5: deletions flagged, not silent
- [ ] Verification: every content unit re-checked; counts and percentage reported
- [ ] Submodule changes committed and pushed before the parent pointer, if the skill lives in one
