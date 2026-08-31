# Authorship and wording provenance

For every substantive passage, suggestion, reformulation, source-contribution statement, and synthesis in chat or a content file, track:

- **Human wording:** percentage traceable to exact source/user wording or a word form changed only by a Human-preserving operation.
- **Origin:** **Human**, **Mixed**, or **AI**, plus actual method, basis, and any controlled use.

Source and user wording is Human. Omission markers are not words. Assistant wording remains AI after selection; assistant white box synthesis remains Mixed even at 100% Human wording. Only user replacement spans become Human. Provenance does not prove source fidelity; apply [source-map](source-maps.md) meaning tests.

## Inheritance and stamps

Declare uniform fields once at the widest scope. A declaration below the title covers the file; below a heading, that section until the next heading of equal/higher level; in a row, that row. Every covered sentence and substantive label inherits it.

    **Content authorship:** Human · Human wording: 100% · Method: shared method · Basis/Use: supplied by each heading, item, or compact map

Per item add only basis/use not supplied by the declaration. A local stamp covers only the preceding passage/row. Record only differing fields in an exception; use a full stamp only without inheritance:

    **Provenance:** Human | Mixed | AI · Human wording: P% · Method: operation · Basis: readable exact references · Use: exact current use
    **Provenance exception:** differing fields only · Basis/Use: local values

Split exceptions when a field changes. Count whitespace-separated reader-facing words; exclude Markdown/citation markers, keep hyphenated/apostrophised words whole, count traceable spans once, and round to one decimal. Human passages are 100%. **Unresolved** blocks migration dependents.

**Process prose: AI** without a percentage covers only process headings, fixed labels, question framing, and non-substantive notes. Reader-facing headings, proposed content, role assignments, diagnostic explanations, and suggested fixes are substantive. **Basis** names each source item and user exchange. Map draft prose and approved global operations in its appendix. [Combined sources](combine-sources.md) and [full export](full-export.md) preserve their input files and provenance unchanged.

## Exact uses

Internally record the exact canonical version and use. In chat show only the exact wording/decision and its plain-language function or article location—never filename, timestamp, code, item ID, workflow label, or internal status. Predraft selection, predraft-report treatment/exception approval, draft use, or Mixed/AI process use requires explicit assent to that display; silence, continuation, praise, milestone approval, or assent to another use does not count.

Route Human wording automatically only when it passes [faithful routing](file-output-standard.md) and names one thesis-and-vision, user-synthesis, source-map, or arc function; ask if several fit. Any arc or report addition/change affecting structure, boundary, emphasis, meaning, role, treatment, exception, or use first follows the substantive-change rule. Routing never selects predraft/report/draft use. Each canonical copy has one use: **Chat candidate only**; **Thesis-and-vision: heading**; **User-synthesis: heading**; **Source map: item**; **Predraft raw material**; **Predraft report: finding/treatment/exception**; **Draft: section and span**; **Process: file and field**; **Rejected**; or **Unresolved**. Predraft, report, and draft uses remain separate; the arc controls structure and the report controls approved global treatments. Use changes neither origin, fidelity, nor synthesis eligibility.

## Human-preserving operations

Before complete-predraft approval, correct spelling, grammar, tense, inflection, number, agreement, capitalisation, punctuation, paragraphing, citation markers, and meaning-neutral word order without asking. Moving an intact cleared block or removing a selected duplicate or rejected/withdrawn/superseded wording is Human-preserving only after the exact removal impact has been shown and authorised under [file-output-standard.md](file-output-standard.md). A direct user removal request authorises only its exact target. Add no lexical content or change meaning, relation, scope, qualification, or emphasis. Never alter quotations, delete unique active wording, or choose between differing alternatives. Record the method in the canonical passage before reuse; origin and use remain.

After the complete predraft is approved, apply no report-identified correction automatically: show one exact suggested fix and obtain explicit approval even if the operation would otherwise be Human-preserving. These general operations do not expand white box synthesis's closed **INFLECT** list or make a downstream assistant correction an eligible synthesis input. Never apply them directly to a white-box-derived predraft passage: restart from its original Human bases, produce a new terminal candidate and final record, and obtain new selection/removal authority before replacement.

If an operation before global draft production needs a new word, connector, heading, explanation, semantic relation, or reformulated article passage, follow [white box synthesis](white-box-synthesis.md); do not bypass its same-turn gap gate by asking or proposing. Exact report-approved adjacency, combination, cutting, or consolidation of intact predraft spans within an already approved arc destination is instead a global arrangement operation: it may add no word or semantic relation and must retain its exact report authority in the draft map. Assistant arrangement makes Human input Mixed; input that was already AI remains AI. During draft production, stop and name the affected canonical owner and **review-predraft** requirement; return control instead of inventing an operation or starting another function.

## Draft metrics

The draft appendix reports total, Human, and AI article words and percentages. Count title, reader-facing headings/body/notes; exclude citations' metadata and the appendix. Passage and total figures must agree. Target zero AI words.
