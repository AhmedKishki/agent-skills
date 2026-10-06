# Agent Skills

A collection of skills for Codex and Claude. Each skill is its own Git repository, included here as a submodule under `skills/` with a `SKILL.md` entry point.

## Available skills

| Skill | Repository | Purpose |
|---|---|---|
| [`collaborative-learning`](skills/collaborative-learning/) | [collaborative-learning-skill](https://github.com/AhmedKishki/collaborative-learning-skill) | Conduct collaborative, source-grounded learning with a confirmed plan and Markdown records of explanations and discussion. |
| [`draft-writing`](skills/draft-writing/) | [draft-writing-skill](https://github.com/AhmedKishki/draft-writing-skill) | Author-led, source-grounded drafting in isolated sections, using white-box synthesis, approved AI gap text and collaborative smoothing. |
| [`humaniser`](skills/humaniser/) | [humaniser-skill](https://github.com/AhmedKishki/humaniser-skill) | Find repeated or unclear Markdown prose using a semantic checklist. |
| [`markdown-refactor`](skills/markdown-refactor/) | [markdown-refactor-skill](https://github.com/AhmedKishki/markdown-refactor-skill) | Make agent-facing Markdown do its job sufficiently, with one owner per type of information and one meta view. |
| [`write-like-me`](skills/write-like-me/) | [write-like-me-skill](https://github.com/AhmedKishki/write-like-me-skill) | Write, rewrite, or audit prose using an evidence-backed personal writing pattern. Upstream skill files from [HopLittleBunny/write-like-me](https://github.com/HopLittleBunny/write-like-me). |

## Install

Clone the collection with its submodules:

```sh
git clone --recurse-submodules https://github.com/AhmedKishki/agent-skills.git
cd agent-skills
```

Each skill is released in its own repository. Pin a skill to one of its own tags inside its submodule:

```sh
git -C skills/draft-writing fetch --tags
git -C skills/draft-writing checkout "vX.Y.Z"
```

Replace the example tag with a published release tag from that skill's repository.

`skills/write-like-me/` includes the upstream skill entry point, its references, runtime scripts, agent metadata, and license. No upstream installer is required.

### Codex

Codex discovers personal skills in `~/.agents/skills` and supports symlinked skill directories.

```sh
mkdir -p ~/.agents/skills
ln -s "$PWD/skills/draft-writing" ~/.agents/skills/draft-writing
ln -s "$PWD/skills/write-like-me" ~/.agents/skills/write-like-me
```

Invoke the skills with `$draft-writing` or `$write-like-me`, or describe a matching task. See the [official Codex skill documentation](https://developers.openai.com/codex/skills).

### Claude plugin marketplace

This repository is a Claude plugin marketplace named `ahmedkishki-skills`. Each entry points directly at the skill's own repository, so the submodules do not need to be initialised for an install. In Claude, open **Customize → Plugins → Personal plugins**, select **Add marketplace**, add `https://github.com/AhmedKishki/agent-skills`, and install the skills you want:

```text
/plugin marketplace add AhmedKishki/agent-skills
/plugin install draft-writing@ahmedkishki-skills
/plugin install write-like-me@ahmedkishki-skills
```

The marketplace entries follow each skill repository's default branch. To reproduce an exact version, pin the skill's repository and tag in the marketplace entry's `source` (`ref`), or check out that tag in the submodule.

A public repository works for personal marketplaces and Claude Code. Organization-managed GitHub sync requires the marketplace repository to be private or internal. Under this repository's Git-derived version policy, organization owners should trigger **Update** manually for each release; Anthropic's automatic organization sync currently requires an explicit plugin-version bump. See [Anthropic's plugin marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces).

### Standalone Claude installation

Claude Code also discovers personal skills in `~/.claude/skills`; a project can instead place the directory at `.claude/skills/draft-writing`.

```sh
mkdir -p ~/.claude/skills
ln -s "$PWD/skills/draft-writing" ~/.claude/skills/draft-writing
ln -s "$PWD/skills/write-like-me" ~/.claude/skills/write-like-me
```

Invoke these standalone installations with `/draft-writing` or `/write-like-me`, or describe a matching task. See the [official Claude Code skill documentation](https://code.claude.com/docs/en/skills).

If symlinks are unavailable, copy the complete skill directory. Keep `SKILL.md` and its linked directories together.

#### Claude.ai skill upload

Download the dedicated `draft-writing.zip` asset from a release and upload it under **Settings → Features**. Use the per-skill asset, not GitHub's repository source archive, so the ZIP has `draft-writing/SKILL.md` at the required depth. See [Anthropic's skill documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

## Codex and Claude compatibility

The portable workflow follows the open [Agent Skills specification](https://agentskills.io/specification): instructions live in `SKILL.md`, and supporting files use relative links. OpenAI-specific presentation metadata is isolated in `agents/openai.yaml`; Claude marketplace metadata is isolated in `.claude-plugin/`. Each host ignores the other's metadata. Host behavior can differ, so every release should validate the skill and test its main workflow in both Codex and Claude.

## Versions and releases

Each skill repository may carry a `version` file (for example `draft-writing/version`) whose single line is the current version string (for example `7.3.0`), updated in the same commit that ships the change. The immutable annotated tag `vMAJOR.MINOR.PATCH` in that skill's repository is the release marker; the `version` file records that same number for readability and tooling, not a second source of truth. Record user-visible changes in the skill's changelog.

- Commits on a skill repository's `main` are unreleased development state.
- Published skill versions use immutable annotated tags named `vMAJOR.MINOR.PATCH` in the skill's own repository and a matching GitHub Release.
- The Claude marketplace entry omits a plugin `version` deliberately: Git-backed installs use the resolved commit, while a release-tag pin in the entry's `source` supplies the immutable version.
- Release notes summarize the corresponding changelog entry and add publication assets and compatibility results.
- Each release attaches a ZIP for the skill, with exactly one top-level skill directory.
- `PATCH` fixes compatible behavior, `MINOR` adds compatible behavior, and `MAJOR` changes a workflow or persisted format incompatibly.

Inspect a checkout (the tag remains the canonical version identifier; the `version` file mirrors it):

```sh
git describe --tags --match 'v*' --always --dirty
```

Workflow-schema labels such as `v6 → v7` inside migration instructions describe persisted project-file compatibility; they are not package release versions.

## Publishing future updates

1. Make a focused change in the skill's own repository and keep each skill self-contained.
2. Validate its structure, linked resources, observable behavior, and Claude marketplace metadata with `claude plugin validate . --strict`.
3. Test the changed workflow in Codex and Claude.
4. Update the skill's enduring changelog with user-visible changes and any migration or breaking change; derive release notes from that entry.
5. Merge the reviewed change to the skill repository's `main`.
6. Create and push an annotated tag in the skill repository, build the per-skill ZIP, and publish the matching GitHub Release.
7. Update the submodule pointer in this collection to the released commit.

Future updates may refine existing skills or add new skills as submodules. They should keep canonical state lean, preserve host-portable instructions, and announce compatibility or migration requirements before users upgrade.
