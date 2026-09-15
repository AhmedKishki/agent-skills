---
name: changelog.md
description: Records the enduring user-visible history of the draft-writing skill.
---

# Changelog

This is the single enduring changelog for `draft-writing`. Current behaviour is governed by `SKILL.md`; historical entries describe the behaviour of their version. Entries were recovered from the former `change-log.md`, Git commits, annotated and lightweight tags, and published GitHub releases.

## 21.0.0 — 2026-09-15

- Made white-box synthesis and synthesis material strictly Human-only: approved user material, source-map excerpts and other approved outputs are eligible only when their complete lineage is Human.
- Made AI-authored, Mixed and unverified material permanently ineligible for white-box synthesis and material, regardless of later approval.
- Replaced unsolicited bounded AI suggestions with user-led gap resolution: identify the smallest exact gap, explain why Human-preserving operations cannot fill it and ask the user to supply or resolve it.
- Permitted an AI suggestion only after an explicit user request, with exact marking, permanent provenance and no later use as synthesis input.
- Added post-synthesis smoothing. Human-only smoothing may revise material through white-box operations; explicitly requested AI smoothing may enter only the draft and never alters Human synthesis lineage.

## 20.0.2 — 2026-09-15

- Required Human-first white-box reconstruction and restricted AI suggestions to demonstrated residual gaps that prevent completion.
- Added collaborative gap resolution: expose the smallest exact gap, show why permitted operations cannot fill it, ask the user to resolve it, then offer at most one bounded suggestion.
- Required mixed proposals to mark only exact AI additions, wholly Human proposals to use no marker, and wholly AI proposals to mark the complete output.
- Applied the gap-first procedure separately to argument claims, thesis relations, qualifications and dependencies as well as reader-facing drafting.

## 20.0.1 — 2026-09-15

- Required every AI-authored span, including connectors and transitions, to be marked inline in proposals and approved exactly; general provenance disclosure no longer suffices.
- Made explicit that the user must never be expected to detect undisclosed AI wording.

## 20.0.0 — 2026-09-14

- Replaced the linear thesis-to-arc workflow with a recursive process in which drafting can revise any affected upstream owner.
- Consolidated active project outputs into thesis, user material, source maps, arguments, material, plan, draft, and progress.
- Made arguments the record of every current argument, its thesis relation, qualifications, dependencies and authorized basis.
- Made material the record of synthesized passages, each formed from one or more approved arguments.
- Made argument formation an ongoing part of drafting: candidates may be inferred from source maps, user material, direct user requests, the thesis, existing arguments, the plan and drafting gaps, but require explicit approval.
- Routed independent parts of user prompts to thesis, user material or arguments, while keeping source quotations source-authored in source maps.
- Generalised `white-box-synthesis` as directly labelled authorised inputs producing an exactly labelled output through `COPY`, `INFLECT`, `NORMALISE`, `ORDER`, and `DELETE`.
- Required relevant user material in synthesis when present; exclusion requires explicit user authorisation.
- Required every argument to state its substantive relation to the thesis and required contradictions to be exposed for user resolution.
- Required pedagogical critique of user claims against mapped sources: explain conflicts in evidence, scope or category while preserving the user’s authority to reject the critique without relabelling the disputed claim as source-grounded.
- Restricted AI-authored wording and connections to exact, bounded, disclosed proposals with explicit approval.
- Standardised every canonical output while allowing its substantive content and internal development to remain flexible.
- Added minimal `name` and `description` YAML frontmatter to every module and canonical output structure.
- Limited metadata to current operative direction, identity, evidence location, provenance and live blockers.
- Made every ID namespace monotonic: removed, retired, merged or replaced IDs remain historically allocated and are never reused.
- Removed repeated editing notes, default metadata, immutable working snapshots, superseded-decision archives and overlapping handoff records from the workflow.
- Made progress the necessary-and-sufficient next-session handoff for current work, reliable state, live decisions and limits, approval state, next work, blockers, resume files and counters.
- Removed the Basic Memory integration; canonical project files and Git remain the workflow’s durable state.
- Consolidated citation verification into drafting and made a separate citation work file optional.
- Restored one enduring changelog inside `skills/draft-writing` and reconstructed its full available history.

