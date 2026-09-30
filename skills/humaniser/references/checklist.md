# Checklist

The instrument for `scripts/evaluate.py`. Each check names the part of the report it consumes, so the walk follows the report's own order rather than this file's grouping.

## Pass index

| Walk this | From the report | Then apply |
|---|---|---|
| 1. Counts | the header: `cv`, semicolons, em-dashes, questions, `bold label openings`, `curly quotes` | §8, §19, §21, §29 |
| 2. Blocks | the `## Blocks` section: every block with the blocks beside it | §2, §20, §24, §25, §27 |
| 3. Sentences | the `## Sentences` section: every sentence with its phrases and its block | §1, §3–§7, §9–§18, §22, §23, §26 |
| 4. Phrases | `--level phrase`, narrowed with `--lines` to blocks step 3 flagged | §1, §6, §14, §15 |
| 5. 3-grams | the `## 3-grams` section, computed across every file in the run | §28, §31 |
| 6. Whole document | read it once end to end | §27, §30 |

A pattern is a default choice, not a proof. A person can make any one of them on purpose. Act on one sighting for §1–§5; items marked *weak alone* need company from other tells in the same block. Several tells together are the safeguard.

Do not act on a watched phrase inside a quotation, a title, a proper name, a code span, or a passage that discusses the phrase rather than uses it. This matters more here than in prose, because a document about AI voice quotes those words on purpose.

## A. Staging instead of stating

The strongest and most frequent tells. Act on one sighting.

**§1 Not X but Y** — *sentences, phrases.* `not X but Y`; `not just`, `not only`, `not merely X, but Y`; `it's not X, it's Y`; the reversed `X rather than Y`; the same contrast split across sentences ("This does not mean X. It means Y."); a clipped negative tail ("…, no guessing"). The negative half names something no one claimed, so the positive half sounds larger. Keep a contrast only when the negative half corrects a belief the reader actually holds, or when both halves carry information. Split across two blocks, the report gives you the negative in one and the positive in the other.
> Before: It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere.
> After: The heavy beat adds to the aggressive tone.

**§2 One-line closers and fragments** — *blocks.* A one-sentence block that restates the block before it; "That is the real win."; "That distinction matters."; "Let that sink in."; the same closer after several blocks; a sentence after an example that names what the example showed ("This shows the importance of…", "The message was clear:"); a row of fragments ("No aesthetic prior. No nostalgia."). One short sentence can carry emphasis when it carries a new fact. Cut a closer that repeats.

**§3 Sayings that sound deep** — *sentences.* `the real question is`, `at its core`, `in reality`, `what really matters`, `fundamentally`, `the deeper issue`, `the heart of the matter`, `X is the Y of Z`, `X becomes a trap`, `X is not a tool but a mirror`, `the language of`, `the currency of`, `the architecture of`. An ordinary point dressed as a hidden truth. Replace the saying with the specific claim.

**§4 Staged run-up** — *sentences.* `Let's dive in`, `let's explore`, `let's break this down`, `here's what you need to know`, `now let's look at`, `without further ado`, `heads up`, `quick note`, `Honestly?`, `Look,`, `Here's the thing`, `Real talk`. The writer announces the point or stages a moment of candour. Remove the run-up, not just its tone. A "look" inside a sentence is ordinary; the tell is the standalone opener before a routine claim.

**§5 Arguing with no one** — *sentences.* `This isn't (mainly) about`, `I'm not saying`, `To be clear`, `Don't get me wrong`, `This is not to say`, `Some might say… but`, `A tempting approach would be`, `One might be tempted to`, `You might think… but`, `It would be easy to just`. The text rejects an option that appears nowhere else, usually a leftover from an earlier draft. Several unrelated rejections in a row are a stronger sign than one.

## B. Rhythm by rule

**§6 Forced triads** — *sentences, phrases.* Three items where the meaning has two or four, at sentence or block scale. The phrase pass shows the three items as separate units with their context, which is where you see whether each adds a distinct idea. Three real items are fine.
> Before: A career can look promising and fail. A relationship can feel important and end. A skill can take years and remain useless.
> After: A career can look promising and fail. So can a relationship that felt important and ended, or a skill that took years and remained useless.

**§7 Repeated sentence openings** — *sentences.* Consecutive units in the report start with the same subject or the same first word. Do not ban the word; a remaining sentence may still start with "She."

