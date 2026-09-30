# Checklist

The instrument for `scripts/evaluate.py`. Semantic checks first: they are decisive. Surface checks come second and can only tip the scale.

Why this order. A generated passage and a written one can be identical in form — the same sentence lengths, the same punctuation, the same absence of repetition — and one of them can say nothing. Formatting cannot tell those apart. Meaning can. So the report supplies context windows, Part A asks whether the sentence means anything, and Part B asks whether its shape gives the reader away.

Two tests run under everything in Part A:

- **Can you say it back in plain words without it turning poetic?** If the literal version is empty, the sentence carries no meaning.
- **What does this add, and to what?** If the answer is nothing, or nothing in particular, the element is dead weight.

## A. Slop features

The six families, expanded. Each check gives what to look for, a test, and an example from this repository.

**A1 Vague referent.** A noun whose content the reader has to supply.

- **A1a The bare abstract noun.** *a boom, the expectation, the image, the rhetoric, the problem.* Point at it and ask what it contains. A category is not a thing.
- **A1b Comparison with an unstated term.** *further than the stock market, over X, more than before.* Compared with what, said where?
- **A1c Demonstrative standing in for a noun.** *That answer, This one states, It has reached the arsenal.* The pronoun points at something the reader cannot see.
- **A1d Plural with no members.** *the social relations, the ordinary relations* without saying whose or which.
- **A1e The collective that is not a collective.** *every large technology firm, nearly every company,* where the exception would matter.

> That answer now sits at the centre of a boom.
> Boom of what, and what does the answer have to do with its centre?

Compare, from the same section written by the author:

> The most valuable company in the world, Nvidia, with a $5.4tn market cap, has cashed in on Big Tech's AI aspirations (21 May 2026).

**A2 Metaphorical.** A figure doing work the literal words cannot.

- **A2a Figure standing in for a mechanism.** *get behind the fetishism, unlock the mysteries, open up the question.* What operation is this?
- **A2b Figure with no literal remainder.** Translate it back. If the plain version is empty, the figure carried nothing.
- **A2c The inherited figure.** A term the article has already defined, used as a figure, so the definition returns as a discovery. *The cloud is a metaphor for a physical place* restates the article's own premise as a finding.
- **A2d Process noun in place of an actor.** *the commodification of, the digitalisation of, the fetishism of.* A sentence with someone in it says more.
- **A2e Conduit metaphor.** *the flow of value, the web of relations, the chain of production,* where the article argues the relation is not a chain.

> Any sober assessment of what a technology might do for us has to get behind the fetishism of things.
> Get behind it by doing what?

**A3 Subject and verb mismatch.** The verb is carried by something that cannot do it.

- **A3a Abstraction as actor.** *the network names, the analysis makes visible, the relations produce* where a person or a mechanism would.
- **A3b The wrong valency.** *a set of relations is invoked: extraction, manufacturing, freight.* Extraction is not invoked; something invokes it.
- **A3c Collective noun with a member's action.** *capitalism decides, the market consumes, the system designates,* where the argument is about who inside it does it.
- **A3d Passive hiding the actor the sentence is about.** *waste is designated, data is labelled,* when the designating is the point.

> the network it names runs on data centres
> How does a network name?

**A4 Opened and closed.** A loop raised and tidied away, so the reader feels an insight that has not happened.

- **A4a The question that is not one.** Shaped as a question with no uncertainty in it, answered by the writer in the next clause.
- **A4b The frame resolved by the next sentence.** The second sentence restates the first in a shorter form.
- **A4c The verdict that closes nothing.** After *That is what defetishising AI comes down to*, is anything established that the opening did not contain?
- **A4d The exception that neutralises the claim it follows.** *even when it is a metaphor for data centres,* attached to a sentence that has already made the point.
- **A4e The escalation with no landing.** *It has reached the arsenal,* after a sentence about expectations.

