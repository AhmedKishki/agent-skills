# Agent Skills

Skills for Claude Code, Kilo Code and Cline. Each skill is a folder in `skills/` with a `SKILL.md`.

## Install

### Claude Code marketplace: choose individual skills

Run these commands in your shell:

```sh
claude plugin marketplace add AhmedKishki/agent-skills
claude plugin install coding-partner@ahmedkishki-skills
```

The repository provides one root marketplace, `ahmedkishki-skills`, with one independently installable plugin per skill. Replace `coding-partner` with any name in the table below. Each plugin explicitly discovers its root `SKILL.md` through `"skills": ["./"]`; there are no nested marketplaces.

Start a new Claude Code session or run `/reload-plugins` after installation. Invoke the example as `/coding-partner:coding-partner`.

### Local checkout: install every skill for all three agents

```sh
git clone https://github.com/AhmedKishki/agent-skills.git ~/agent-skills
~/agent-skills/bin/agent-skills install
```

The installer links every skill into each agent's global skill directory:

| Agent | Directory |
|---|---|
| Claude Code | `~/.claude/skills/` |
| Kilo Code | `~/.kilo/skills/` |
| Cline | `~/.cline/skills/` |

No agent configuration or marketplace registration is required. Restart or reload your agent to discover the skills. Existing Kilo `skills.paths` entries pointing to `~/.claude/skills` are no longer needed; the installer leaves them unchanged.

It installs the `agent-skills` command in `~/.local/bin` and warns if that directory is missing from `PATH`; it does not edit shell startup files. Keep the checkout in place because the command and skills link to it.

Same-name files, folders or foreign links are moved into unique backup directories under the affected agent's `skill-backups/` folder. Rerunning `install` is safe; unrelated skills remain untouched.

Choose marketplace installation or local linking for a given skill to avoid loading two copies. The project-link and editing commands below apply to the local-checkout route.

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

After Git succeeds, it synchronizes all three agents' links: newly added skills become available, existing skills use the updated checkout, and links owned by this checkout are removed when their skill disappears or loses its `SKILL.md`. Backups and unrelated skills are preserved. Rerunning `install` performs the same link synchronization without fetching or pushing Git commits.

It then refreshes the catalog if `ahmedkishki-skills` is already registered in Claude Code. Only this optional refresh requires `claude` and `python3` on PATH; otherwise it reports the skipped refresh and the manual command above. A failed lookup or refresh exits nonzero after the Git/link update, without rolling it back.

The refresh uses Claude's registered source and branch or tag, not necessarily this checkout. It never registers a marketplace or installs or enables plugins. Marketplace registration alone does not load every skill; use the individual plugin install and update commands above. Local linking and synced copies remain separate from the marketplace cache.

## Change a skill

Edit it in `~/agent-skills/skills/` or through a project's link, commit, then run `agent-skills update` to push it. Other machines get the change with their next `agent-skills update`.

To add a skill, create `skills/<name>/SKILL.md` and its supporting files, then run `agent-skills install` to link it locally. There is no hard-coded local skill list to update. Follow [AGENTS.md](AGENTS.md) for skill maintenance; Claude marketplace entries remain separate from local discovery.

## Skills

| Skill | Purpose |
|---|---|
| [`active-objects`](skills/active-objects/) | Design and review event-driven code built from active objects: private state, queue-only communication and run-to-completion handlers. |
| [`auto-jobber`](skills/auto-jobber/) | Retain qualifications, review English/German CVs, research employers and prepare CVs and cover letters in the applicant's own wording. |
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
| [`write-like-me`](skills/write-like-me/) | Write, rewrite, or audit prose using an evidence-backed personal writing pattern. |
