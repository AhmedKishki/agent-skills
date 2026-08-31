# White box synthesis

White box synthesis assembles an unselected chat candidate from existing Human wording. Every result span maps to a named original Human source or user message and changes, if at all, only through **INFLECT** below. Every adjacency between mapped result spans has original-source continuity or a stated Human basis, and every cut is disclosed.

Black-box synthesis is any result with an unmapped span, unsupported relation, hidden transformation, or fluent passage shown without its span map. It is prohibited.

Use this method for a requested suggestion, synthesis, content question, or predraft-report wording fix before global draft production. Never run it while producing the draft. If draft production exposes missing wording, reopen the report and affected arc or predraft work before attempting synthesis.

## Inputs and target

Only exact active Article-role source wording and exact user wording stamped **Human · 100%** are eligible. Mixed wording, reformulations, assistant output, and earlier syntheses are not. A draft or downstream file may help locate a span, but the span must resolve to its original Human basis. Every revision restarts from those bases plus any new Human wording. Similarity and adjacency supply nothing.

The inputs must supply every lexical item, claim, relation, scope, qualification, modality, and conclusion. They must also establish the target:

- body wording: paragraph, role, destination, entry, exit, and boundary;
- title or heading: heading row, placement, purpose, and boundary; or
- thesis, vision, or process candidate: function, purpose, and boundary.

Anything missing invokes the gap gate.

## Closed operations

Only four operations are permitted:

- **COPY:** reproduce one contiguous source or user-message span verbatim.
- **INFLECT:** change only tense, number, grammatical case, article, capitalisation, or an unambiguous pronoun to a referent already named in the same Human basis passage. Record before → after. The change must preserve meaning, relation, scope, qualification, modality, and emphasis. A synonym, modality or quantifier change, or hedge-to-claim conversion is invention.
- **ORDER:** place mapped COPY or INFLECT result spans in sequence. Record every adjacency between them and its Human basis; original continuity may cite the basis's original order.
- **DELETE:** remove only exact semantic repetition with the same subject, claim, scope, modality, and qualification. Record the removed span and what it repeated.

Do not atomise passages into word fragments to manufacture new phrasing. Never alter a quotation. Unless copied from an eligible span, insert no connective (such as *however*, *therefore*, or *while*), hedge, intensifier, topic/summary/closing sentence, or parallel construction made to create continuity. Human-established equivalence permits choosing an existing Human variant, never assistant substitution.

This closed list overrides the broader Human-preserving operation list while synthesis is running. Return to original Human wording; do not make a downstream assistant correction eligible by calling it Human-preserving.

Apply operative-metatheory tests without importing their wording. Framework-only material tests fit; it never supplies article words or relations.

## Method

1. **Collect:** identify each relevant eligible passage.
2. **Construct:** COPY or INFLECT spans, then ORDER them.
3. **Reduce:** DELETE only qualifying repetition.
4. **Verify:** build the span map; test the target, one linear Human-supported argument path, every adjacency and cut, quotation integrity, and operative-metatheory fit.

If a record or test cannot be completed from Human material, do not infer, rescan, ask a resolving question, or present a candidate in that turn. Use the gap gate.

## Gap gate

Show:

- **Target and consequence:** readable function/location, boundary, and what cannot be completed;
- **Established path:** each supported step and its full-name Human basis;
- **Exact gap:** missing word, claim, relation, scope, qualification, modality, conclusion, or target field;
- **Coverage:** sources and locators already checked, including partial or inaccessible limits; and
- **State:** **Synthesis stopped—no bridge supplied.**

Keep the point unresolved for that turn. Add no connector, infer no relation, and show no completed candidate. A later turn may rescan or obtain new Human wording under [collaborative questions](collaborative-questions.md), then restart from the original Human bases. A post-rescan AI gap suggestion is a separate unsupported proposal, never completion of the stopped synthesis.

## Visible record

Before the candidate, show every raw input passage once:

    | Input | Full source name or user's wording | Locator or user exchange in ordinary language | Raw Human passage, verbatim |
    |---|---|---|---|

Then show the final span map. One row covers each maximal contiguous result span with one input, basis span, and operation:

    | Result span, verbatim | Input | Human basis span, verbatim | COPY or INFLECT: exact change |
    |---|---|---|---|

Then show:

    - **Purpose:** readable function/location · role · boundary · starting point → intended result
    - **Input keys:** each Input → full source name or user's wording · ordinary-language locator or user exchange · all Human · 100%
    - **Ordering:** each mapped-span adjacency → original continuity or its stated Human basis
    - **Cuts:** each removed span → retained repetition and its Human basis, or none
    - **Argument path:** each step → its Human basis · unresolved jump or loop: none
    - **Metatheory fit:** none | full framework name · readable bases · function and fit · reader-facing framework wording: none
    - **Verification:** unmapped spans: 0 · outside-list changes: 0 · unsupported adjacencies: 0 · unsupported cuts: 0 · altered quotations: 0 · missing target fields: 0

    Exact final passage.

    **Origin:** Mixed · **Human wording:** 100% · **Method:** white box synthesis · **Based on:** full source names, ordinary-language locators, and the user's wording. Not selected for the article.

In chat, use full source names and plain descriptions; show no filename, timestamp, code, item ID, internal use, or workflow term. Any unfillable row or nonzero verification count invokes the gap gate instead of shipping the passage. The final white box record is **Input keys**, the span map, **Ordering**, **Cuts**, **Argument path**, **Metatheory fit**, and **Verification** above; the one-time raw-input display and purpose summary are not part of that record.

## Terminal output

The arrangement is assistant work, so it remains terminal **Mixed** even at 100% Human wording and is never a later synthesis input. A correction or revision also restarts from original Human bases and produces a new terminal result.

Selection creates a separate **Predraft raw material** copy; it never relabels the chat candidate. Copy only the exact result, final white box record, and this canonical stamp:

    **Provenance:** Mixed · Human wording: 100% · Method: white box synthesis · Basis: final record's Input keys · Use: Predraft raw material

Do not copy the raw-input display, chat stamp, purpose summary, or intermediate construction. The arc separately names the raw-material function and the predraft report separately names its finding or treatment; a process proposal separately names one field. User synthesis retains its actual Human/AI spans.

Never return a fluent result without its span map or a gap alert.