**§8 Dashes as the universal connector** — *counts, sentences.* Start from the `em-dashes` count in the header, then read the sentences that contain one. Replace with a period, comma, colon or parentheses where the relation allows. *Weak alone* — many editors use dashes — but a high count is not. If the author's own prose uses dashes, match its rate rather than removing them.

**§9 Stacked qualifiers** — *sentences.* `to be fair`, `it's also possible`, `could potentially`, `might arguably`, `in some cases it may`, `this is an inference`. Repeated editing adds one qualifier until every claim sounds uncertain. Keep a qualifier the source supports. Ordinary hedges such as *perhaps* are human habits, not tells. *Weak alone.*

**§10 Hyphenated pairs everywhere** — *sentences.* The compound keeps its hyphen after the noun: "a high-quality report" is right, "the report is high-quality" is the tell. Words the dictionary always spells with a hyphen keep it everywhere. *Weak alone.*

**§11 Passive voice and missing subjects** — *sentences.* The text hides who acts, or drops the subject ("No configuration file needed"). Use active voice when it names the actor more clearly. *Weak alone.*

## C. Inflation and borrowed authority

The fact underneath is usually sound. Keep it and remove the dressing.

**§12 Overused words** — *sentences.* `Actually, additionally, align with, bolstered, crucial, deep dive, delve, enduring, enhance, garner, gated (figurative), highlight (verb), interplay, intricate, key (adjective), landscape (abstract), meticulous, pivotal, quietly, robust (figurative), showcase, tapestry, testament, underscore (verb), valuable, vibrant`. Models use these far more often than people do, especially in groups. A formal word outside this list is not a tell by itself.

**§13 Inflated significance** — *sentences.* `stands as a testament`, `a pivotal or crucial moment`, `plays a key role`, `marking or shaping the`, `underscores its importance`, `a broader, enduring legacy`, `setting the stage for`, `evolving landscape`, `Despite these challenges… continues to thrive`, and stock `Challenges and Legacy` / `Future Outlook` send-offs. Keep the fact, drop the significance, end on the last concrete fact.

**§14 Vague connection** — *sentences, phrases.* `associated with`, `in association with`, `connected to`, `in connection with`, `linked to`, `tied to`, said without saying how. "He was associated with the leadership of ExampleCorp" hides whether he was CEO, board member or consultant. Name the relationship the source gives; if the source does not say, keep the vague wording rather than inventing a role.

**§15 Shallow -ing riders** — *phrases.* `highlighting`, `underscoring`, `emphasizing`, `ensuring`, `reflecting`, `symbolizing`, `contributing to`, `cultivating`, `fostering`, `encompassing`, `showcasing`. An -ing phrase bolted onto a simple fact to sound deeper. The phrase pass isolates the rider from the fact it is attached to, which is where you see the join. Attaching it to a named source does not make it true. Keep the rider only when the source supports what it claims.

**§16 Sales language** — *sentences.* `rich (figurative), profound, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, featuring, diverse array, breathtaking, must-visit, stunning`. The text reads like an advertisement.

**§17 Borrowed authority** — *sentences.* `experts argue`, `observers have cited`, `industry reports`, `some critics`, `several publications`, a list of outlets, `over N followers`. A name or an unnamed authority stands in for what was said. Use the real source or cut the claim. A missing citation alone is not a tell.

**§18 Avoiding is, are, and has** — *sentences.* `serves as`, `stands as`, `functions as`, `operates as`, `marks`, `represents [a]`, `boasts`, `features`, `offers`, `maintains [a]`, `refers to`. Use the short verb.
> Before: Gallery 825 serves as LAAA's exhibition space and boasts over 3,000 square feet.
> After: Gallery 825 is LAAA's exhibition space and has 3,000 square feet.

## D. Formatting by rule

**§19 Bold as decoration** — *counts, blocks.* Read `bold label openings` in the header first: it gives the number of blocks opening `**Label:**` out of the total. A majority means the document is a frame, not a list, and §27 applies too. Words bolded without a reason are the sentence-level case.
> Before: - **User Experience:** The experience has been improved. - **Performance:** Performance has been enhanced.
> After: The update improves the interface, speeds up load times and adds end-to-end encryption.

**§20 Decorative headings** — *blocks.* Headings capitalising every main word; emojis or arrows as decoration; a horizontal rule between every block; a heading restating its own first block. Use sentence case and let the title stand once. Headings are not units in the report, so read them from the file.

