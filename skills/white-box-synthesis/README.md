# White-Box Synthesis

Answers a query from the sources you supply, using only their wording and only the connections they state. A source can be a retrieval (RAG) result, a quotation, a passage, a note or your own writing.

The agent first plans the argument A → B → … → Z that answers the query and keeps only the source sentences that Z needs. It then writes a derivation: exact source spans and the operations applied to them (COPY, DELETE, ORDER, INFLECT and NORMALISE, each from a closed list). A bundled script replays the derivation and renders the reply, so the agent never types the reply's prose. Where Z needs a link that no source states, the reply shows `⟦GAP: X → Y: …⟧`. An AI-authored link appears only where you allow it, as `⟦AI-AUTHORED: …⟧`.

You get four parts: the synthesis, its references, minimal provenance and the agent's reasoning. The script checks the wording. The agent checks the meaning, including a check of the synthesis against each source in turn, as best it can. You judge adequacy.

## Use

Give the query and the sources together. For example:

> Use white-box-synthesis. Query: What happened to prices and incomes after the mill closed?
> S1: Lee, *Example Book*, p. 3: "…"
> S2: retrieval result, Diaz, *Sample Study*, ch. 2: "…"

Optional: draft text around where the reply will go (output context), spelling pairs for your house style, and permission to fill named gaps with AI links.

## Install

The entry point is [SKILL.md](SKILL.md). Install the complete directory so that `references/` and `scripts/` remain available. The script needs Python 3.8 or later and no packages. Without Python, the agent renders the reply by hand and says the wording check did not run.

Run the script's tests with `python3 tests/test_render.py` and `python3 tests/test_space.py`.
