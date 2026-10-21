---
name: human-writing
description: Write prose in which every sentence earns its place through a logical connection to its part and to the sentences around it. Use this whenever you generate prose of any kind (answers, explanations, documentation, reports, articles, emails, summaries), even when the user does not name the skill. Also use it when the user asks to rewrite a text with human-writing, or to find superfluous argument or wording in a text. Draft, justify each sentence in context, cut or repair the sentences that connect to nothing, then deliver the prose.
---

# Human writing

A sentence is artificial when it makes no logical connection. You find such sentences while you write by justifying every sentence before you deliver it. The output therefore has two parts: the prose, which the reader gets, and the justification, which is your working.

## Parts

Every sentence belongs to a part: a section, subsection, paragraph, list or table. Each part has a purpose, which is the question it answers or the claim it establishes. Judge a sentence by its place. Ask what it does for its part's purpose, and how it relates to the sentence before it and the sentence after it.

## Connections

A connection is the relation a sentence carries to its context. It can give a reason, draw an inference, state a condition or a consequence, give evidence or an example, qualify or concede, contrast, define a term that a later sentence uses, or take the next step in a procedure.

## Rules

1. **Every sentence needs work to do.** If you cannot say what a sentence does for its part, cut it.
2. **A plain assertion is not enough on its own.** "X is Y" and "X is not Y" connect nothing by themselves. Keep one only when its context gives it work, such as a premise the next sentence reasons from.
3. **Addition is not a connection.** "And", "also", "as well" and a phrase tacked onto the end of a sentence look like links, but they only set claims side by side. A sentence whose only link to its neighbour is "also" needs work from its part, like a plain assertion.
4. **Join claims only by a relation.** One sentence may carry two claims only when one gives the reason, condition, consequence, concession or contrast of the other. Name that relation in the `joins` line. If the claims only sit side by side, split them and justify each new sentence on its own. One of them often turns out to have no work and is cut.
5. **Negate only what could be confused.** "Not X but Y" and its variants are allowed only when X has something a reader could mistake for Y. Name that shared feature in the justification. If there is none, drop X and state Y.
6. **Connectors must match the content.** Use "because", "so", "but" or "therefore" only when the sentences contain the relation the word names. If the relation is true but unstated, state it. If it is false, or you cannot tell, move or cut the sentence. Never invent a fact to make a connection.
7. **Lists and tables are welcome.** A fact the reader needs that argues nothing, such as a specification value, can go in a list or table. Each item must answer the purpose of its list or table, and the sentences around them follow rules 1 to 6.

The examples below come from a part that explains why dashboard prices are stale.

Rule 2:

> "Caching is an important part of modern systems." **Cut.** The part asks about these prices, and no sentence uses this one.
>
> "The cache keeps each price for 60 seconds." **Keep.** The next sentence reasons from it: "Prices change every 10 seconds, so a price on the dashboard can be 50 seconds old."

Rule 4:

> "The cache keeps each price for 60 seconds, and the dashboard is built with React." **Split, then cut the second claim.** The framework has nothing to do with the age of a price.
>
> "The cache keeps each price for 60 seconds while prices change every 10 seconds, so a price on the dashboard can be 50 seconds old." **Keep.** "While" sets the two rates against each other and "so" draws the age from them.

Rule 5:

> "This is not a pricing bug. It is a caching issue." **Cut the negation.** Nothing in the part made the pricing service a suspect.
>
> "The wrong prices look like a pricing-service bug, since they arrive through its API, but they come from the cache in front of it." **Keep.** Both causes deliver wrong values through the same API, so a reader could confuse them.

## Justification format

```
Part: <name>: <purpose>
S1 "<first few words>"
  does: <its work for the part>
  back: <how it follows from the previous sentence, or how it opens the part>
  next: <what the next sentence takes from it, or how it closes the part>
  joins: <sentences with two or more claims: the relation between them>
  confusable: <negations only: what X shares with Y>
  verdict: keep | repair: <how> | split | cut
```

## Generating

1. Plan the parts and write each purpose in one line.
2. Draft the prose.
3. Justify every sentence. Do this in your reasoning, or in a scratch file when the output is long. Test every "and" between clauses, every trailing phrase and every "also" against rules 3 and 4.
4. Revise by the verdicts: cut, repair, split, move or merge. Justify each changed sentence again.
5. Deliver the prose without the justification. Show the justification when the user asks for it. If they ask in a later turn, rebuild it from the delivered prose.

A reply of a few sentences goes through the same steps quickly, and every sentence still gets its check.

## Supplied text

To check a text for superfluous argument or wording, or to rewrite one, follow `references/detect-and-rewrite.md`. Both modes show the justification to the user.

## Modules

Read `references/justification.md` before your first justification in a session. Read the others when their question comes up.

- `references/justification.md`: a weak part, its justification and its revision, worked through.
- `references/semantic-tests.md`: tests for a sentence whose work or link is doubtful (noun-verb fit, complete claims, referents, comparisons, logical links, lists).
- `references/argument-order.md`: where claims, evidence and conclusions go, and how a part opens and closes.
- `references/formulaic-phrases.md`: stock phrasing that often marks a sentence with no connection.
- `references/detect-and-rewrite.md`: the check and rewrite modes for supplied text.
