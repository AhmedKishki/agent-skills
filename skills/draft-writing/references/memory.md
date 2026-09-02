# Project memory

Project memory is held in three stores, each owning a distinct kind of content. No fact has two homes: nothing is duplicated between them, and there is no mirroring or reconciliation.

- **The knowledge graph** — the project's own memory server, backed by `{project}-memory.jsonl` in the repo — owns drafts, arcs, sections, arguments, concepts, distinctions, examples, sources, decisions, the relations between them, and atomic observations about them.
- **`{project}-memory.md`** owns open questions with stable IDs (`Q1`, `Q2`, …) and long-lived research tasks.
- **`{project}-activity-tracker.md`** owns Now and Next, drafting-stage status, and anything actionable this session.

## The knowledge graph

The graph is the authoritative store for arguments, concepts, decisions, structures, and sources. Read and write it through the project's memory server tools (`search_nodes`, `open_nodes`, `create_entities`, `create_relations`, `add_observations`, `delete_observations`, `delete_relations`, `delete_entities`, `read_graph`). Commit `{project}-memory.jsonl` to the repo whenever the graph changes.

If the project's memory server is unavailable, report the configuration failure once, then continue from the repository files (the markdown memory, the tracker, and the source files). Never fall back to another memory server, and never invent remembered content.

### Entities, observations, relations

The graph reduces durable information to three parts:

- **Entity** — a named, reusable thing: a draft, arc, section, argument, concept, distinction, example, source, or decision. Names are lowercase kebab-case with a type prefix (for example `arc-seven-part`, `section-minerals`, `argument-the-machine-is-labour`, `concept-real-abstraction`, `source-valdivia`, `decision-energy-as-common-thread`); stable once created, no project prefix, no timestamps.
- **Observation** — one self-contained fact, decision, or status attached to an entity: one claim, one sentence. Anything longer belongs in the draft, not in memory. Record origin where it is not self-evident (approved by the user; derived from source X; the user's own synthesis).
- **Relation** — a directed, active-voice link between two entities (`contains`, `argues`, `depends_on`, `cites`, `illustrates`, `contrasts_with`, `revises`, `supersedes`). Create entities before relations; create a relation only where it improves future retrieval.

There is no `question` or `task` entity type — those live in the markdown memory. Keep the graph current, not historical: supersede rather than accumulate, and delete stale observations rather than silently overwriting a claim the user agreed to.

## `{project}-memory.md`

The markdown memory owns only open questions and research tasks, each with a stable ID. Question IDs (`Q1`, `Q2`, …) are never reused once a question closes. The markdown never restates an argument, structure, or relation that lives in the graph; a graph observation may point at a question by ID (for example "blocked by Q4") without restating the question text.

## `{project}-activity-tracker.md`

The tracker owns Now and Next, drafting-stage status, and anything actionable this session. It records current state; it never authorises the next module.

## When to use it

- **Session start** — read the tracker (Now/Next), the active thesis, arc, predraft/draft, and the markdown memory (questions and tasks); query the graph for the topic named in the request.
- **During** — whenever the user and assistant agree on a thesis or central claim, a section structure, a key argument or example, a conceptual distinction, or a decision, record it immediately in the graph. An open question or research task goes to the markdown memory.
- **Session end** — update the graph (what changed, new dependencies, decisions), the markdown memory (resolve or add questions, update research tasks), and the tracker (Now/Next).

## File shape — `{project}-memory.md`

    # Writing memory

    **Exported:** date · **Source:** this file (authoritative for open questions and research tasks)

    ---

    ## Open questions

    ### Q1 · short question title

    - The question, stated in one sentence.

    ## Research tasks

    - A long-lived research task, stated in one sentence.

Save and track the markdown file and the `.jsonl` per the [shared output-file standard](file-output-standard.md).
