# Repository Instructions

Apply these rules when creating, editing, maintaining, or releasing skills in `agent-skills`. Honour the user's requested scope and established decisions.

## File responsibilities

- Keep each skill self-contained in its own directory, `skills/<skill-name>/`, with everything it needs inside it.
- Use `SKILL.md` for the operational workflow and routing to supporting files.
- Use `references/*.md` for detailed instructions needed during that workflow.
- Use the skill's `README.md` for a brief user-facing introduction and usage.
- Keep general creation, maintenance, editing, and release rules in this root `AGENTS.md`; do not embed them in a skill's operational instructions.
- Keep the root `README.md` to using the collection: install, link, update, changing a skill and the list of skills. Keep it consistent with `bin/agent-skills`.
- Give each instruction one canonical owner; avoid copying rules between files.
- Keep generated project records and temporary work outside skill directories.

## Create and edit

- Read the target skill and relevant references before making changes.
- Ask about unclear requirements or unspecified decisions that affect behaviour.
- Make only changes within the authorised task; preserve unrelated work.
- Use lowercase letters, digits, and hyphens for skill names and directory names.
- Give `SKILL.md` YAML frontmatter containing `name` and `description`.
- Describe the task and its triggering conditions clearly in `description`.
- Write direct instructions that another agent can execute.
- Keep each Markdown prose paragraph on one physical line; preserve code blocks, tables and list structure.
- Give each third-party credit one owner, such as the skill's README or a dedicated notice. Preserve required license notices and omit commit hashes from prose.
- Keep the entry point concise; place detailed procedures in linked references.
- Link every supporting reference directly from `SKILL.md` and state when to read it.
- Use relative paths within a skill so the complete directory remains portable.
- Include only resources that support the skill's intended operation.
- Keep host-specific metadata separate, such as `agents/openai.yaml`.
- Keep metadata consistent with the skill's actual behaviour.
- Update the skill's README when its user-facing behaviour changes.

## File length

- Keep new skill files and this `AGENTS.md` at 100 lines or fewer per file.
- When editing a skill file, keep the resulting file within that limit.
- Split longer instructions into coherent reference files; do not compress prose into unreadably long lines to evade the limit.
- If splitting an existing file would exceed the authorised scope, explain the required restructuring and ask before expanding the task.
- Apply the limit to skill package files, not to records produced by a skill.
- Do not refactor unrelated existing files merely to enforce the limit.

## Verify changes

- Validate required frontmatter, names, relative links, and file line counts.
- Check that every linked resource exists and contains the expected instructions.
- Remove placeholders and check the workflow against the user's requirements.
- Run added or modified executable scripts with representative inputs.
- Validate Claude metadata with `claude plugin validate . --strict`.
- For behavioural changes, exercise relevant workflow paths where practical.
- Distinguish structural validation from observed workflow behaviour.
- Review the final diff and verify that only intended files changed.

## Save and release

- Save authorised changes to the repository and verify the resulting files.
- Preserve concurrent changes; never force-push to overwrite them.
- Commit and push skill changes to this repository's `main`.
- Treat commits on `main` as development state, not published releases.
- Follow the version and release policy below for requested releases.
- Keep version metadata, changelog entries, release tags, and assets consistent.
- Do not create a release merely because skill files were edited.
- Report what changed and which checks actually passed.

## Versions and releases

- A skill may carry a `version` file whose single line is its current version, updated in the commit that ships the change. Record user-visible changes in the skill's changelog.
- A release is an immutable annotated tag `<name>-vMAJOR.MINOR.PATCH` in this repository, with a matching GitHub Release whose notes summarise the changelog entry and which attaches one ZIP with exactly one top-level skill directory.
- `PATCH` fixes compatible behaviour, `MINOR` adds compatible behaviour, and `MAJOR` changes a workflow or persisted format incompatibly.
- Plugin manifests and marketplace entries omit `version` deliberately: Git-backed installs use the resolved commit, so `--strict` validation reports it as a warning.
- Workflow-schema labels such as `v6 → v7` in migration instructions describe persisted project-file compatibility, not release versions.