### Breaking migration

- `{project}-thesis.md` absorbs `{project}-user-thesis.md` and the former `{project}-draft-direction.md`.
- `{project}-arguments.md` owns arguments and their bases; `{project}-material.md` owns synthesized passages formerly distributed across synthesis and argument-draft records.
- `{project}-article-arc.md` becomes `{project}-plan.md`.
- `{project}-progress.md` absorbs separate handoff and current-focus records.
- `{project}-draft.md` remains the only canonical output with the `draft-` prefix.
- Live files retain only current operative information. Use Git when earlier states are needed.

## 19.0.0 — 2026-09-14

- Removed legacy modules after routing their remaining responsibilities to canonical owners.
- Removed the former historical `change-log.md`; 20.0.0 reverses that decision and restores this enduring record.

## 18.0.0 — 2026-09-14

- Combined argument-definition and synthesis-basis approval into one decision while retaining separate storage owners.

## 17.0.0 — 2026-09-14

- Required lean canonical files and removed completed workflow history, repeated defaults and duplicated provenance.

## 16.0.0 — 2026-09-14

- Bounded working file families and made the article arc the sole structural plan.

## 15.0.0

- Recast draft-writing as a staged but recursive process: thesis, draft direction, source mapping, user-material routing, argument formation, synthesis-material approval, argument synthesis, one article arc, drafting and citation.
- Make `article-arc.md` the sole structural authority and retire separate blueprint and architectural-decision artifacts for new projects.
- Split argument definition, input collection and raw-prose synthesis into single-purpose modules and files.
- Classify incoming user material by function; preserve exact reusable user wording once and keep supplied source quotations source-authored.
- Replace active project-file tables with readable headings, normal text, bullets and blockquotes.
- Add a human-editability contract, direct-edit routing and minimal progress tracking.
- Retain old combined module filenames only as migration pointers for projects created before 15.0.0.

## 14.1.0

- Make user wording authoritative over AI wording.
- Block possible source–user conflicts until the agent quotes both positions, states the incompatibility and consequences, and the user explicitly resolves the article claim and source use.
- Permit an explicitly labelled recommendation; prohibit inferred resolutions and citation of a source as support for a claim it contradicts.

## 14.0.0

- Replace source-map tables with one `# Author, Full Source Title` heading and one `## CODE — Short topic, location` plus exact blockquote per excerpt.
- Use full author names and full source titles in source-map filenames.
- Migrate existing source maps mechanically: preserve stable excerpt codes, exact source wording and source order; move each row's code, short topic and locator into its H2; decode `<br>` as source paragraph breaks and table-escaped pipes as literal pipes; retain tracker coverage, originals and next-item counters.
- Historical changelog descriptions of earlier table schemas remain historical and are superseded by the 14.0.0 format.

## 13.0.0

- Replace article-arc and passage predrafting with schema-and-predraft: an unordered `predraft-schema.md` records stable arguments and broad Human input inventories; `predraft.md` stores approved raw argument material.
- Make blueprint-and-draft solely authoritative for passages, paragraphs, sections, selection and article order.
- Allow white-box synthesis to reuse approved Human white-box outputs while accepting Human inputs only, preserving finite lineage and always producing Human output.
- Use `{base}-{modifier}.md`, including `predraft-working.md`, `blueprint-working.md`, `draft-working.md` and `citation-working.md`.
- Keep every substantive decision under explicit user approval; require one focused question instead of guessing.

## 12.0.0

- Replace drafting and fidelity-audit with authorial-voice, blueprint-and-draft, and article-citation modules.
- Build immutable blueprint versions through critical user–agent discussion, then draft and approve one complete section at a time.
- Prohibit AI-authored article wording unless the user approves the exact span for one identified need; make authorial voice a skill-wide contract.
- Begin citation only from a user-approved finalised uncited draft and require New Left Review footnote style.
- Move validation into each producing module, generalise tracker objects and use British English throughout the skill.

