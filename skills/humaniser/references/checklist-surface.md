# Checklist: surface, mechanical faults and sources

Parts B and C of the checklist, what to keep and where the items come from. Part A is in [checklist.md](checklist.md) and [checklist-wording.md](checklist-wording.md).

## B. Surface

These cannot decide anything on their own. A generated passage passes all of them. They matter when a semantic check has already found the sentence thin and a surface habit confirms the diagnosis.

- **B1 One frame across blocks.** The same opening, field labels or closing clause in a run of blocks. Test: the first three words of each block. `bold label openings` in the report gives the count.
- **B2 Repeated clause.** A span repeated verbatim where the second copy adds nothing. The 3-gram list is the only reliable way to see it.
- **B3 The same claim three times.** A rule or definition stated in an overview, its own block, and again at the close.
- **B4 Bold as decoration.** Bold with no reason, or a list giving every item a bold label and a colon.
- **B5 Forced triads.** Three where the meaning has two or four.
- **B6 Dashes as the universal join.** One per sentence stops reading as a choice. Match the author's rate rather than removing them.
- **B7 Semicolon-joined imperatives.** A register rather than a sentence: 10 or more per thousand words marks agent-facing prose.
- **B8 Repeated sentence openings.** Consecutive sentences starting the same way. The 3-gram list shows it.
- **B9 Repeated block openings.** *The, The, The.* Legitimate as a rhythm and a tell as a habit.
- **B10 Knowledge-limit hedging.** *as of publication, recent reports suggest, it is believed that.* State what the source does not show, or cut the sentence.
- **B11 The heading restated by its first block.** Cut the block.
- **B12 Writing about the document.** A legend, an order, a note about what was assembled. Keep a caveat that changes what the reader should do.
- **B13 Hyphenation.** The compound keeping its hyphen after the noun. A *missing* hyphen is a copy fault, not this item.

## C. Mechanical and provenance faults

Not voice. A reader trips on them whatever wrote the sentence, and they concentrate in files that have been edited, which is why a working draft carries more of them than a generated one. Report them under this heading and do not mix them into a voice score.

- **C1 A figure stated two ways.** *hundreds of suppliers* and *tens of thousands of suppliers,* four sentences apart, with nothing saying they count different tiers.
- **C2 A footnote carrying two unrelated figures.**
- **C3 Footnote anchors out of sequence.** The number is supposed to be the order.
- **C4 A locator pointing at the wrong source.**
- **C5 Two names for one thing.** *the Democratic Republic of the Congo* and *the Democratic Republic of Congo* in one file.
- **C6 A key term reversing its word order.** *waste data* and *data waste.*
- **C7 A subject that cannot do its verb in a factual sentence.** A similarity cannot equate things.
- **C8 A number with no period attached,** so the ratio the sentence exists to establish cannot be checked.
- **C9 An unanchored referent at a pivot,** where the reader cannot tell which of two things just mentioned is meant.
- **C10 A broken contraction or agreement,** the result of a bad edit: *is n't* for *isn't*, *All of these chains are the necessary condition* for four chains.

## What to keep

A checklist that removes every tell removes the writer. These are load-bearing and no item above touches them:

- a specific, unusual detail: a real address, an odd figure or quote, a named person with a role
- a number with its period, its source and its date
- mixed feelings left unresolved
- a first-person choice the writer can explain
- a genuine aside, parenthetical or self-correction
- an era-bound reference: slang, memes, dated phrases, in-jokes that map to a year
- a question the writer has not answered yet

## Source

A1 to A7 were derived from the author's own classification of passages in this repository, blind to which were generated. A1, A2, A3, A6 and A7b come from the six families the author named: vague referent, metaphorical, subject/verb mismatch, opened and closed, grandiose marketing, tell before show. B and C adapt checks from [blader/humanizer](https://github.com/blader/humanizer) (MIT), which derives from Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), kept because formatting can tip a scale it cannot decide. A blind panel of eight evaluators, given the earlier 31-item version, rated generated passages cleaner than the author's own drafts: 4.3 tells per thousand words against 6.1. It was measuring editing residue, which is what a machine-written passage has none of.
