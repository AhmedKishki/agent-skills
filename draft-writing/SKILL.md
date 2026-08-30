---
name: draft-writing
description: "Collaboratively build a user-controlled, source-grounded article. Use for thesis-led drafting, requested Markdown source or user exports, or requested hand-offs. Enforces meaning-preserving source fidelity, Human/Mixed/AI provenance, reductive synthesis, coded theory/metatheory source maps, argument-led rescans, global/local arcs, and previous-major migration."
---

# Collaborative thesis-led drafting

**Version:** 6.20.0 (2026-08-30)

## Core contract

The user is author and final authority. Ask whenever content, wording, relations, or judgement are missing. Only the user revises thesis/metatheory, selects exact predraft wording, places it unchanged in the arc, approves stages, or declares completion.

Source fidelity preserves meaning; quotation is not required. Apply excerpt, Article/Framework role, optional metatheory, provenance, synthesis, use, change, and cleanup rules only through their linked owner modules. Framework-only material never supplies article wording or synthesis input.

Attempt [reductive synthesis](references/reductive-synthesis.md) before every substantive suggestion; only [collaborative questions](references/collaborative-questions.md) may offer a labelled post-rescan AI gap suggestion. Each output has one function and only current useful state. After an authorised change, remove retracted direction, retain unaffected work, and return to the earliest affected stage. Never strengthen the thesis. No humaniser follows.

## Module loading

Read each required module in full before acting:

- [Authorship and wording provenance](references/authorship-and-provenance.md) before project work.
- [Shared output-file standard](references/file-output-standard.md) before changing files.
- [Activity tracker](references/activity-tracker.md) before resuming, reconciling, approving, or delivering.
- [Keyword and theme index](references/index.md) before indexing or searching excerpts.
- [Previous-major project migration](references/migration-to-v6.md) for pre-v6 work, active v5 files, schema mismatches, or established legacy namespaces.
- [Requested hand-off](references/handoff.md) only when the user explicitly requests a hand-off document.
- [Requested source export](references/export.md) only on an explicit request; Markdown only.
- [Requested user export](references/user-export.md) only on an explicit request; Markdown only.
- [Collaborative questions, answer routing, and user synthesis](references/collaborative-questions.md) before asking, classifying an answer, or recording content-producing user answers.
- [Predraft](references/predraft.md) before discussing, selecting, or using article wording.
- [Transparent reductive synthesis](references/reductive-synthesis.md) before synthesis.

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

<!-- Major-version rule for future maintainers: at v7 replace the v5→v6 migration with v6→v7 migration and update its links, metadata, and tracker clauses. Always retain exactly the immediately preceding major-version path; never remove migration support entirely. -->
