---
name: draft-writing
description: "Collaboratively build a user-controlled, source-grounded article. Use for thesis-led drafting, a requested full-export handoff ZIP, or a requested combination of complete source maps and index. Enforces meaning-preserving source fidelity, Human/Mixed/AI provenance, white box synthesis, coded theory/metatheory source maps, argument-led rescans, global/local arcs, and previous-major migration."
---

# Collaborative thesis-led drafting

## Core contract

The user is author and final authority. Ask whenever content, wording, relations, or judgement are missing. Only the user revises thesis/metatheory, selects exact predraft wording, places it unchanged in the arc, approves stages, or declares completion.

Source fidelity preserves meaning; quotation is not required. Apply excerpt, Article/Framework role, optional metatheory, provenance, synthesis, use, change, and cleanup rules only through their linked owner modules. Framework-only material never supplies article wording or synthesis input.

Map each source independently and refresh the [index](references/index.md) whenever an active excerpt changes. Before draft assembly, attempt [white box synthesis](references/white-box-synthesis.md) for every substantive suggestion. If its Human inputs contain a gap, expose the gap and stop before any resolution attempt; only a later [collaborative-questions](references/collaborative-questions.md) turn may offer a labelled post-rescan AI gap suggestion. Never synthesise during draft assembly; black-box synthesis is prohibited.

Each output has one function and only current useful state. Save only net-new governing information. Before an addition or change removes, supersedes, invalidates, deduplicates, or retires anything, follow the [novelty and removal-impact rules](references/file-output-standard.md): tell the user exactly what would be lost and obtain any required authority before changing files. After an authorised change, remove only the disclosed obsolete state, retain unaffected work, and return to the earliest affected stage. Never strengthen the thesis. No humaniser follows.

## Module loading

Read each required module in full before acting:

- [Authorship and wording provenance](references/authorship-and-provenance.md) before project work.
- [Shared output-file standard](references/file-output-standard.md) before changing files.
- [Activity tracker](references/activity-tracker.md) before resuming, reconciling, approving, or delivering.
- [Keyword and theme index](references/index.md) before indexing or searching excerpts.
- [Previous-major project migration](references/migration-to-v6.md) for pre-v6 work, active v5 files, schema/current-use mismatches, established legacy namespaces, or legacy synthesis records.
- [Requested full export](references/full-export.md) only when the user explicitly requests a **full export** or handoff package; ZIP only.
- [Requested combined sources](references/combine-sources.md) only when the user explicitly requests **combine sources**; Markdown only.
- [Collaborative questions, answer routing, and user synthesis](references/collaborative-questions.md) before asking, classifying an answer, or recording content-producing user answers.
- [Predraft](references/predraft.md) before discussing, selecting, or using article wording.
- [White box synthesis](references/white-box-synthesis.md) before synthesis.

Read the current stage and its output specification:

| Stage or output | Specification |
|---|---|
| 1. Thesis and vision | [Thesis and vision](references/stage-1-thesis-and-vision.md) |
| 2. Source material | [Source review](references/stage-2-source-review.md) and [per-source maps](references/source-maps.md) (including operative metatheory) |
| 3. Global and local article arc | [Article arc](references/stage-3-article-arc.md) |
| 4. Selected raw wording and draft | [Predraft](references/predraft.md) and [draft and changelog](references/stage-4-draft.md) |
| 5. Fidelity audit | [Audit](references/stage-5-audit.md) |

## Workflow

Run Stages 1–5 in order, returning to the earliest invalidated stage. Stage 3 first creates a **Working** arc with resolved structure and **Undecided** passage actions. Stage 4 predrafts one argument at a time and updates those rows; after all resolve, the user approves the complete arc and draft assembly begins. Do not substitute source summaries or generative drafting. Create only linked files and follow immediate save/tracker rules.

A handoff request means **full export**; create no separate hand-off document. The former **export** and **export user** functions are retired. Do not interpret either retired name as a legacy alias: if the intended current function is unclear, ask whether the user wants **full export** or **combine sources**.

<!-- Workflow-schema rule for future maintainers: at schema v7 replace the v5→v6 migration with v6→v7 migration and update its links, metadata, and tracker clauses. Always retain exactly the immediately preceding schema migration path; never remove migration support entirely. -->
