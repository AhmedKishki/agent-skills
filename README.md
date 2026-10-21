# Agent Skills

Skills for Claude Code and Kilo Code. Each skill is a folder in `skills/` with a `SKILL.md`.

## Install

### Claude Code marketplace: choose individual skills

Run these commands in your shell:

```sh
claude plugin marketplace add AhmedKishki/agent-skills
claude plugin install coding-partner@ahmedkishki-skills
```

The repository provides one root marketplace, `ahmedkishki-skills`, with one independently installable plugin per skill. Replace `coding-partner` with any name in the table below. Each plugin explicitly discovers its root `SKILL.md` through `"skills": ["./"]`; there are no nested marketplaces.

Start a new Claude Code session or run `/reload-plugins` after installation. Invoke the example as `/coding-partner:coding-partner`.

### Local checkout: link every skill for Claude Code and Kilo Code

```sh
git clone https://github.com/AhmedKishki/agent-skills.git ~/agent-skills
~/agent-skills/bin/agent-skills install
```

This links every skill into `~/.claude/skills`, where Claude Code finds it; an older copy already there is moved to `~/.claude/skill-backups/`. For Kilo Code, add `~/.claude/skills` to `skills.paths` in `~/.config/kilo/kilo.jsonc`.

Choose marketplace installation or local linking for a given skill to avoid loading two copies. The link, update and editing commands below apply to the local-checkout route.

## Use in a project

```sh
cd path/to/project
agent-skills link
```

The project gets an `agent-skills` link to the collection, which its Git ignores, so you can open and edit the skills from your workspace.

## Update

For marketplace installs, refresh the catalog and update each installed plugin:

```sh
claude plugin marketplace update ahmedkishki-skills
claude plugin update coding-partner@ahmedkishki-skills
```

Replace `coding-partner` with the installed skill's name. Start a new session or run `/reload-plugins` to load the update.

For a local checkout:

```sh
agent-skills update
```

This pulls the latest skills and pushes your local commits. Local changes you have not committed stay local and are listed. If your branch and the remote have diverged, or the merge would overwrite your local changes, nothing changes and the command shows how to resolve it with git.

## Change a skill

Edit it in `~/agent-skills/skills/` or through a project's link, commit, then run `agent-skills update` to push it. Other machines get the change with their next `agent-skills update`.

## Skills

| Skill | Purpose |
|---|---|
| [`active-objects`](skills/active-objects/) | Design and review event-driven code built from active objects: private state, queue-only communication and run-to-completion handlers. |
| [`coding-partner`](skills/coding-partner/) | Explain code chunk by chunk and collaboratively engineer minimal, readable code under user-defined constraints. |
| [`collaborative-coding`](skills/collaborative-coding/) | Work through a shared task list with user-approved code patches and Beginner, Standard, or Expert explanations. |
| [`collaborative-learning`](skills/collaborative-learning/) | Conduct collaborative, source-grounded learning with a confirmed plan and Markdown records of explanations and discussion. |
| [`draft-writing`](skills/draft-writing/) | Author-led, source-grounded drafting in isolated sections, using white-box synthesis, approved AI gap text and collaborative smoothing. |
| [`human-writing`](skills/human-writing/) | Write and check prose by justifying every sentence's logical connection to its part and surrounding sentences. |
| [`humaniser`](skills/humaniser/) | Find repeated or unclear Markdown prose using a semantic checklist. |
| [`markdown-refactor`](skills/markdown-refactor/) | Make agent-facing Markdown do its job sufficiently, with one owner per type of information and one meta view. |
| [`read-along-guide`](skills/read-along-guide/) | Build book companions with verified quotations, diagrams, linked definitions and PDF output. |
| [`scheduled-learning`](skills/scheduled-learning/) | Study a source section by section across manual or automated runs, with source-faithful explanations and a persistent progress file. |
| [`white-box-synthesis`](skills/white-box-synthesis/) | Answer a query only from supplied sources, with marked AI-authored connections, references and provenance on request. |
| [`write-like-me`](skills/write-like-me/) | Write, rewrite, or audit prose using an evidence-backed personal writing pattern. Upstream skill files from [HopLittleBunny/write-like-me](https://github.com/HopLittleBunny/write-like-me). |
