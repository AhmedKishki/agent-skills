# Authorship and wording provenance

For every substantive passage, suggestion, reformulation, source-contribution statement, and synthesis in chat or a content file, track:

- **Human wording:** percentage traceable to exact source/user wording or a word form changed only by a Human-preserving operation.
- **Origin:** **Human**, **Mixed**, or **AI**, plus actual method, basis, and any controlled use.

Source and user wording is Human. Omission markers are not words. Assistant wording remains AI after selection; assistant reductive synthesis remains Mixed even at 100% Human wording. Only user replacement spans become Human. Provenance does not prove source fidelity; apply [source-map](source-maps.md) meaning tests.

## Inheritance and stamps

Declare uniform fields once at the widest scope. A declaration below the title covers the file; below a heading, that section until the next heading of equal/higher level; in a row, that row. Every covered sentence and substantive label inherits it.

    **Content authorship:** Human · Human wording: 100% · Method: shared method · Basis/Use: supplied by each heading, item, or compact map

Per item add only basis/use not supplied by the declaration. A local stamp covers only the preceding passage/row. Record only differing fields in an exception; use a full stamp only without inheritance:

    **Provenance:** Human | Mixed | AI · Human wording: P% · Method: operation · Basis: readable exact references · Use: exact current use
    **Provenance exception:** differing fields only · Basis/Use: local values

Split exceptions when a field changes. Count whitespace-separated reader-facing words; exclude Markdown/citation markers, keep hyphenated/apostrophised words whole, count traceable spans once, and round to one decimal. Human passages are 100%. **Unresolved** blocks migration dependents.

**Process prose: AI** without a percentage covers only process headings, fixed labels, question framing, and non-substantive notes. Reader-facing headings, proposed content, role assignments, and explanations are substantive. **Basis** names each source item and user exchange. Map draft prose in its appendix. Only the requested [source export](export.md) omits provenance; the [user export](user-export.md) preserves it.

## Exact uses

Internally record the exact canonical version and use. In chat show only the exact wording/decision and its plain-language function or article location—never filename, timestamp, code, item ID, workflow label, or internal status. Predraft selection, draft placement, or Mixed/AI process use requires explicit assent to that display; silence, continuation, praise, milestone approval, or assent to another use does not count.

Route Human wording automatically only when it passes [faithful routing](file-output-standard.md) and names one thesis-and-vision, user-synthesis, source-map, or arc function; ask if several fit. Any arc addition/change affecting structure, boundary, meaning, role, or use first follows the substantive-change rule. Routing never selects predraft/draft use. Each canonical copy has one use: **Chat candidate only**; **Thesis-and-vision: heading**; **User-synthesis: heading**; **Source map: item**; **Predraft raw material**; **Draft: section and paragraph**; **Process: file and field**; **Rejected**; or **Unresolved**. Predraft and draft copies keep separate uses; the arc controls placement. Use changes neither origin, fidelity, nor synthesis eligibility.

## Human-preserving operations

Without asking: remove a selected duplicate or explicitly rejected/withdrawn/superseded wording; move an intact cleared block to its selected destination; or correct spelling, grammar, tense, inflection, number, agreement, capitalisation, punctuation, paragraphing, citation markers, and meaning-neutral word order. Add no lexical content or change meaning, relation, scope, qualification, or emphasis. Never alter quotations, delete unique active wording, or choose between differing alternatives. Record the method in the canonical passage before reuse; origin and use remain.

If an operation needs a word, connector, heading, explanation, relation, synthesis, combination, or new order, pause and follow [reductive synthesis](reductive-synthesis.md) or ask.

## Draft metrics

The draft appendix reports total, Human, and AI article words and percentages. Count title, reader-facing headings/body/notes; exclude citations' metadata and the appendix. Passage and total figures must agree. Target zero AI words.
