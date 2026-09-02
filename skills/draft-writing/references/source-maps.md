# Per-source maps

Keep one lineage per source. Assign and increment the tracker's monotonic **Next source code**: A–Z, then AA onward; never reuse. Retire an unneeded map only after its references and stale combined-sources file are handled and its removal is authorised under [file-output-standard.md](file-output-standard.md). Concurrent editions get separate codes; a replacement keeps the code only after all locators/dependents are revalidated.

Map one source at a time using that source, the approved thesis-and-vision (including its operative-metatheory commitments), and explicit user decisions. Never use another source, its map, or the index to decide what the current source contains, fill its context, assign its roles, or suppress an item as cross-source duplication. Establish cross-source relations only downstream after every source has its own mapping.

Name maps `{project}-source-map-{code}-{author-short-title}.md`; head with full author/title. Assign then increment **Next item**; never reuse/renumber. Base IDs are A1, A2, and so on; add **-MT** to the active label when Framework is Metatheory. Role changes alter the label/references, not the base. Corrections retain numbers; splits, merges, and replacements get new ones. Preserve legacy dual namespaces.

Each passage has independent roles:

- **Article:** Theory | Other article support | None | Unresolved
- **Framework:** Metatheory | None | Unresolved

Theory supplies an article concept, mechanism, or argument; Other supplies evidence, context, example, qualification, limit, or contest; Metatheory supplies silent fit only. A user-designated metatheory source defaults to Framework: Metatheory and Article: None; select Article separately. **Unresolved** blocks use. Role fields—not suffixes—authorise use. After a role change, mark affected dependents invalid; if framework commitments may change, suggest revisiting [thesis and vision](thesis-and-vision.md) and wait.

Apply only the operative metatheory recorded in thesis-and-vision. Framework material silently tests fit; it never supplies article evidence, citations, contributions, vocabulary, wording, relations, or synthesis inputs. MT-qualified wording needs separate Article role, predraft selection, arc disposition, and global draft use.

Record one readable path row per main argument/move, including unused moves, with locator, item range, possible roles, relevance, and provenance. The path is retrieval guidance only; copy no passage.

Each excerpt is an exact Human quotation centred on one relevant claim/topic named with exact source/user wording. Retain only enough context to identify the subject and preserve meaning, relation, scope, modality, and qualification; omit unrelated setup, examples, and adjacent claims. One item may join same-topic fragments from one contiguous paragraph or bounded consecutive page/section range, in source order, with **[…]** only between retained words. Different locators or an intervening topic require separate items. Preserve source-authored ellipses; add no leading/trailing **[…]** merely for a mid-unit boundary. The blockquote and locator define the quotation.

Legacy reformulations retain their established provenance/use but are not active excerpts; **combine sources** copies them only as part of the complete map. Coverage records scan extent, not excerpt completeness. Record source identity, selection basis, coverage, source-wide qualifications once, and item qualifications locally. Exclude summaries, unrelated material, thesis changes, cross-source comparison, and placement.

Keep every identity, qualification, main-move cell, topic, quotation, and locator readable without project codes; locators may retain source-native numbering or identifiers.

    # Source map A — Full author, full title

    - **Project:** Project name
    - **Status:** Working | Approved
    - **Next item:** A1
    - **Source:** Original filename or citation
    - **Selection basis:** Exact active thesis-and-vision filename; operative metatheory location when defined
    - **Coverage:** Complete | Partial, exact limit
    - **Source role default:** Passage-specific | User-designated full Metatheory · **Decision provenance:** compact passage stamp
    - **Collaboration:** Infer the module from a clear request; ask on ambiguity; never infer substantive content or authority
    - **Process prose:** AI
    - **Item wording authorship:** Human · Human wording: 100% · Method: exact source/user topic label and exact source quotation · Basis/Use: item heading and locator

    ## Additional source qualifications

    Source-wide edition, access caveat, scope, limit, counterclaim, or caution, each with provenance.

    ## Source argument path
    | Main source argument or move | Locator / item range | Article role · Framework role | Current or possible relevance | Authority/provenance |
    |---|---|---|---|---|

    ## Item label · Main claim/topic — locator

    > Exact source fragment centred on the named claim/topic; mark editorial omissions with […].

    **Article role:** role
    **Framework role:** role
    **Qualification:** Exact item-specific qualification, limit, or counterclaim; omit when none
    **Qualification provenance:** Compact stamp; required with Qualification
    **Role-decision provenance:** One compact stamp if both decisions share every field; otherwise one per role · Use: Process: this source-map item role

Identity, status, next item, source, selection basis, coverage, both roles, role-decision provenance, item-wording default, and locators are mandatory. Stamp any legacy non-quotation item or AI/Mixed topic label locally. Omit empty qualifications. Within one source, add an excerpt only when it contributes a distinct claim, relation, scope, modality, qualification, role, function, or materially useful occurrence. A newly discovered qualification at the same locator that governs an existing excerpt corrects that item and retains its number; a qualification established at a different locator gets a new minimal item without repeating more of the claim than meaning requires. Otherwise record a useful repeated locator in the source path or coverage without duplicating the item. Across sources, overlapping support remains independently mapped because its source provenance is distinct.

Record **No relevant material retained** with local provenance and coverage basis when applicable. Rescans update the path and append only net-new items in discovery order. After a direction change or item split/merge/replacement, follow the [removal-impact protocol](file-output-standard.md) before omitting superseded items; preserve **Next item** and never reuse numbers. Never replace an item in place or save an unchanged map. Every active item addition, removal, split, merge, replacement, content change, code change, or active-label change automatically triggers an immediate [index](index.md) refresh before the next question, action, synthesis, or delivery.

After one full-name key, internal files use codes such as A, A1, and A2-MT. Chat, article prose, and citations use full names and readable descriptions, never codes. [Combined sources](combine-sources.md) preserves each complete map, including its codes and full-name key, unchanged.