> That expectation has already reached further than the stock market. It has reached the arsenal.
> The second sentence is the first one again.

**A5 Grandiose.** The topic made to sound larger than the claim.

- **A5a Scale without a figure.** *the most valuable company in the world* is a fact with a number and a puff without one.
- **A5b Importance by adjective.** *profoundly destructive, the unprecedented expansion, enormous volumes, the deep intermingling of.*
- **A5c The virtue frame.** *any sober assessment, we must get behind.* The reader is cast as insufficient for not already agreeing.
- **A5d The myth with a sting.** *Sovereign AI is a myth, and a useful one.* The cleverness is the content.
- **A5e The borrowed narrative.** *companies they are not supposed to be beating, the race for superintelligence,* where a trope stands in for the relation.
- **A5f Significance in place of a fact.** *this raises concerns around priorities for water use.* Name the concern.

Test: delete the adjective. Does the claim survive with the same force? If yes, the adjective was the argument.

**A6 Tell before show.** The text announces itself, its stakes or its structure before delivering anything.

- **A6a The roadmap.** *The last section named a method. This one states how I intend to carry it out.*
- **A6b The promise of later.** *named here once, briefly, and developed later where the relations that produce them are traced.*
- **A6c The stake-setting.** *it is worth being clear about what follows from this, because the opposite conclusion is common.*
- **A6d The announced suspicion or importance.** *The rhetoric that surrounds this deserves suspicion.*
- **A6e The self-description.** *the article's analysis defetishises, the purpose of the article is.*
- **A6f The topic announcement.** *The image of AI is a particular version of this.*
- **A6g The reaction told, not shown.** *which is a curious thing to read in an article about chatbots.* The reaction is reported as if it were a finding.

Test: delete the sentence. Does the next one still work? If it does, the sentence was a tell.

> The last section named a method. This one states how I intend to carry it out, because a reader who has been told about defetishism should not then have to guess.
> Delete the first two clauses and the paragraph is stronger. Car salesman showing the customer the car.

**A7 Reaction, elaboration and trope.** Not among the six families, but reported from the same pass and not to be dropped.

- **A7a Reaction asserted.** *a curious thing, a remarkable shift, a striking result,* where the reaction is offered as the evidence.
- **A7b Elaborating a question nobody asked.** *it is not simply the adversary.* The negative half answers an objection the text has not raised.
- **A7c The contrast that inflates.** *not merely X but Y* where the X is not a view anyone holds. Keep it when the negative half corrects a belief the reader does hold, which is most of the time in this article, and cut it when it is only there to make the positive half sound bigger.
- **A7d The narrative borrowed.** *the underdog, the race, the war,* standing in for a relation the article could state.

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

- a specific, unusual detail: a real address, an odd figure, a named person with a role
- a number with its period, its source and its date
- mixed feelings left unresolved
- a first-person choice the writer can explain
- a genuine aside, parenthetical or self-correction
- an era-bound reference: a meme, a dated phrase
- a question the writer has not answered yet

## How to use this

Read the document once before the script runs, so the first reading is not the report's. Then walk the report: the `## Sentences` section for Part A, the blocks and 3-grams for Part B, and one whole read for Part C.

Report Part A findings first and separately from Part C. A document can have no voice tells and several content defects, and reporting them as one number hides the fact that the prose is fine.

## Source

A1 to A7 were derived from the author's own classification of passages in this repository, blind to which were generated. A1, A2, A3, A6 and A7b come from the six families the author named: vague referent, metaphorical, subject/verb mismatch, opened and closed, grandiose marketing, tell before show. B and C adapt checks from [blader/humanizer](https://github.com/blader/humanizer) (MIT), which derives from Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), kept because formatting can tip a scale it cannot decide. A blind panel of eight evaluators, given the earlier 31-item version, rated generated passages cleaner than the author's own drafts: 4.3 tells per thousand words against 6.1. It was measuring editing residue, which is what a machine-written passage has none of.