## 11.0.0

- Treat approved thesis-and-vision and user wording as operational unless an affected aspect is explicitly marked `Outdated`; require the user to confirm both an emerging contradiction and that the new commitment shall become operative before applying it.
- Preserve superseded content and place an `Outdated` marker beside the exact affected aspect, identifying its operative replacement and invalidating only affected downstream passages.
- Simplify compact provenance to `Provenance`, `Method` and `Basis`; remove the uncalculated human-wording percentage while retaining exact reconstruction and authorship checks.

## 10.4.1

- Replace the `> comments:` header with an unlabelled `>` qualification under a section, passage or argument; its content may be a question, comment, direction, limit, boundary, specification or other qualification.

## 10.4.0

- Add optional `> comments:` blocks beneath article-arc sections, passages and arguments for their directions, limitations, boundaries, specifications and qualifications.
- Require every argument to end with one unlabelled, broad, user-revisable fragment-inventory bullet, using `- None identified` when no candidate is known.
- Distinguish inventory membership from synthesis selection: predraft proposes a limited set for explicit approval, white-box synthesis receives only that set, and provenance records only fragments actually used.
- Prevent inventory-only revisions from triggering synthesis, approving fragment use or invalidating unaffected prose.

## 10.3.0

- Replace article-arc paragraph units with single-claim passages. A passage is developed and approved independently of final paragraph boundaries and may become part of one paragraph, one paragraph, or multiple paragraphs.
- Make predrafting explicitly passage-by-passage: every in-scope arc passage is presented with its full construction record and must receive explicit approval before it is saved or work advances.
- Store each approved passage's compact provenance immediately after that passage. Remove the predraft's two-part prose/provenance structure.
- Define predraft as raw approved passage material that normally lacks connectors between passages and sections. Drafting owns collaborative connector development, final paragraph boundaries and connected article assembly.
- Simplify source maps to a single `Code | Excerpt | Location` table.
- Retire and delete the source-index module and remove all active index dependencies.

## 10.2.0

- Standardise compact provenance as origin, Human wording, Method and original Basis codes. Verify the human-wording declaration against recoverable originals.
- Present the full synthesis record before each user decision: exact inputs and output spans, ordered operations, argument coverage, support and limits.
- Replace saved construction ledgers with compact provenance records while retaining the two-part predraft layout. Align drafting, audits and wording retention with feasible reconstruction from the saved bases.

## 10.1.2

- Keep article-arc concerned with structure; predraft selects relevant sources and user wording for each argument and records their use.
- Make user-directed arc revision explicit within the predraft loop. Require approval of structural changes and resulting prose separately; move renumbering and reference maintenance into the shared editing rules.

## 10.1.1

- Standardise argument terminology across modules, examples and historical changelog descriptions.
- Key Used by argument ID and original fragment codes. Resolve ambiguous prose and source spans with exact text boundaries, paragraph positions or stored line positions.

## 10.1.0

- Simplify the arc to H2 sections, H3 paragraph claims and plain numbered arguments, with one top-level section progression. Section labels state claims or governing questions; final article headings are selected separately.
- Make dependence hierarchical: arguments establish paragraph claims, and paragraphs establish section claims or answer their questions. Keep explanations in prose and pending questions in the conversation/tracker.
- Use section.paragraph.argument numbering throughout active instructions. Synthesis develops arguments from human fragments; predraft records their prose spans and original codes while retaining paragraph-by-paragraph user approval.

## 10.0.0

- Require explicit user consent for substantive decisions and each synthesis result. Predraft presents one paragraph, waits for approval or comments, saves the approved result, then proceeds to the next paragraph.
- Make white-box synthesis a standalone algorithm: supplied claim, argument plan, human fragments and constraints produce a paragraph with Used and Construction, or a precise gap. Keep workflow and approval orchestration in the calling modules.
- Shorten the active instructions and use concrete, affirmative procedures while preserving editable schemas, section.paragraph.argument numbering, stable user/source codes and brief provenance.
- Develop the final article from approved predraft material; route structural changes through the arc and changed paragraphs through synthesis and user approval.
- Remove the predraft-report and full-export modules, the export script, and their active workflow references.

