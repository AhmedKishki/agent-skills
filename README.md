# Agent Skills

A collection of skills for Claude and Kilo Code, also usable from Codex. Every skill lives in this one repository, in `skills/<name>/` with a `SKILL.md` entry point. `bin/agent-skills` installs the collection once per machine, links it into projects and updates it.

## Available skills

| Skill | Purpose |
|---|---|
| [`active-objects`](skills/active-objects/) | Design and review event-driven code built from active objects: private state, queue-only communication and run-to-completion handlers. |
| [`coding-partner`](skills/coding-partner/) | Explain code chunk by chunk and collaboratively engineer minimal, readable code under user-defined constraints. |
| [`collaborative-coding`](skills/collaborative-coding/) | Work through a shared task list with user-approved code patches and Beginner, Standard, or Expert explanations. |
| [`collaborative-learning`](skills/collaborative-learning/) | Conduct collaborative, source-grounded learning with a confirmed plan and Markdown records of explanations and discussion. |
| [`draft-writing`](skills/draft-writing/) | Author-led, source-grounded drafting in isolated sections, using white-box synthesis, approved AI gap text and collaborative smoothing. |
| [`humaniser`](skills/humaniser/) | Find repeated or unclear Markdown prose using a semantic checklist. |
| [`markdown-refactor`](skills/markdown-refactor/) | Make agent-facing Markdown do its job sufficiently, with one owner per type of information and one meta view. |
| [`read-along-guide`](skills/read-along-guide/) | Build book companions with verified quotations, diagrams, linked definitions and PDF output. |
| [`white-box-synthesis`](skills/white-box-synthesis/) | Answer a query only from supplied sources, with marked AI-authored connections, references and provenance on request. |
| [`write-like-me`](skills/write-like-me/) | Write, rewrite, or audit prose using an evidence-backed personal writing pattern. Upstream skill files from [HopLittleBunny/write-like-me](https://github.com/HopLittleBunny/write-like-me). |

## Install (Linux)

Clone the collection to `~/agent-skills` and install it:

```sh
git clone https://github.com/AhmedKishki/agent-skills.git ~/agent-skills
~/agent-skills/bin/agent-skills install
```

`install` does two things:

- links `~/.local/bin/agent-skills` to the command, so it runs from anywhere;
- links every skill into `~/.claude/skills/<name>`, where Claude Code loads personal skills. Anything already there under a skill's name, such as an older copy, is moved to `~/.claude/skill-backups/<time>/`.

Kilo Code loads the same folder once `~/.config/kilo/kilo.jsonc` lists it; `install` says so when it does not:

```jsonc
"skills": { "paths": ["/home/<user>/.claude/skills"] }
```

Load each skill through these links only. A skill also installed as a Claude plugin, or copied into a project's `.claude/skills`, `.kilo/skills` or `.agents/skills`, loads a second time.

## Use it in a project

Inside a project, link the checkout so its skills can be opened, referenced and edited from that workspace:

```sh
agent-skills link            # or: agent-skills link path/to/project
```

This creates `./agent-skills`, a symlink to `~/agent-skills`, and adds `/agent-skills` to the project's `.git/info/exclude`, which Git never commits. The project's own files stay untouched, and no agent loads the skills from this path, so nothing loads twice. Every project shares the one checkout: an edit made through any project's link is the same edit everywhere.

## Updates

Bring the checkout up to date from a terminal:

```sh
agent-skills update
```

An update only fast-forwards:

- local edits are kept, as long as the update does not change the same files;
- if it would, or if the checkout has commits that origin lacks, nothing changes and the update says why;
- after pulling, links are added for new skills and removed for deleted ones.

An edit reaches another machine once it is committed and pushed and `agent-skills update` runs on that machine; the update itself never commits or pushes.

## Other hosts

### Codex

Codex discovers personal skills in `~/.agents/skills` and supports symlinked skill directories:

```sh
mkdir -p ~/.agents/skills
ln -s ~/agent-skills/skills/draft-writing ~/.agents/skills/draft-writing
```

Invoke a skill with `$draft-writing`, or describe a matching task. See the [official Codex skill documentation](https://developers.openai.com/codex/skills).

### Claude plugin marketplace

This repository is also a Claude plugin marketplace named `ahmedkishki-skills`, for installing single skills without a checkout. Each entry points at its skill's directory in this repository:

```text
/plugin marketplace add AhmedKishki/agent-skills
/plugin install draft-writing@ahmedkishki-skills
```

Use either the marketplace or `agent-skills install` on a machine, not both. A public repository works for personal marketplaces and Claude Code. Organization-managed GitHub sync requires the marketplace repository to be private or internal, and organization owners trigger **Update** manually for each release. See [Anthropic's plugin marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces).

### Claude.ai skill upload

Download a skill's ZIP asset from its release and upload it under **Settings → Features**. Use the per-skill asset, not GitHub's source archive, so the ZIP has `<name>/SKILL.md` at the required depth. See [Anthropic's skill documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

## Codex and Claude compatibility

The portable workflow follows the open [Agent Skills specification](https://agentskills.io/specification): instructions live in `SKILL.md`, and supporting files use relative links. OpenAI-specific presentation metadata is isolated in `agents/openai.yaml`; Claude plugin metadata is isolated in `.claude-plugin/`. Each host ignores the other's metadata. Host behaviour can differ, so every release should validate the skill and test its main workflow in each host it targets.

## Versions and releases

A skill may carry a `version` file whose single line is its current version (for example `7.3.0`), updated in the same commit that ships the change. The release marker is an immutable annotated tag in this repository named `<name>-vMAJOR.MINOR.PATCH`, such as `draft-writing-v10.0.0`; the `version` file records the same number for readability and tooling. Record user-visible changes in the skill's changelog.

- Commits on `main` are unreleased development state.
- Plugin manifests and marketplace entries omit a plugin `version` deliberately: Git-backed installs use the resolved commit, so `claude plugin validate --strict` reports the missing version as a warning.
- Each release tag has a matching GitHub Release whose notes summarize the changelog entry and which attaches one ZIP with exactly one top-level skill directory.
- `PATCH` fixes compatible behaviour, `MINOR` adds compatible behaviour, and `MAJOR` changes a workflow or persisted format incompatibly.

Find a skill's latest release in a checkout:

```sh
git describe --tags --match 'draft-writing-v*' --abbrev=0
```

Workflow-schema labels such as `v6 → v7` inside migration instructions describe persisted project-file compatibility; they are not package release versions.

## Publishing updates

1. Make a focused change in the skill's directory and keep the skill self-contained.
2. Validate its structure, linked resources and Claude metadata with `claude plugin validate . --strict`.
3. Test the changed workflow in the hosts it targets.
4. Update the skill's changelog with user-visible changes and any migration or breaking change.
5. Commit and push to `main`; `agent-skills update` brings it to the other machines.
6. For a release, create and push the annotated `<name>-vX.Y.Z` tag, build the per-skill ZIP and publish the matching GitHub Release.
