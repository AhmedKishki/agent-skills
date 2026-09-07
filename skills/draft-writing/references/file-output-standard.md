# Shared file contract

## Owners and routing

Use stable `{project}-` filenames and edit in place. Each fact or decision has one authoritative home; dependent files refer to it.

| Content | Filename after the prefix |
|---|---|
| General picture, questions, specifications, accepted framework | `thesis-and-vision.md` |
| Exact reusable user article language | `user-wording.md` |
| Source identity, excerpt codes, locations, exact excerpts | `source-map-{code}-{author-short-title}.md` |
| Keywords, themes, excerpt retrieval assignments | `source-index.md` |
| Section, paragraph and supporting argument claims | `article-arc.md` |
| Selected prose and compact provenance | `predraft.md` |
| Reader-facing article and links to its provenance trail | `draft.md` |
| Working inventory, reading coverage, allocation counters, next action | `activity-tracker.md` |

Split a user message by function. Capture article language exactly in user wording; apply explicit general directions in thesis, structural decisions in arc, and exact prose selections in predraft. Route source leads to mapping. Execute procedural commands and omit their completed text from the article files.

Identified user-authored article language supplied in thesis, arc, predraft, draft or conversation also enters user wording as its original basis. Keep source quotations attributed to their source. Predraft owns the saved provenance trail; its selected prose and the draft are derived outputs.

## Consent and provenance

Apply the [collaboration rule](../SKILL.md#collaboration) at every substantive choice. Present the exact candidate or change and ask for approval or comments. Keep an unanswered proposal distinct from accepted content. An explicit selection authorises saving that result and mechanically updating its references.

Preserve these distinctions:

- **Authorship:** original user wording, source wording, or assistant arrangement. Approval retains that origin.
- **Evidence:** what the original supports in context.
- **Selection:** the user's explicit acceptance of the particular result.

Use established human originals for article wording. Mark uncertain or mixed origin through the compact provenance format and obtain clarification before using the uncertain part. When evidence and the intended claim differ, explain the gap and ask the user how to proceed.

## Compact provenance

Use this field order whenever an explicit provenance declaration is needed:

```markdown
**Provenance:** Mixed · Human wording: 100% · Method: white-box synthesis · Basis: T1, T2, T5, T6, AA4, E10, user-1, user-2
```

- **Human:** unchanged wording from a human original. **Mixed:** human wording composed by the assistant. **AI:** assistant-authored wording. **Unverified:** origin remains unresolved.
- **Human wording:** use `100%` after verifying all wording against human originals through permitted operations. Use `Unverified` for an incomplete check; retain `0%` for known wholly assistant-authored wording. Approval preserves the actual origin.
- **Method:** the actual process, such as `white-box synthesis`, `verbatim user wording` or `verbatim source excerpt`.
- **Basis:** original source/user codes actually used, deduplicated in order of use. Write source codes as `T1` here; they resolve to the same entries as `src:T1`. Include actual framework consultation. Use `Unverified` for an unrecovered basis.

The declaration supplies a traceable basis for feasible reconstruction. Source support and authorship remain separate checks. Present the full construction record for each synthesis decision; save the compact line after selection. Preserve originals needed by the trail and route the user's continuing directions to their established owners.

Source maps and established user originals identify their origin through their defined structures. Arc, index and tracker retain their planning and retrieval formats. Draft references the predraft's saved declarations.

## Structure and editing

Follow each module's headings and field order. Create files when their function has content. Include optional fields only where the module defines them and the content requires them.

Thesis, arc and draft use `Status: Working | Needs review | Approved`. Approved means the user accepted that exact content; Needs review marks changed correspondence. The draft becomes Complete when the user declares it finished. Predraft stores exact selected prose; unresolved candidates remain in the conversation.

For each edit:

1. Read current files and preserve the immediate pre-edit state in a temporary snapshot.
2. Keep user edits; capture identified new human wording and apply explicit decisions in their owners. Ask about ambiguous intent or origin.
3. After an accepted move, split or insertion, update positional numbers and dependent references together. Carry prose and authority with the claims they realise; ask about ambiguous correspondence.
4. Check exact wording, source context, argument coverage, basis codes, claim dependencies and links. Reconstruct from the bases where needed.
5. Update the tracker with actual progress and the outstanding question.

Link to section and paragraph headings. Identify a plain-text argument by its full number through its paragraph link. Heading anchors omit dots: `1.1 — Record` becomes `#11--record`.

Retain earlier exact wording while a saved provenance trail needs it. Preserve a direct user rewrite and update its bases and origin after checking the change.

During an authorised migration, preserve stable source/user IDs and required originals, route legacy material to these owners, and follow the user's retention instructions. Apply this skill's new schemas to project files within the requested migration scope.