## 9.2.0
- Make section.paragraph.argument numbering explicit in both arc and predraft. Keep paragraph prose clean and give each argument one Used entry identifying its original user-n / source-coded fragments.
- Keep the four-field construction record: Arc locates the paragraph, Used owns the argument-to-fragment mapping, Construction explains meaningful changes and uses, and Selection records authority. Require finer span locators only where needed; add no fragment IDs or fourth numeric level.
- Reconcile argument boundaries and update Used labels with positional renumbering. Align review, audit, shared checks, and the report with the clarified construction trail.

## 9.1.0
- Rename user-inputs to user-wording, restoring the reusable-language function of user-synthesis. Allocate user-n only to human article wording; route meta direction, structure, and selection to their owners and discard purely procedural commands.
- Record thesis direction directly without a numbered-input prerequisite, routine Basis header, or completed-task checklist. Keep exact selection authority in predraft's brief record rather than a numbered approval entry; create predraft only when prose is selected.
- Give the article, each section, and each paragraph an explicit Arc line: section to section, paragraph to paragraph, and argument to argument. Use compact positional numbering 1 / 1.1 / 1.1.1 with short planning labels and no source codes or full prose in the arc.
- Make each paragraph's single claim and its arguments' causal or explanatory argument concrete. Check the relationship at every arrow rather than treating sequence as support.
- Select human fragments during synthesis, build the arguments, then compose one paragraph. Predraft alone owns actual source/user references, uses, spans when needed, interpretive limits, and selected heading placement; remove duplicate use mappings from arc and user-wording.
- Synchronize arrow chains and detailed blocks, renumbering affected positions and dependent references together. Preserve the content and authority behind each record during moves.
- Limit source maps to source identity and Code / Location / Excerpt entries without excerpt titles. Keep keyword/theme assignments only in the index and mapping coverage only in the tracker. Align consumers and the report with these separate responsibilities.

## 9.0.0
- Restore the required article → section → paragraph → argument → fragment arc with stable IDs, exact source/user references, and contextual uses and limits.
- Specify readable editable schemas for every output and reconcile direct user edits before regeneration. Preserve earlier human bases only while current records need them.
- Number contributions as user-n, with persistent allocation checkpoints. Keep thesis-and-vision to the general picture, questions, and specifications; capture its article-relevant human prose in user inputs for synthesis.
- Limit source maps to identity, access coverage, exact excerpts, codes, and locators. Move interpretive decisions to arc occurrences and keep the index focused on retrieval.
- Replace exhaustive synthesis span records with actual inputs, named sources, meaningful construction, and exact selection authority. Retain the five human-wording operations and checks for unsupported connections.
- Align predraft, readiness review, draft, audit, tracker, and export with the new structures. Keep source-heading handling explicit and small; preserve the existing export transport and validation.

## 8.0.1
- Remove the combine-sources module and its routing. Full export remains the handoff utility; legacy combined-source deliveries remain excluded from exports.

## 8.0.0
- Replace scattered question/provenance rules with a shared contract and user-inputs module: preserve exact contributions, pending parts, incorporation links, and standing permissions independently of approval.
- Give modules one output responsibility; merge source review into mapping and remove the separate authorship reference. Simplify source maps, index, tracker, and document headers; remove authorship percentages, default source lists, draft changelogs, and forced AI-gap exceptions.
- Rebuild the arc around stable section/paragraph IDs and optional argument plans. Keep strict original-wording synthesis with five operations, concrete evidence freshness, semantic join checks, and one compact construction record.
- Store exact predraft selections in two linked parts; assemble one chosen complete selection per paragraph. Keep review focused on findings, recheck affected work through authorised fixes, and run one final readiness check without repeated whole-file approval loops.
- Use a stable draft filename. Treat combined sources and full export as requested deliveries outside the tracked working set; retain compatibility guidance for existing projects without converting them automatically.
- Validate export resume fields, roles, table boundaries, delivery exclusions, and input aliases. Add verified replacement of a known prior delivery with failure preservation, plus exporter regression tests.

