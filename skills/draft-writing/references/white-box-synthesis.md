# White box synthesis

White box synthesis assembles an unselected chat candidate from existing Human wording. Every result span maps to a named original Human source or user message and uses only the closed, disclosed operations below. Every adjacency between mapped result spans has original-source continuity or a stated Human basis, and every cut is disclosed.

Black-box synthesis is any result with an unmapped span, unsupported relation, hidden transformation, or fluent passage shown without its span map. It is prohibited.

Use this method for a requested suggestion, synthesis, content question, or predraft-report wording fix before global draft production. Never run it while producing the draft. If draft production exposes missing wording, mark the report and affected owner invalid, name the modules needed to resolve it, and wait for user direction before attempting synthesis.

## Inputs and target

Only exact active Article-role source wording and exact user wording stamped **Human · 100%** are eligible. Mixed wording, reformulations, assistant output, and earlier syntheses are not. A draft or downstream file may help locate a span, but the span must resolve to its original Human basis. Every revision restarts from those bases plus any new Human wording. Similarity and adjacency supply nothing.

The inputs must supply every substantive word, claim, relation, scope, qualification, modality, and conclusion. Permitted mechanical normalisation supplies no content. The inputs must also establish the target:

- body wording: exactly one arc move—its proposition, role, destination section, and entry, exit, and include/exclude boundary, taken from the move's arc row;
- title or heading: heading row, placement, purpose, and boundary; or
- thesis, vision, or process candidate: function, purpose, and boundary.

Run one synthesis per move, never several moves in one run. The move row's named Article-role source items define the source collection scope; thesis-and-vision, user-synthesis, and user-message wording remain eligible under the same rules. If the move row or its rescan is missing or stale, the target is not established: state that the [article arc](article-arc.md) or [source review](source-review.md) is required and stop. If the target could support materially different meanings or uses, ask one clarifying question before synthesis. Once the target is established, apply the substantive gap test below.

## Closed operations

Only five operations are permitted:

INFLECT and NORMALISE apply only to unquoted result text. Neither may alter direct quotations, raw-input or Human-basis displays, code, URLs, source titles, citation data, or the spelling or wording of proper names, trademarks, official organisation or product names, and defined terms. Change protected names' capitalisation only when unambiguous and meaning-neutral.

- **COPY:** reproduce one contiguous source or user-message span verbatim.
- **INFLECT:** change only tense, number, grammatical case, article, or an unambiguous pronoun to a referent already named in the same Human basis passage. Preserve meaning, relation, scope, qualification, modality, and emphasis. A synonym, modality or quantifier change, or hedge-to-claim conversion is invention.
- **NORMALISE:** correct unambiguous spelling, convert American to British spelling, or make a meaning-neutral capitalisation or punctuation change. This does not permit vocabulary or grammar substitution.
- **ORDER:** place mapped COPY, INFLECT, or NORMALISE result spans in sequence. Record every adjacency between them and its Human basis; original continuity may cite the basis's original order.
- **DELETE:** remove only exact semantic repetition with the same subject, claim, scope, modality, and qualification. Record the removed span and what it repeated.

Do not atomise passages into word fragments to manufacture new phrasing. Unless copied from an eligible span, insert no connective (such as *however*, *therefore*, or *while*), hedge, intensifier, topic/summary/closing sentence, or parallel construction made to create continuity. Human-established equivalence permits choosing an existing Human variant, never assistant substitution. If a possible normalisation is ambiguous or meaning-changing, retain the original form and ask only if it blocks the candidate; invoke the gap gate only under its substantive test below.

For a result span changed by INFLECT, NORMALISE, or both, record one exact original → final pair and list the applied text operations. Do not repeat the pair per operation. Give each changed occurrence a readable location; write punctuation insertion as ∅ → mark and deletion as mark → ∅. Record ORDER only under **Ordering** and DELETE only under **Cuts**.

This closed list overrides the broader Human-preserving operation list while synthesis is running. Use original Human wording as the basis and make only these disclosed changes; do not make a downstream assistant correction eligible by labelling it Human-preserving.

Apply operative-metatheory tests without importing their wording. Framework-only material tests fit; it never supplies article words or relations.

## Method

1. **Collect:** identify each relevant eligible passage within the move's named source items and other eligible Human wording.
2. **Construct:** COPY, INFLECT, or NORMALISE spans, then ORDER them.
3. **Reduce:** DELETE only qualifying repetition.
4. **Verify:** build the span map; test the target, one linear Human-supported argument path, every adjacency and cut, quotation integrity, every mechanical-change disclosure, and operative-metatheory fit.

