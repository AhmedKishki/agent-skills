# Project memory

Maintain `{project}-memory-YYYY-MM-DD-HHMMSS.md` as the project-specific memory: the durable, human-readable store of the entities, observations, and relations the project has agreed on. Read it before working to recover state, arguments, concepts, and open questions; record agreed items during the session; update it at the end with what changed, new decisions, and next steps.

The file is the authoritative store and works with no memory server. If a memory MCP server is available it may mirror the same entities and relations, but reading and writing always go through `{project}-memory-YYYY-MM-DD-HHMMSS.md`; treat any server as an optional, disposable copy of this file, never a substitute for it.

## Entities, observations, relations

Memory is a small knowledge graph reduced to three parts:

- **Entity** — a named, reusable thing: the project, a section, an argument, a concept, a distinction, a decision, a source, or an open question. Each entity carries a `Type` label and a list of **observations**.
- **Observation** — one self-contained, dated fact, decision, or question attached to an entity. Keep it concise and structured (a bullet, a clear label). Store no raw draft prose; reference the owning file instead.
- **Relation** — a directed, active-voice link between two entities (`part of`, `governs`, `supports`, `precedes`).

Keep the file current, not historical: replace an outdated observation rather than stacking it, and retire a superseded entity.

## When to use it

- **Session start** — read the whole file, summarise the relevant state in three to five bullets, and ask the user to confirm or correct it before working.
- **During** — whenever the user and assistant agree on a thesis or central claim, a section structure, a key argument or example, a conceptual distinction, or an open question, record it immediately as an entity or observation.
- **Session end** — update the file with what changed in the draft, new decisions, and next steps and open questions.

## File shape

    # Writing memory

    **Exported:** date · **Source:** this file (authoritative)

    ---

    ## 1 · Group name

    ### Entity name
    *Type: article | structure | section | process | instruction | concept | question*

    - Observation one — dated.
    - Observation two — dated.

    ---

    ## Relations

    | From | Relation | To |
    |---|---|---|
    | Entity A | relationType | Entity B |

Group entities under numbered headings by theme. Use the `Type` label for the entity kind. The `Relations` table lists every relation between entity names.

Save and track the file per the [shared output-file standard](file-output-standard.md).
