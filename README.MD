# Agent Skills

A collection of source-controlled skills for Codex and Claude. Each top-level directory is a self-contained skill with a `SKILL.md` entry point and any supporting references, scripts, or assets.

## Available skills

| Skill | Purpose |
|---|---|
| [`draft-writing`](draft-writing/) | User-led, source-grounded research and drafting through a canonical thesis-to-draft workflow of callable functions. |

## Install

Use a tagged [GitHub Release](https://github.com/AhmedKishki/agent-skills/releases) for reproducible work. Use `main` only when you intentionally want the current development state.

```sh
git clone https://github.com/AhmedKishki/agent-skills.git
cd agent-skills
git checkout "draft-writing-vX.Y.Z"
```

Replace the example tag with a published release tag.

### Codex

Codex discovers personal skills in `~/.agents/skills` and supports symlinked skill directories.

```sh
mkdir -p ~/.agents/skills
ln -s "$PWD/draft-writing" ~/.agents/skills/draft-writing
```

Invoke the skill with `$draft-writing`, or describe a task that matches it. See the [official Codex skill documentation](https://developers.openai.com/codex/skills).

### Claude plugin marketplace

This repository is a Claude plugin marketplace named `ahmedkishki-skills`. In Claude, open **Customize → Plugins → Personal plugins**, select **Add marketplace**, add `https://github.com/AhmedKishki/agent-skills`, and install **Draft Writing**. This interface follows the repository's default branch, so use it after released changes have been merged to `main`.

For a reproducible Claude Code installation, pin the marketplace checkout to a published tag:

```text
/plugin marketplace add AhmedKishki/agent-skills@draft-writing-vX.Y.Z
/plugin install draft-writing@ahmedkishki-skills
```

Replace the example tag with a published release tag. To test the current development state instead, omit the `@draft-writing-vX.Y.Z` suffix:

```text
/plugin marketplace add AhmedKishki/agent-skills
/plugin install draft-writing@ahmedkishki-skills
```

Claude can invoke the installed skill automatically. In Claude Code, invoke it directly as `/draft-writing:draft-writing`.

A public repository works for personal marketplaces and Claude Code. Organization-managed GitHub sync requires the marketplace repository to be private or internal. Under this repository's Git-derived version policy, organization owners should trigger **Update** manually for each release; Anthropic's automatic organization sync currently requires an explicit plugin-version bump. See [Anthropic's plugin marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces).

### Standalone Claude installation

Claude Code also discovers personal skills in `~/.claude/skills`; a project can instead place the directory at `.claude/skills/draft-writing`.

```sh
mkdir -p ~/.claude/skills
ln -s "$PWD/draft-writing" ~/.claude/skills/draft-writing
```

Invoke this standalone installation with `/draft-writing`, or describe a matching task. See the [official Claude Code skill documentation](https://code.claude.com/docs/en/skills).

If symlinks are unavailable, copy the complete skill directory. Keep `SKILL.md` and its linked directories together.

#### Claude.ai skill upload

Download the dedicated `draft-writing.zip` asset from a release and upload it under **Settings → Features**. Use the per-skill asset, not GitHub's repository source archive, so the ZIP has `draft-writing/SKILL.md` at the required depth. See [Anthropic's skill documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

## Codex and Claude compatibility

The portable workflow follows the open [Agent Skills specification](https://agentskills.io/specification): instructions live in `SKILL.md`, and supporting files use relative links. OpenAI-specific presentation metadata is isolated in `agents/openai.yaml`; Claude marketplace metadata is isolated in `.claude-plugin/`. Each host ignores the other's metadata. Host behavior can differ, so every release should validate the skill and test its main workflow in both Codex and Claude.

## Versions and releases

Git is the sole source of release-version truth. Do not add a `VERSION` file, a hand-maintained changelog, or a release number inside a skill.

- Commits on `main` are unreleased development state.
- Published skill versions use immutable annotated tags named `<skill-name>-vMAJOR.MINOR.PATCH` and a matching GitHub Release.
- The Claude marketplace entry omits a plugin `version` deliberately: Git-backed installs use the resolved commit, while a release-tag pin supplies the immutable version.
- Release notes are the changelog. They identify affected skills, user-visible changes, migrations or breaking changes, and Codex/Claude compatibility results.
- Each release attaches a ZIP for every released skill, with exactly one top-level skill directory.
- `PATCH` fixes compatible behavior, `MINOR` adds compatible behavior, and `MAJOR` changes a workflow or persisted format incompatibly.

Inspect a checkout without duplicating its version in tracked files:

```sh
git describe --tags --match 'draft-writing-v*' --always --dirty
```

Workflow-schema labels such as `v6 → v7` inside migration instructions describe persisted project-file compatibility; they are not package release versions.

## Publishing future updates

1. Make a focused change and keep each skill self-contained.
2. Validate its structure, linked resources, observable behavior, and Claude marketplace metadata with `claude plugin validate . --strict`.
3. Test the changed workflow in Codex and Claude.
4. Document any migration or breaking change in the release notes.
5. Merge the reviewed change to `main`.
6. Create and push an annotated skill-scoped tag, build the per-skill ZIP, and publish the matching GitHub Release.

Future updates may refine existing skills or add new top-level skill directories. They should keep canonical state lean, preserve host-portable instructions, and announce compatibility or migration requirements before users upgrade.
