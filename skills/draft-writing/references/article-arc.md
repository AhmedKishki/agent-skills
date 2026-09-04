# Article arc

Build the arc from a general overview of the active source maps and the user's wording — the approved thesis-and-vision, the user-synthesis, and whichever selected predraft material is currently available. Begin with the approved main questions; add one only when the user agrees the thesis needs it. Leave what cannot yet be supported undecided and ask. Arc and predraft may alternate at the user's direction; neither complete artifact is a prerequisite for starting the other.

The arc is always a sketch, not a rigorous file: it does not identify specific fragments, and it does not aim to fix which fragment supports which claim. It is a dynamic document — modified as predrafting and drafting proceed; revision is expected.

## The scales

The arc maps the article by decomposing it into its constitutive elements. The vocabulary is fixed: **article → section → paragraph → sentence → fragment**.

- **Article** — the full scale. The article's claim is the thesis; the article is one arrow chain of sections in reading order.
- **Section** — supports the thesis: the question the section resolves, its goal, and its paragraphs as an arrow chain.
- **Paragraph** — makes one claim supporting its section; the exact target of one [white-box synthesis](white-box-synthesis.md) run; synthesised from its sentences.
- **Sentence** — the constitutive element of a paragraph: one numbered line stating a proposition that supports the paragraph's claim.
- **Fragment** — the smallest unit, and the material the arc does not hold: exact source-map excerpts and user wording. Synthesis finds fragments and composes them into sentences, and sentences into paragraphs.

The arc phase resolves the decomposition: sections into paragraphs, paragraphs into their sentences. The document order carries position. Everything before a paragraph is already argued — do not repeat it; everything after it is still to come — do not anticipate it. A section's first paragraph builds from the previous section's last; its last prepares the next section's first. Predrafting and synthesis work with the paragraph in view of the section and article chains, so synthesis knows what already came and what is coming.

Number the sections in reading order, paragraphs `section.paragraph`, and sentences `section.paragraph.sentence` — so 2.3 is the third paragraph of section 2 and 2.3.1 its first sentence. The scheme continues globally to fragments — `section.paragraph.sentence.fragment`, so 2.3.1.2 is the second fragment supporting sentence 2.3.1 — but the arc holds no fragments: fragment IDs live in the records that hold them (the predraft's production records) and shift as synthesis choices shift. IDs are stable: never renumber or reuse one. An inserted section, paragraph, or sentence takes the next unused number; the document order, not the numbers, carries reading order.

Every paragraph's claim is one distinct contribution, every sentence supports its paragraph's claim, and every section serves a main question and the thesis. Each claim or list has one sole home; an intentional repetition needs a distinct function and exact user authority. Remove filler, loops, and excess scope only through the [removal-impact protocol](file-output-standard.md).

## Revision at any stage

The user may revise the arc at any stage, including mid-drafting. On revision, apply the [unaffected-work test](file-output-standard.md) to everything built on the arc — predraft coverage, the predraft report, the draft — mark affected work invalid, name the required modules, and wait for user direction.

## Authority

Structure requires exact user wording or an exact selected proposal; sources establish contributions, never structure. Metatheory fit is applied silently; Framework-only material is never an article contribution.

The arc carries structure and context only — no article wording, no copied source passages, no fragment citations, no raw-material decisions. Titles and reader-facing headings are wording, decided in [predrafting](predraft.md) like any other wording. The predraft is a raw-material pool, not keyed paragraph-by-paragraph to the arc; each selected passage names the arc elements it covers.

The complete arc becomes **Approved** only when the user explicitly approves the whole file; revisions follow the revision rule above.

## File shape — `{project}-article-arc.md`

    # Article arc

    [Lean process header]

    **Arc structure:** AI · Human wording: 0%

    **Exact source names:** Human · Human wording: 100%

    ## Article

    **Thesis:** the exact thesis sentence

    Section 1 claim → section 2 claim → …

    ## 1 · Section name

    **Question:** the main question the section resolves · **Goal:** its thesis contribution

    ### 1.1 The paragraph's claim

    1.1.1 A sentence supporting the claim

    1.1.2 The next sentence

    ### 1.2 The next paragraph's claim

    1.2.1 A sentence

    ## 2 · …

A section is an H2 heading; a paragraph's claim is an H3 heading (`### section.paragraph`); each sentence is a plain numbered line stating its proposition — the document order carries the reading sequence. Add a short em-dash note — a point of emphasis or an include/exclude boundary — only where synthesis genuinely needs it. List only the sources that inform the sketch. The section names above are illustrative.
