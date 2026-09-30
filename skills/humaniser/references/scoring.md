# Scoring

The checklist decides. The script supplies context and counts, and nothing else. Two numbers come out of a run, and they mean different things.

## What the script prints

```
python3 scripts/evaluate.py FILE [FILE ...] [--level all|sentence|phrase|paragraph]
                                [--lines 40-60,120-140] [--out REPORT.md] [--max-chars N]
```

- **Blocks, sentences, words**, and the count of sentences per block.
- **Sentence words**: min, median, max, mean, standard deviation, and the coefficient of variation.
- **Surface counts per 1000 words**: semicolons, em-dashes, parentheses, questions.
- **Repeated 3-grams** across every file passed in one invocation, with line numbers.
- **Every unit with its context**: a phrase with its neighbouring phrases, its sentence and the surrounding sentences and blocks; a sentence with the phrases beside it and its block; a block with the blocks before and after it.

The script segments and counts. It classifies nothing, scores nothing, and holds no thresholds. It skips front matter, fenced code, tables and footnote entries, because a reference is not prose and a citation is not a sentence.

Pass several files in one run to find a rule restated across them. That is the only way §31 becomes visible.

## The two numbers

**Pattern score.** For each checklist item, decide whether the document exhibits it, and in how many blocks. Report the fraction of the 31 items the document passes, and list the failures by item number with a quoted example each. A document that passes 20 of 31 is not "65% human" — it has six tells, and the number only tells you where to look.

**Counts.** The measured numbers are facts about the text, not verdicts on it. Report them, and say what they show. Three findings from measuring this repository, which changed how the checklist is written:

- Sentence-length variation does not separate registers. Prose in `sections/section-1/ai-and-fetishism-draft-section-1.md` measures a coefficient of variation of 0.52 against 0.49 for `AGENTS.md`. The drafts read as *less* varied because they carry long quoted sources and parenthetical citations inside short sentences. The measurement is worth taking and is worth nothing as a threshold.
- Semicolon density does separate them: 10.7 to 14.2 per 1000 words in agent-facing files against 0.0 to 4.7 in section drafts. It is a symptom of the semicolon-joined imperative, which is §11 and §19 at register scale.
- The repeated 3-gram list finds more than any judgement call. A verbatim clause across six entries is §28, and no amount of reading catches it as reliably as the list.

## Judging a document you did not write

The pattern score is reliable enough to compare two documents and not reliable enough to certify one. Two evaluators given the same document and this checklist disagreed by up to 20 points on a two-block file and agreed within 10 on a long one. Long files agree because there is more evidence; short files are close to a coin toss.

So: report the item-by-item verdicts with quotes, and report the score as a summary of those verdicts rather than as a measurement of the writer. Where two evaluators would differ, say which item is the judgement call and why you ruled the way you did.

## Approving a change

Present a table — location, before, after, item number — and apply only what is approved. A diagnosis, a score, or silence is not approval. Never change a claim, an instruction, a path, an identifier, a scope or a date without asking; a deletion that cannot change meaning may be applied when the user asks for the pass to be applied as a whole.

A document that changed materially returns to Part 1, because an edit introduces new sentences with the same faults. Verify by rerunning the script and confirming the 3-gram list is shorter, not merely that the prose reads better.
