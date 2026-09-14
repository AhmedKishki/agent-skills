# Changelog

This file records user-visible changes to the skills in this repository. Git retains implementation history; this changelog describes released behavior and migrations.

## Unreleased

### draft-writing 20.0.0

- Replaced the linear thesis-to-arc workflow with a recursive process in which drafting can revise any affected upstream owner.
- Consolidated active project outputs into user thesis, user material, source maps, material, plan, draft, and progress.
- Combined argument definitions, selected synthesis inputs, construction records, and developing argument prose in one flexible material owner.
- Generalized `white-box-synthesis` as authorised inputs `A, B, C, …` producing output `Z` through `COPY`, `INFLECT`, `NORMALISE`, `ORDER`, and `DELETE`.
- Required relevant user material in synthesis when present; exclusion now requires explicit user authorisation.
- Required every claim and argument to state its substantive relation to the user thesis and required contradictions to be exposed for user resolution.
- Restricted AI-authored wording and connections to exact, bounded, disclosed proposals with explicit approval.
- Standardized every canonical output while allowing its substantive content and internal development to remain flexible.
- Added minimal `name` and `description` YAML frontmatter to every module and canonical output structure.
- Limited metadata to current operative direction, identity, evidence location, provenance and live blockers.
- Made every ID namespace monotonic: removed, retired, merged or replaced IDs remain historically allocated and are never reused.
- Removed repeated editing notes, default metadata, immutable working snapshots, superseded-decision archives, and overlapping handoff records from the workflow.
- Made progress the sole resumption owner for current work, achieved state, next work, blockers, and counters.
- Consolidated citation verification into drafting and made a separate citation work file optional.

#### Breaking migration

- `{project}-user-thesis.md` absorbs `{project}-thesis.md` and `{project}-draft-direction.md`.
- `{project}-arguments.md`, `{project}-synthesis-material.md`, and `{project}-argument-drafts.md` become `{project}-material.md`.
- `{project}-article-arc.md` becomes `{project}-plan.md`.
- `{project}-progress.md` absorbs separate handoff/current-focus records.
- `{project}-draft.md` remains the only canonical output with the `draft-` prefix.
- Live files retain only current operative information. Use Git when earlier states are needed.

## 19.0.0

- Removed legacy draft-writing modules after routing their remaining responsibilities to canonical owners.

## 18.0.0

- Combined argument-definition and synthesis-basis approval into one decision while retaining separate storage owners.

## 17.0.0

- Required lean canonical files and removed completed workflow history, repeated defaults, and duplicated provenance.

## 16.0.0

- Bounded working file families and made the article arc the sole structural plan.

## 15.0.0

- Introduced one editable article arc and strengthened direct-edit handling.

## Earlier releases

Earlier behavior remains recoverable from Git commits, annotated tags, and published GitHub releases.