## 7.8.2
- The project-memory module is removed: the skill no longer defines or references a `{project}-memory.md` record; memory is external tooling, never a skill module.

## 7.8.1
- The memory module's reference no longer mentions MCP tooling: a project's recall layer is external tooling that may index project Markdown in place; the skill maintains only the Markdown record and never reads from or writes to a memory server on its behalf.

## 7.8.0
- The memory module becomes the project's context-preservation record: `{project}-memory.md` stores everything a different AI, in a new chat, needs to resume the project seamlessly — what the project is, where things stand, the plan, what is expected, and where everything lives — brought current at every session end. Decisions, Questions and Rejected keep their forms.
- The article arc's file shape moves to heading-level structure for readability: sections are H2 headings, paragraph claims are H3 headings, and arguments are plain numbered lines; the in-section paragraph-chain line is dropped and the trailing arrows are removed — the document order carries reading order.

## 7.7.0
- The arc's vocabulary is fixed as article → section → paragraph → argument → fragment: the article's claim is the thesis; each section supports the thesis; each paragraph makes one claim and is the target of one white-box run; arguments are the constitutive elements of paragraphs; fragments — exact source-map excerpts and user wording — are the smallest unit, synthesised into arguments, and arguments into paragraphs. Numbering nests per level: section, section.paragraph, section.paragraph.argument, section.paragraph.argument.fragment.
- The arc is a sketch, built from a general overview of the source maps and user wording: arguments carry no source-item citations (provenance lives in the predraft records and the source index), and the arc does not fix which fragment supports which claim. It is a dynamic document — revision at any stage, including mid-drafting, is expected; a revision marks affected dependents invalid and waits for user direction.
- Predrafting repeats paragraph synthesis — find and choose fragments, synthesise them into arguments and the paragraph — until the predraft is fully formed. The predraft remains a raw-material pool: not arc-keyed, and not all selected material need be used; each passage names the arc elements it covers.

## 7.6.2
- The predraft file becomes two parts: Part 1 holds the selected passages as clean prose under their headings; Part 2 holds each passage's production record (Basis/Use stamp and, for white-box passages, the final record) under the same heading. A readability and footprint change only; no rule changes.

## 7.6.1
- Standardised, minimal provenance declarations across all module templates: `**<Scope>:** Origin · Human wording: P%`, adding method/basis/use only where needed to trace origin or a controlled use.
- Memory module reframed: `{project}-memory.md` is the context-preservation/handoff record between tasks; the project's actual memory is handled by MCP tooling outside the skill.

## 7.6.0
- The article arc becomes three scales in plain arrow form: the article as a chain of sections, each section as a chain of paragraphs, and each paragraph as a single argument that is the exact target of one white-box run. The move-based two-scale arc is superseded.
- The user's own synthesis wording leads every candidate: white-box synthesis runs one candidate per arc paragraph, building the user's synthesis up and strengthening it with source support; source wording grounds and qualifies the user's claims, never the reverse.
- Predraft development happens one arc paragraph at a time, and the user's voice is authoritative and stays present in every passage.
- Project memory becomes a single FIFO markdown working record — Current focus, Decisions, Questions (open and closed), Rejected — updated from the top, with entries falling away from the bottom as they stop being useful; the knowledge-graph model and its separate graph layer are removed.
- Terminology aligned across the predraft report, drafting, fidelity audit, source review and source maps: "move" and "local arc" give way to paragraphs and argument steps.
- The migration module is removed.

