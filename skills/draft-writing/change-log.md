# Changelog

## 10.0.0

- Require explicit user consent for substantive decisions and each synthesis result. Predraft presents one paragraph, waits for approval or comments, saves the approved result, then proceeds to the next paragraph.
- Make white-box synthesis a standalone algorithm: supplied claim, sentence plan, human fragments and constraints produce a paragraph with Used and Construction, or a precise gap. Keep workflow and approval orchestration in the calling modules.
- Shorten the active instructions and use concrete, affirmative procedures while preserving editable schemas, section.paragraph.sentence numbering, stable user/source codes and brief provenance.
- Develop the final article from approved predraft material; route structural changes through the arc and changed paragraphs through synthesis and user approval.
- Remove the predraft-report and full-export modules, the export script, and their active workflow references.

## 9.2.0
- Make section.paragraph.sentence numbering explicit in both arc and predraft. Keep paragraph prose clean and give each sentence one Used entry identifying its original user-n / source-coded fragments.
- Keep the four-field construction record: Arc locates the paragraph, Used owns the sentence-to-fragment mapping, Construction explains meaningful changes and uses, and Selection records authority. Require finer span locators only where needed; add no fragment IDs or fourth numeric level.
- Reconcile sentence boundaries and update Used labels with positional renumbering. Align review, audit, shared checks, and the report with the clarified construction trail.

## 9.1.0
- Rename user-inputs to user-wording, restoring the reusable-language function of user-synthesis. Allocate user-n only to human article wording; route meta direction, structure, and selection to their owners and discard purely procedural commands.
- Record thesis direction directly without a numbered-input prerequisite, routine Basis header, or completed-task checklist. Keep exact selection authority in predraft's brief record rather than a numbered approval entry; create predraft only when prose is selected.
- Give the article, each section, and each paragraph an explicit Arc line: section to section, paragraph to paragraph, and sentence to sentence. Use compact positional numbering 1 / 1.1 / 1.1.1 with short planning labels and no source codes or full prose in the arc.
- Make each paragraph's single claim and its sentences' causal or explanatory argument concrete. Check the relationship at every arrow rather than treating sequence as support.
- Select human fragments during synthesis, build the sentences, then compose one paragraph. Predraft alone owns actual source/user references, uses, spans when needed, interpretive limits, and selected heading placement; remove duplicate use mappings from arc and user-wording.
- Synchronize arrow chains and detailed blocks, renumbering affected positions and dependent references together. Preserve the content and authority behind each record during moves.
- Limit source maps to source identity and Code / Location / Excerpt entries without excerpt titles. Keep keyword/theme assignments only in the index and mapping coverage only in the tracker. Align consumers and the report with these separate responsibilities.

## 9.0.0
- Restore the required article → section → paragraph → sentence → fragment arc with stable IDs, exact source/user references, and contextual uses and limits.
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
- Rebuild the arc around stable section/paragraph IDs and optional sentence plans. Keep strict original-wording synthesis with five operations, concrete evidence freshness, semantic join checks, and one compact construction record.
- Store exact predraft selections in two linked parts; assemble one chosen complete selection per paragraph. Keep review focused on findings, recheck affected work through authorized fixes, and run one final readiness check without repeated whole-file approval loops.
- Use a stable draft filename. Treat combined sources and full export as requested deliveries outside the tracked working set; retain compatibility guidance for existing projects without converting them automatically.
- Validate export resume fields, roles, table boundaries, delivery exclusions, and input aliases. Add verified replacement of a known prior delivery with failure preservation, plus exporter regression tests.

## 7.8.2
- The project-memory module is removed: the skill no longer defines or references a `{project}-memory.md` record — memory is external tooling (Basic Memory where adopted), never a skill module.

## 7.8.1
- The memory module's reference no longer mentions MCP tooling: a project's recall layer is external tooling that indexes the project's markdown in place as notes (Basic Memory where adopted); the skill maintains only the markdown record and never reads from or writes to a memory server on its behalf.

## 7.8.0
- The memory module becomes the project's context-preservation record: `{project}-memory.md` stores everything a different AI, in a new chat, needs to resume the project seamlessly — what the project is, where things stand, the plan, what is expected, and where everything lives — brought current at every session end. Decisions, Questions and Rejected keep their forms.
- The article arc's file shape moves to heading-level structure for readability: sections are H2 headings, paragraph claims are H3 headings, and sentences are plain numbered lines; the in-section paragraph-chain line is dropped and the trailing arrows are removed — the document order carries reading order.

## 7.7.0
- The arc's vocabulary is fixed as article → section → paragraph → sentence → fragment: the article's claim is the thesis; each section supports the thesis; each paragraph makes one claim and is the target of one white-box run; sentences are the constitutive elements of paragraphs; fragments — exact source-map excerpts and user wording — are the smallest unit, synthesised into sentences, and sentences into paragraphs. Numbering nests per level: section, section.paragraph, section.paragraph.sentence, section.paragraph.sentence.fragment.
- The arc is a sketch, built from a general overview of the source maps and user wording: sentences carry no source-item citations (provenance lives in the predraft records and the source index), and the arc does not fix which fragment supports which claim. It is a dynamic document — revision at any stage, including mid-drafting, is expected; a revision marks affected dependents invalid and waits for user direction.
- Predrafting repeats paragraph synthesis — find and choose fragments, synthesise them into sentences and the paragraph — until the predraft is fully formed. The predraft remains a raw-material pool: not arc-keyed, and not all selected material need be used; each passage names the arc elements it covers.

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
