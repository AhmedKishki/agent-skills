# Article arc

Build the arc from the approved thesis-and-vision and whichever active source maps, user-synthesis, and selected predraft material are currently available. Begin with the approved main questions; add one only when the user agrees the thesis needs it. Leave what cannot yet be supported undecided and ask. Arc and predraft may alternate at the user's direction; neither complete artifact is a prerequisite for starting the other.

## Three scales

The arc maps the article at three scales, each giving a different level of detail:

- **Article** — the full scale: one arrow chain of sections in reading order.
- **Section** — the local scale: the question the section resolves, its goal, and its paragraphs as an arrow chain.
- **Paragraph** — the working scale: one numbered line per paragraph. Each paragraph is a single argument — one proposition — and is the exact target of one [white-box synthesis](white-box-synthesis.md) run.

The arrows carry position. Everything before a paragraph is already argued — do not repeat it; everything after it is still to come — do not anticipate it. A section's first paragraph builds from the previous section's last; its last prepares the next section's first. This is the context predrafting and synthesis work with: predrafting always happens at paragraph scale, with the section and article chains in view, so synthesis knows what already came and what is coming.

Number the sections in reading order and the paragraphs `section.number`, so 2.3 is the third paragraph of section 2. IDs are stable: never renumber or reuse one. An inserted section or paragraph takes the next unused number; the arrows, not the numbers, carry reading order.

Every paragraph makes one distinct contribution and every section serves a main question and the thesis. Each claim or list has one sole home; an intentional repetition needs a distinct function and exact user authority. Remove filler, loops, and excess scope only through the [removal-impact protocol](file-output-standard.md).

## Authority

Structure requires exact user wording or an exact selected proposal; sources establish contributions, never structure. A paragraph's named source items need active source-map entries with resolved roles; if support or its rescan is missing or stale, state that [source review](source-review.md) is required and stop. Metatheory fit is applied silently; Framework-only material is never an article contribution.

The arc carries structure and context only — no article wording, no copied source passages, no raw-material decisions. Titles and reader-facing headings are wording, decided in [predrafting](predraft.md) like any other wording. The predraft keys each selected passage to its paragraph ID.

The complete arc becomes **Approved** only when the user explicitly approves the whole file.

## File shape — `{project}-article-arc.md`

    # Article arc

    [Lean process header]

    **Arc structure and source-use decisions:** AI · Human wording: 0% · Method: structural proposal · Basis: the approved thesis-and-vision, the user-synthesis, and the active source-map items named per paragraph · Use: Process: article-arc structure only, not article wording

    **Exact source names:** Human · Human wording: 100% · Method: unchanged source wording

    **Thesis:** the exact thesis sentence

    ## Article

    Preface → Model → Data → Annotations → Data centre → Minerals → Conclusion

    ## Source key

    - A — full source name
    - B — full source name

    ## 1 · Section name

    **Question:** the main question the section resolves · **Goal:** its thesis contribution

    1.1 The paragraph's single argument, in one sentence (A1, B2) →
    1.2 The next argument (D3) →
    1.3 The closing argument

    ## 2 · …

A paragraph line is its proposition plus its named source items. Add a short em-dash note — a point of emphasis or an include/exclude boundary — only where synthesis genuinely needs it. List only the sources the arc actually uses. The section names above are illustrative.
