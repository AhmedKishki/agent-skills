# Scoring

The checklist decides. The script supplies context and counts, and nothing else. Two numbers come out of a run, and they mean different things.

## What the script prints

```
python3 scripts/evaluate.py FILE [FILE ...] [--level all|sentence|phrase|paragraph]
                                [--lines 40-60,120-140] [--out REPORT.md] [--max-chars N]
```

The report has four sections, in this order, and the checklist's pass index walks them in this order.

**Header.** Blocks, sentences, words, sentences per block. Then sentence words: min, median, max, mean, standard deviation, coefficient of variation. Then surface counts per 1000 words: semicolons, em-dashes, parentheses, questions. Then `bold label openings`, the number of blocks that open `**Label:**`, and `curly quotes`.

**`## 3-grams occurring in more than one block`** — every three-word span that appears in more than one block across all files in the run, with line numbers.

**`## Blocks`** — each block with the blocks before and after it.

**`## Sentences`** — each sentence with the phrases beside it, the sentences around it, and its block. Units are numbered `S000.0`, `S000.1` and carry `file:line sentence n`, so a finding can cite the report directly.

**`## Phrases`** — each phrase with its neighbouring phrases, its sentence, the surrounding sentences, and its block. Emitted only at `--level phrase` or `--level all`; narrow it with `--lines` because it is the widest pass.

The script segments and counts. It classifies nothing, scores nothing, and holds no thresholds. Footnote entries are listed as blocks so a finding can cite one, but they are excluded from every statistic: a citation is not prose. Headings are not units, so B11 and B12 need the file itself.

Pass several files in one run: the 3-gram list is computed across all of them, and that is the only way §31 becomes visible.

## The numbers

**Part A count.** For each of the seven semantic families, decide whether the document exhibits it, and in how many sentences. Report the families that fired, not a single percentage: A1 and A6 alone can account for most of what is wrong with a passage, and a number that merges them tells the reader nothing they can act on. Give each finding a quotation, a line number, and the test it failed.

**Part B count.** The same, over the surface items. Report it separately and label it as a tie-breaker.

**Part C list.** The mechanical and provenance faults. Never fold these into a voice figure. A document can have no voice tells and four content defects, and a merged number hides exactly that.

**Counts.** The measured numbers are facts about the text, not verdicts on it. Report them and say what they show. Four findings from measuring this repository:

- Sentence-length variation separates nothing. Prose in `sections/section-1/ai-and-fetishism-draft-section-1.md` measures 0.47 against 0.49 for `AGENTS.md`. The drafts read as *less* varied because they carry long quoted sources inside short sentences. Worth taking, worth nothing as a threshold.
- Semicolon density marks a register rather than an author: 10.7 to 14.2 per 1000 words in agent-facing files against 0.0 to 4.7 in section drafts. B7.
- Bold label openings mark a template, not a person: 85 of 146 blocks in the draft-scale todo, 0 in every section draft.
- The repeated 3-gram list finds more than any judgement call, and it also finds the residue an editor leaves: half-merged sentences, a repeated clause whose second copy is weaker, a term whose word order has drifted.

## A note on what a score can be

Two earlier versions of this instrument rated generated passages *cleaner* than the author's own drafts: 4.3 tells per thousand words against 6.1, and before that 90 to 92 per cent quality against 51. Both were form-based rubrics, and form is what a generated passage gets right. The author's own classification of eight passages, blind to which were which, was correct eight times out of eight on the same text the rubric scored backwards.

So the instrument does not certify authorship. It names the sentences that say nothing, and the author decides what that means for the document.


## Judging a document you did not write

The pattern score is reliable enough to compare two documents and not reliable enough to certify one. Two evaluators given the same document and this checklist disagreed by up to 20 points on a two-block file and agreed within 10 on a long one. Long files agree because there is more evidence; short files are close to a coin toss.

So: report the item-by-item verdicts with quotes, and report the score as a summary of those verdicts rather than as a measurement of the writer. Where two evaluators would differ, say which item is the judgement call and why you ruled the way you did.

## Approving a change

Present a table — location, before, after, item number — and apply only what is approved. A diagnosis, a score, or silence is not approval. Never change a claim, an instruction, a path, an identifier, a scope or a date without asking; a deletion that cannot change meaning may be applied when the user asks for the pass to be applied as a whole.

A document that changed materially returns to Part 1, because an edit introduces new sentences with the same faults. Verify by rerunning the script and confirming the 3-gram list is shorter, not merely that the prose reads better.
