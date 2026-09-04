# Changelog

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