Fix an incomplete change record before showing the candidate. If traceability cannot be restored, stop and report a provenance failure, not a synthesis gap. When the substantive gap test passes, do not infer, rescan, ask a resolving question, or present a candidate in that turn.

## Gap gate

A gap is blocking only when completing the established target would require missing substantive content, an unsupported semantic relation, or choosing between unresolved meaning-bearing alternatives. A meaning-neutral mechanical correction or style choice, or a record defect, is not a synthesis gap.

Show:

- **Target and consequence:** readable function/location, boundary, and what cannot be completed;
- **Established path:** each supported step and its full-name Human basis;
- **Exact gap:** missing substantive wording, premise, claim, definition, semantic connection, scope, qualification, modality, conclusion, or unresolved meaning-bearing choice within the established target;
- **Coverage:** sources and locators already checked, including partial or inaccessible limits; and
- **State:** **Synthesis stopped—no bridge supplied.**

Keep the point unresolved for that turn. Add no connector, infer no relation, and show no completed candidate. In a later turn the user may request a [source review](source-review.md) or supply new Human wording under [collaborative questions](collaborative-questions.md). Then suggest resuming white-box synthesis or the originating module and wait for user direction; any new attempt restarts from the original Human bases. A post-rescan AI gap suggestion is a separate unsupported proposal, never completion of the stopped synthesis.

## Visible record

Before the candidate, show every raw input passage once:

    | Input | Full source name or user's wording | Locator or user exchange in ordinary language | Raw Human passage, verbatim |
    |---|---|---|---|

Then show the final span map. One row covers each maximal contiguous result span with one input, basis span, and its text operation:

    | Result span, verbatim | Input | Human basis span, verbatim | COPY, INFLECT, and/or NORMALISE · readable result location · one exact original → final change, or unchanged |
    |---|---|---|---|

The span map plus **Ordering** and **Cuts** below is the user's change alert; do not add a duplicate summary.

Then show:

    - **Purpose:** readable function/location · role · boundary · starting point → intended result
    - **Input keys:** each Input → full source name or user's wording · ordinary-language locator or user exchange · all Human · 100%
    - **Ordering:** each mapped-span adjacency → original continuity or its stated Human basis
    - **Cuts:** each removed span → retained repetition and its Human basis, or none
    - **Argument path:** each step → its Human basis · unresolved jump or loop: none
    - **Metatheory fit:** none | full framework name · readable bases · function and fit · reader-facing framework wording: none
    - **Verification:** unmapped spans: 0 · outside-list changes: 0 · undisclosed permitted changes: 0 · unsupported adjacencies: 0 · unsupported cuts: 0 · unpermitted protected-text changes: 0 · missing substantive target decisions: 0

    Exact final passage.

    **Origin:** Mixed · **Human wording:** 100% · **Method:** white box synthesis · **Based on:** full source names, ordinary-language locators, and the user's wording. Not selected for the article.

In chat, use full source names and plain descriptions; show no filename, timestamp, code, item ID, internal use, or workflow term. Do not ship with an unfillable row or nonzero verification count. Report missing traceability as a provenance failure; invoke the gap gate only under its substantive test. The final white box record is **Input keys**, the span map, **Ordering**, **Cuts**, **Argument path**, **Metatheory fit**, and **Verification** above; the one-time raw-input display and purpose summary are not part of that record.

## Terminal output

The arrangement is assistant work, so it remains terminal **Mixed** even at 100% Human wording and is never a later synthesis input. Disclosed NORMALISE forms remain Human wording; punctuation does not affect the word percentage. A correction or revision also restarts from original Human bases and produces a new terminal result.

Selection creates a separate **Predraft raw material** copy keyed to its move (exact move ID and readable title); it never relabels the chat candidate. Copy only the exact result, final white box record, and this canonical stamp:

    **Provenance:** Mixed · Human wording: 100% · Method: white box synthesis · Basis: final record's Input keys · Use: Predraft raw material

Do not copy the raw-input display, chat stamp, purpose summary, or intermediate construction. The arc separately names the raw-material function and the predraft report separately names its finding or treatment; a process proposal separately names one field. User synthesis retains its actual Human/AI spans.

Never return a fluent result without its complete span map. If no result can be returned, report the substantive gap, provenance failure, or verification failure under the rules above.
