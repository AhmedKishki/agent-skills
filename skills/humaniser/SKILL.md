---
name: humaniser
description: >-
  Cut bloat and slop out of markdown documentation. Use for AGENTS.md, plans,
  todos, arcs, progress files, supplements, skill files, READMEs and any other
  human-facing or agent-facing prose that is padded, repetitive, hedged,
  signposted, inflated or abstract where it should be concrete. Two parts:
  evaluate with the script, then propose replacements. Not for approved wording,
  quotations or source excerpts.
---

# Humaniser

Documentation is read by people, so every sentence has to carry weight. This skill finds the sentences that do not, then proposes replacements. It judges nothing by itself: the script reports what is in the text, and you apply the standards below.

## Scope

In: `AGENTS.md`, plans, todos, arcs, progress files, supplements, skill files, READMEs, and any prose an agent or a person reads.

Out: approved wording, quotations, source excerpts, and the article's own prose. Those carry provenance and approval rules that rewriting them would break. If a document mixes both, say which passages are in scope before starting.

## Standards

1. **Every word earns its place.** Delete any word whose removal changes no meaning. Test: cut the phrase, read the sentence, and see whether it still says the same thing.
2. **Every sentence carries a claim and its support.** A claim on its own goes, or gains the figure, path, example or named source that backs it. The report's `no-support?` flag marks where to look first.
3. **Short sentences only when they carry a thesis.** Chopping a sentence in half for rhythm reads as machine prose. Test: join it to its neighbour and see whether the point survives.
4. **Show the concrete case.** A critique without a named file, paragraph or example is an assertion. Test: can the reader check the claim without taking your word for it?
5. **No contrast nobody asked for.** "Not just X but Y" is for displacing a view the reader actually holds. If X never appears in the document, cut it.
6. **No repetition at any level** — word, phrase, sentence, paragraph, file. The report's 3-gram list covers the files you passed together, which is how you find a rule stated in three places.
7. **No promotional or inflated wording.** Words like crucial, robust, landscape and leverage raise the volume without adding content. The report lists the hits.
8. **No hedging and no signposting.** Delete "it is important to note", "in this section", "we will now". A sentence that announces what it is about to do says nothing.
9. **No unnecessary modifiers.** Cut the adverb that restates the verb and the adjective that restates the noun.
10. **Regular structure reads as machine prose.** Do not imitate a human. Vary structure where the meaning varies and leave it alone where it does not.

Report the writing problems as writing problems. Never claim or imply who wrote a passage.

## Part 1 — Evaluate

The script segments markdown into paragraphs, sentences and phrases, then prints each unit with its neighbours:

- a phrase with the phrases, sentences and paragraphs around it
- a sentence with its phrases and its paragraph
- a paragraph with the paragraphs beside it

It also prints facts about the text: word counts, repeated 3-grams, hedge and contrast hits, and whether a sentence contains a figure, path, footnote or named source.

```bash
python3 scripts/evaluate.py FILE [FILE ...] --out /tmp/evaluate.md
python3 scripts/evaluate.py FILE --level sentence --lines 40-90 --out /tmp/evaluate.md
python3 scripts/evaluate.py AGENTS.md plan.md --out /tmp/evaluate.md   # cross-file repetition
```

| Flag | Effect |
|---|---|
| `--level all\|sentence\|phrase\|paragraph` | Which passes to emit. `phrase` is the widest; narrow it with `--lines`. |
| `--lines 40-60,120-140` | Only blocks starting in these line ranges. Use it to run the phrase pass on the paragraphs the sentence pass flagged. |
| `--max-chars N` | Truncate every unit and context field. Useful on long files. |
| `--out PATH` | Report path. Default is stdout. Keep reports outside the repository. |

Work in this order:

1. Run the sentence pass over the whole file, or over several files when checking for a rule repeated across them.
2. Read the report and judge each unit against the standards, in the context the report gives. The facts are cues, and each one has a known way of being wrong:

   - `no-verb?` misses imperatives and table cells
   - `no-support?` fires on a sentence whose support is the sentence before it
   - a document that names a banned word in order to ban it matches on that word

3. Name the rule each finding breaks and what would change. Quote the unit.
4. Order findings by consequence. A rule stated in three files outranks a sentence of forty words.
5. Run the phrase pass only where the sentence pass found something, using `--lines`.

The lexicon for hedges, contrasts and verb cues lives at the top of `scripts/evaluate.py`. Edit it there; do not copy it into a report or a document.

## Part 2 — Humanise

Produce a table before touching the file:

| Location | Before | After | Rule | Approval needed |
|---|---|---|---|---|

Then:

- Apply only the changes the user approved. A diagnosis, a report or silence is not approval.
- Never change a claim, an instruction, a path, an identifier, a scope or a date without asking. A deletion that cannot change meaning may be applied when the user asks for the pass to be applied as a whole.
- Keep the change log outside the document: location, before, after, reason.
- A document that changed materially returns to Part 1, because an edit introduces new sentences with the same faults.
- Verify by rerunning the script on the changed file and confirming the findings are gone, not merely reduced.
