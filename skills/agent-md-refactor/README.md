# Agent markdown refactor

Refactors bloated agent-generated markdown using progressive disclosure, with a remedy chosen by file type and a mandatory audit proving nothing was lost.

## When to use

- "refactor my `AGENTS.md` / `CLAUDE.md`"
- "my skill file is too long" / "split my instructions"
- "this progress log keeps growing" / "prune my handoff"
- "my plan doc is a mess" / "my README duplicates the skill"
- Any markdown an agent reads or maintains that mixes concerns, duplicates rules, contradicts itself, or carries superseded state

## The problem

Agent-generated markdown accumulates bloat in recognisable ways: rules restated in two places, reference material crowding out rules, append-only logs that never shrink, and skills whose README restates their own body. Every task pays for the whole file.

## The six phases

1. **Identify the type** (Phase 0) — instruction file, skill, plan, log, content/evidence, or reference. The type decides the remedy; the wrong remedy causes damage.
2. **Find contradictions** — surface conflicts for the user to resolve, never pick a winner.
3. **Identify the essentials** — keep what every task needs; move what only some tasks need.
4. **Choose the remedy** — consolidate in place, split into linked files, prune to live state, dedupe against an existing owner, or leave alone.
5. **Apply** — same tone, same frontmatter conventions, simple Markdown.
6. **Flag for deletion** — report; never delete silently.

## What makes it general

| Type | Correct remedy |
|---|---|
| Instruction file | Merge duplicate rules; extract reference only if nothing cites it by name |
| Skill | Body stays procedural; deep reference moves to linked files; README stays short |
| Plan / spec | Usually leave whole; split only independent sections |
| Progress / handoff log | **Do not split.** Prune to live state — Git holds the history |
| Content / evidence | Leave structure alone; duplication is a content question |
| Reference / appendix | Dedupe against the canonical owner and link to it |

**Splitting is a last resort.** Consolidating in place is often the correct answer, and so is leaving a file alone. A refactor that other documents cite by name must stay whole, or its citations break.

## Verification

The part that makes it trustworthy: capture a baseline, enumerate the file's content units as a checklist, re-check each unit after editing, confirm every deletion was intended, and report lines, words and percentage change. If a refactor did not measurably reduce size, say so and explain why — "everything here is load-bearing" is a valid finding, an inflated success claim is not.

## Anti-patterns

Defaulting to a split; chasing a line-count target; a README that duplicates its `SKILL.md`; growing a log forever; silent deletion; claiming success without measuring.

## Details

Full phases, tables and the execution checklist: [SKILL.md](SKILL.md).

## License

MIT
