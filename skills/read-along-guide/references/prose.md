# Read-along prose

The guide's prose is plain, direct and natural, for a reader who is not an expert. Every sentence gives the reader information about the author's argument. Apply these rules while drafting and again in a writing pass before every delivery.

## 1. House style (hard rules)

- British English (except inside quotes).
- No semicolons. No em or en dashes in the guide's own prose (allowed inside quotes). Use full stops.
- No "not X but Y", "not only X but", "rather than", "instead of" or similar contrastive frames.
- No signposting or meta-commentary: "this section", "below", "as we will see", "in short", "note that", "it is worth", "let us".
- No pseudo-clefts ("What X does is Y", "What remains is").
- No sentence opens with a bare "This" or "It" as subject ("This argument shows" is fine, "This shows" is not).
- No questions in the guide's own voice (headings included).
- Banned words in non-literal use: posit, proliferate, foreground, problematise, register, important, operate, does work, move, foreclose, run, frontier, agent, actor, crucial, key. Write "people" or "the person acting" for agents, except inside quotes and the author's fixed terms.
- Attributions such as "Bhaskar argues" (the author argues) are allowed.
- Terms are marked with italics or bold, never with quotation marks. Curly single quotes ‘ ’ are reserved for verbatim text by the author or by authors he quotes.
- Paragraphs of two to four sentences. Short, simple sentences, each with one job.

## 2. The deletion test

A sentence earns its place only if removing it would lose a claim, a reason, an example, a qualification, a consequence or a connection the argument needs. If the argument works as well without it, cut it, or fold its one useful fragment into a neighbouring sentence.

Typical failures: announcements of what follows, bare labels before lists, restatements of a conclusion just reached, ceremonial openers and closers, verdict-like one-liners, sentences that call a point significant without saying why, and summary sentences whose content is already in the sentences around them.

Never cut: attributions a quote needs, definitions, examples, qualifications, cross-references attached to a claim, steps of a numbered argument, or anything that carries a distinct claim.

## 3. Say it directly

Tell the reader the information itself, never a description of the text. The rule applies to sentences **and** to phrases inside sentences.

| Instead of | Write |
|---|---|
| "Two statements tell the reader how to treat the book. Bhaskar has ..." | "Bhaskar has ‘little or no quarrel’ with the book in its second-edition form, and ..." |
| "Sociological theory is usually split into two camps." | "Sociological theory is usually divided between a Weberian and a Durkheimian camp." |
| "a ‘new critical naturalism’ with two main parts" | "a ‘new critical naturalism’, which entails a transformational model of social activity and a causal theory of mind" |
| "Bhaskar names four ways a theory can be modified:" | "Hermeneutic writers reproduce positivist theories modified by inversion, displacement, transformation or condensation:" |
| "To say that B reduces to A can mean three things." | "To say that B ‘reduces’ to A can mean that A provides a basis for B, that A explains B, or that knowledge of A lets us predict B." |
| "Bhaskar therefore turns to (2)." | "Bhaskar forestalls that conventionalism by arguing, against (2), that science has implications for values." |
| "The argument in steps:" / "Bhaskar makes three objections." / "There are differences." | cut; the numbered list or bold-labelled points follow directly |
| "Section 3.6 considers the status of agency." | cut (a bare signpost) |

- Replace counting phrases ("in three ways", "two main parts", "on three grounds") with the names of the items, or drop them when the items follow at once.
- A lead-in to a list must itself carry the claim the list develops, or be removed so that each item is a full sentence.
- A short attribution introducing a verbatim quote may stay ("Bhaskar concludes: ‘...’"). Prefer working it into a sentence that already says something.
- When you name items in place of a count, take the names from the guide or the book. Never invent them.

## 4. Reading naturally

- Merge choppy runs of very short sentences that serve one point. Split overloaded sentences that do several jobs.
- Vary monotonous openings ("Bhaskar ... Bhaskar ... He ...").
- Give every "it", "this" and "they" one clear referent.
- Fix noun-verb mismatches (an abstract noun doing something it cannot do).
- Merge one-sentence paragraphs left by cuts with the paragraph that makes the same point.
- Keep the register: clear, plain, precise. Do not make it casual, and do not add facts, interpretations, examples or connections the text does not support.

## 5. Checks

- `python3 -I scripts/check_style.py <file>` flags breaches of the house style. Fix every flag, except literal uses and the author's own terms (e.g. *Agents and patients*, a table title of the author's, "the moves in a game of chess"). Keep a list of the accepted flags.
- `python3 -I scripts/detect_announce.py <files>` lists candidate counting sentences, colon lead-ins and meta descriptions. Judge each one against section 3. Then read the whole file for counting phrases the detector misses.

## 6. The writing pass (correction)

Run the pass on every finished chapter before delivery. The user has opted for direct correction, with no separate diagnostic report. For long files, give one subagent per file a brief that contains sections 1 to 4 of this reference and the following:

- **Unchanged**: text inside ‘ ’ quotes (verbatim), headings, image lines, caption lines (`*Figure ...*`, `*Table ...*`), table rows and bold labels.
- **Survives**: every claim, qualification, example, figure or table reference, chapter or section cross-reference and note reference.
- **Checks**: run `check_style.py`, `detect_announce.py` and the quote check (`check_quotes.py`) after editing.
- **Diff**: compare against a pre-edit copy and confirm that nothing needed was lost.
- **Report back**: the number of sentences cut and rephrased, the checker results, and five before → after examples.

After the pass, confirm that the structural lines are byte-identical (headings, images, captions, tables) by comparing them with the pre-edit copy.