**§21 Curly quotation marks** — *counts.* The `curly quotes` count is the whole check. A document that uses them everywhere and a document that uses them nowhere are each consistent; a document with one curly pair among straight ones is not. Most editors auto-curl, so this is a consistency check rather than a tell on its own.

## E. Leftovers from the chat and the draft

Remove outright; nothing here needs rewriting.

**§22 Chatbot residue** — *sentences.* `I hope this helps`, `Of course!`, `Certainly!`, `Great question!`, `You're absolutely right`, `Would you like…`, `Want me to…?`, `Should I continue?`, `let me know`, `here is a…`. The most certain tell in this list and the easiest to miss when it wraps real content.

**§23 Knowledge-limit disclaimers and guesses** — *sentences.* `as of [date]`, `up to my last training update`, `while specific details are limited`, `based on available information`, `not publicly available`, `in the provided sources`, `it is believed that`, `likely [grew up, studied]`. The text mentions where knowledge ends, or admits it found no source and fills the gap. State what the source does not show, or cut the sentence.

**§24 A heading repeated in the first block** — *blocks.* A heading followed by a one-line block restating it before the real content begins. The report's block list shows the heading and the block that follows it, so read them as a pair.

**§25 Writing about the document instead of its subject** — *blocks.* `was added to replace`; `generated from`; `compiled from`; `anything unconfirmed is flagged rather than guessed`; `the table below compares`; `this section is organized by owner`; a legend of an order the reader can already see. Keep a source credit the reader can follow and a caveat that changes what the reader should do. State a convention once, and only when the reader cannot infer it.

## F. Writing for the wrong reader

**§26 Re-explaining what the reader knows** — *sentences, blocks.* A reply that restates the problem, walks through the diagnosis and lays out the evidence before reaching the decision; background the reader already supplied; the answer in the last block. Each sentence reads fine alone, so this survives sentence-level cleanup. Lead with the decision.

## G. Document scale

The items above are sentence and block scale. These apply to the whole file, and they are the ones that catch a document built on a template. Count before you judge: a pattern in three blocks of eighty is a document-scale tell, a pattern in one is a sentence.

**§27 One frame repeated across blocks** — *blocks, whole document.* The same opening, the same field labels, or the same closing clause in a run of blocks. Test: read only the first three words of each block in the `## Blocks` section. If they form a pattern, the document is a template. `bold label openings` in the header gives the count that starts the test.
> Before: **Target:** … **Existing owners:** … **Section:** … **Evidence state:** … **What remains:** … (repeated for every entry)
> After: Vary what each entry leads with, or drop the labels where the section heading already carries them.

**§28 A stamp that carries no information** — *3-grams.* A clause repeated verbatim across blocks that is true of all of them and informative of none. "absent from the author's list of eight" on every entry of a list the reader can see. The 3-gram section lists it with every line it appears on; delete the stamp and it survives on none of them individually.

**§29 Identical list-item shape** — *counts.* Every item the same length, or the same count of clauses. The report gives a word count per block: sort them and look at the spread. Items within a word or two of each other are one shape, not a list.

**§30 A contradiction between two blocks** — *whole document.* A number or a range stated differently in two places. This is a defect whatever the voice, so check every number twice: once where it is used, once against the block that defines it. `## 3-grams` catches a figure restated identically; it cannot catch one restated differently, which is why this check needs a whole read.

**§31 The same rule stated three times** — *3-grams.* Stated in the overview, restated in the block that owns it, and restated again in a list of files. Pass every related file in one invocation; the 3-gram list is computed across all of them, and it is the only way to see this.

## When not to act

Keep the details that carry the writer's voice unless they hurt the meaning:

- a specific, unusual detail: a real address, an odd quote, a named person with a role
- mixed feelings and unresolved tension: "I think this is mostly good, but it bothers me"
- dated, era-bound references: slang, memes, in-jokes that map to a year
- a first-person choice the writer can explain
- a genuine aside, parenthetical or self-correction

Text written before November 2022 is not AI-written, and a document that predates the model it describes may use its patterns on purpose.

## Source

§1–§26 are adapted from [blader/humanizer](https://github.com/blader/humanizer) (MIT), which derives them from Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) maintained by WikiProject AI Cleanup. §27–§31 were added for this project after a blind evaluation panel found that sentence-level checks do not catch a document built on a template.
