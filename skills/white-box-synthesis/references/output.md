# Output

## Shape

- Present the four parts in the order the script renders them: **Synthesis**, **References**, **Provenance** and **Reasoning**.
- Present the rendered text unchanged and add nothing inside it.
- When the request needs a reply the output cannot give, such as a request to remove markers, add a short note of chat after the output. That chat is the agent's wording and is never a source.

## Synthesis

- Every sentence ends with a marker naming each source it uses, such as `[S1]` or `[S1; S2]`.
- Gaps and allowed AI links appear inline, after the step whose link they mark.
- The synthesis has no heading, lead-in or closing summary. Each would be AI wording.
- Copied wording reads as prose with its marker. Follow the user's citation style where one is given.

## References

- One entry per source used or named in a gap, in order of first use, giving author, title and locator as supplied. An absent detail reads "not supplied".
- The source's note follows. Write a note only from what the user supplied. For a retrieval result, write "Retrieval result, wording not checked against the original".

## Provenance

- One line per sentence names each piece's source and its operations, or `verbatim`. A connective line names the link it realises.
- A sentence that states a deviation ends its line with `· DEVIATION: why`.
- One line per gap or AI link names the link and the sentence it follows.
- When the user asks for full provenance, show the derivation file.

## Reasoning

- Z in planning words, then the chain: each step, its sources, its link and why it is needed.
- The count of gaps and AI links on the chain. The sources establish Z only when the count is 0.
- Left out: sentences that bear on the query, each with its reason, and how many sentences of each source were copied. An antecedent's sentence is not counted.
- Conflicts and their effect on Z, one source check per source, each stated deviation with the rules it waived, or that no rule needed it, then notes.
- Whether the wording check ran.
- Reasoning is the agent's own wording. It explains decisions, never enters the synthesis and is never a source.

## The user's response

- To fill a gap, the user may give their own wording, a further source or permission for an AI link. Re-derive and re-render.
- The user's own wording enters as a new source, labelled as theirs.
- To change the synthesis, change the derivation. Never edit the rendered text.
- A request for a clean reply keeps every marker. Say so after the output and offer the ways to fill each gap.

## Worked example

- Lee, Diaz and both titles are hypothetical. They demonstrate the format and are not sources to cite.
- Query: What happened to prices and incomes in the town after the mill closed?
- S1: Lee, *Example Book*, p. 3: "As noted earlier, prices in the town rose sharply after the mill closed in 1990."
- S2: Diaz, *Sample Study*, ch. 2, a retrieval result: "Household incomes in the town fell by a third between 1990 and 1992."
- The derivation is `tests/fixtures/mill.json`. The script renders:

```markdown
**Synthesis**

Prices in the town rose sharply after the mill closed in 1990 [S1]. Household incomes in the town fell by a third between 1990 and 1992 [S2]. ⟦GAP: income fall from 1990 to 1992 (B) → after the mill closed (Z): no source places the fall after the closure or links it to the mill⟧

**References**

- [S1] Lee, *Example Book*, p. 3.
- [S2] Diaz, *Sample Study*, ch. 2. Retrieval result, wording not checked against the original.

**Provenance**

1. S1: DELETE "As noted earlier, " · NORMALISE case "p" → "P"
2. S2: verbatim
- After 2: GAP for B → Z

**Reasoning**

- Z: After the mill closed, prices in the town rose and household incomes fell.
- Chain:
  - A [S1] prices rose after the closure → Z (part), needed because it answers the prices part of the query and dates the rise after the closure. Link: none needed, part of the answer
  - B [S2] incomes fell 1990 to 1992 → Z (sequence), needed because it is the only claim about incomes. Link: gap, marked in the synthesis
- Gaps and AI links on the chain: 1. The sources establish Z only at 0.
- Left out:
  - S1: 1 of 1 sentences copied.
  - S2: 1 of 1 sentences copied.
- Conflicts:
  - None.
- Source checks:
  - S1: Keeps the rise, its degree and its date. Credits S1 with nothing about incomes.
  - S2: Keeps the figure and the period. The gap records that S2 does not mention the mill.
- Deviations:
  - None.
- Wording check: passed by scripts/render.py. Meaning checks: best effort.
```

- A connective such as "By contrast," would have been AI wording. The two sentences stand unconnected, and the one link Z needs is a gap.