## 7.5.0
- Move-based arc: the article arc is now two levels — the global arc (sections) and, per section, an ordered series of moves. The section arcs replace the local-arc tables and any separate moves list as the single moves representation; a conversion note folds pre-7.5 local-arc units into moves under the removal-impact protocol.
- Arc ↔ synthesis integration: each move row is the target of exactly one white-box run (proposition, role, destination, entry, exit, boundary, named source items); one move per synthesis run, and the predraft passage is keyed to its move.
- Standard file skeleton in file-output-standard.md: every canonical workflow file is `# Title` → lean process header → scoped authorship declarations → module body, with the draft's prose-first layout as the sole documented exception.
- Terminology aligned across modules: "move" replaces "argument unit"/"local argument"; tracker, predraft report, drafting, fidelity audit, and source review now speak of moves.

## 7.4.3
- Fold article role and framework role into the Qualification column: selected items are now `Code | Excerpt | Location | Qualification`, where the cell identifies the role alongside any item-specific qualification, limit, or counterclaim.

## 7.4.2
- Source maps are a table of excerpts, not per-excerpt headings: each row is `Code | Excerpt | Location | Article role | Framework role | Qualification`, with no topic titles.

## 7.4.1
- Metadata is AI-origin process scaffolding, never article content, and reduced to the minimum that identifies a passage's origin and Human-wording percentage.
- Source maps carry no per-item metadata: blockquotes are understood as exact source quotations, every other map field as AI process scaffolding.

## 7.4.0
- Enable the humaniser skill.
- Add MCP server configs.

## 7.3.5
- Replace the candidate/predecessor workflow with edit-in-place + git diff.

## 7.3.4
- Remove all timestamps; stable filenames, git diff tracks changes.

## 7.3.3
- Split project memory into a knowledge graph + markdown questions/tasks + tracker.

## 7.3.2
- Move the skill into the skills/ directory.

## 7.3.1
- Rename source index and add source list.

## 7.3.0
- Add project memory module.

## 7.2.0
- Reframe functions as user-directed modules.

## 7.1.0
- Reframe workflow as user-called functions.

## 7.0.0
- Update workflow descriptions to the predrafting model.

## 6.25.1
- Switch to white-box synthesis and revamp exports.

## Before 6.25.1 — 2026-08-30

- Added the `draft-writing` skill with thesis, source review, article arc, predraft, drafting and audit stages; collaboration, provenance, handoff, export and migration support; and Claude/OpenAI metadata.

## Publication and reconstruction record

### Published GitHub releases

- [10.0.0](https://github.com/AhmedKishki/agent-skills/releases/tag/draft-writing-v10.0.0) — published 2026-09-07; its release notes also contain the unreleased 8.0.0–9.2.0 sequence.
- [7.6.1](https://github.com/AhmedKishki/agent-skills/releases/tag/draft-writing-v7.6.1) — published 2026-09-04; its release notes also contain 7.4.1–7.6.0.
- [7.3.0](https://github.com/AhmedKishki/agent-skills/releases/tag/draft-writing-v7.3.0) — published 2026-09-02.
- [7.2.0](https://github.com/AhmedKishki/agent-skills/releases/tag/draft-writing-v7.2.0) — published 2026-08-31.
- [7.1.0](https://github.com/AhmedKishki/agent-skills/releases/tag/draft-writing-v7.1.0) — published 2026-08-31.
- [7.0.0](https://github.com/AhmedKishki/agent-skills/releases/tag/draft-writing-v7.0.0) — published 2026-08-31.
- [6.25.1](https://github.com/AhmedKishki/agent-skills/releases/tag/draft-writing-v6.25.1) — published 2026-08-31.

### Git tag record

- 7.6.1 and 10.0.0 are annotated release tags.
- 6.25.1, 7.0.0, 7.1.0, 7.2.0, 7.3.0, 7.3.1 and 7.3.2 are annotated tags.
- 7.3.3, 7.3.4, 7.3.5 and 7.4.0 are lightweight tags.
- No current GitHub release object was found for 7.3.1–7.4.0. The published 7.6.1 notes nevertheless refer to 7.4.0 as the preceding published release.

### Commit-reconstructed development versions

Versions 7.4.1–9.2.0 and 10.1.0–20.0.0 without a corresponding tag were reconstructed from the former changelog and version-labelled commits. The skill was first added on 2026-08-30 before the earliest recoverable changelog entry, 6.25.1.
