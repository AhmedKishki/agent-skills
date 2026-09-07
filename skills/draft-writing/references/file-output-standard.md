# Shared file contract

## Owners and routing

Use stable `{project}-` filenames and edit in place. Each fact or decision has one authoritative home; dependent files refer to it.

| Content | Filename after the prefix |
|---|---|
| General picture, questions, specifications, accepted framework | `thesis-and-vision.md` |
| Exact reusable user article language | `user-wording.md` |
| Source identity, excerpt codes, locations, exact excerpts | `source-map-{code}-{author-short-title}.md` |
| Keywords, themes, excerpt retrieval assignments | `source-index.md` |
| Section, paragraph and sentence argument plan | `article-arc.md` |
| Approved paragraph prose, actual fragment uses, construction and selection | `predraft.md` |
| Reader-facing article and links to its paragraph records | `draft.md` |
| Working inventory, reading coverage, allocation counters, next action | `activity-tracker.md` |

Split a user message by function. Capture article language exactly in user wording; apply explicit general directions in thesis, structural decisions in arc, and exact prose selections in predraft. Route source leads to mapping. Execute procedural commands and omit their completed text from the article files.

Identified user-authored article language supplied in thesis, arc, predraft, draft or conversation also enters user wording as its original basis. Keep source quotations attributed to their source. Record actual incorporation once in predraft; its selected prose and the draft are derived outputs.

## Consent and provenance

Apply the [collaboration rule](../SKILL.md#collaboration) at every substantive choice. Present the exact candidate or change and ask for approval or comments. Keep an unanswered proposal distinct from accepted content. An explicit selection authorises saving that result and mechanically updating its references.

Preserve these distinctions:

- **Authorship:** original user wording, source wording, or assistant arrangement. Approval retains that origin.
- **Evidence:** what the original supports in context.
- **Selection:** the user's explicit acceptance of the particular result.

Use established human originals for article wording. Record uncertain or mixed origin in user wording's conditional `Origin:` field and obtain clarification before using the uncertain part. When evidence and the intended claim differ, explain the gap and ask the user how to proceed.

## Structure and editing

Follow each module's headings and field order. Create files when their function has content. Include optional fields only when needed. Use `Open: <specific question>` at the affected location for an unresolved choice.

Thesis, arc and draft use `Status: Working | Needs review | Approved`. Approved means the user accepted that exact content; Needs review marks changed correspondence. The draft becomes Complete when the user declares it finished. Predraft records use their own `Selection:` field.

For each edit:

1. Read current files and preserve the immediate pre-edit state in a temporary snapshot.
2. Keep user edits; capture identified new human wording and apply explicit decisions in their owners. Ask about ambiguous intent or origin.
3. Update dependent references after the accepted change. Carry prose and authority with their content when positional numbers change.
4. Check exact wording, source context, sentence-to-fragment correspondence, arrow relationships and links.
5. Update the tracker with actual progress and the outstanding question.

Retain earlier exact wording while a current record needs it. Preserve a direct user rewrite when its old record becomes stale; resolve the affected record before reuse.

During an authorised migration, preserve stable source/user IDs and required originals, route legacy material to these owners, and follow the user's retention instructions. Apply this skill's new schemas to project files within the requested migration scope.
