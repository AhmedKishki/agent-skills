# Operations

- Each piece of a sentence is one COPY plus the operations applied to it, in order.
- The script checks the wording rule of every operation. The meaning rule is the agent's check.

| Operation | Wording rule (script) | Meaning rule (agent) |
|---|---|---|
| COPY | An exact, whole-word span of one source | The source asserts the span, read in its context |
| DELETE | Remove an exact span from the piece | The DELETE test below |
| ORDER | Sentences follow the chain order of steps | Within a step, keep source order unless a source states another |
| INFLECT | Agreement or antecedent only, from the closed lists | The change only restores grammar after another operation |
| NORMALISE | One rule from the closed list | The change alters no claim |

- Translation, paraphrase, synonyms, tense changes and added words are not operations.

## DELETE test

DELETE passes when the source, read in its context, asserts the shortened span. Keep these unchanged:

- the subject and the predicate
- negation, modality and hedges, such as *not*, *may*, *likely* and *suggests*
- quantifiers and degree, such as *some*, *most*, *slightly* and *sharply*
- conditions on the kept claim, such as *if*, *unless* and *only when* clauses
- attribution frames, such as *Smith argues that*, *critics claim* and *according to*
- the scope of time, place and population

- A whole clause may go when the remaining clause is asserted on its own, for example a concessive *though* clause. Record a removed qualification under Left out.
- A deletion must not create a relation. Removing *separately* or *also* can make two claims read as one.

## INFLECT

- `agreement` changes only these forms: *is/are*, *was/were*, *has/have*, *does/do*, *this/these*, *that/those*, *a/an*, and a word with or without *-s*, *-es* or *-y/-ies*. Use it only where another operation broke agreement.
- `antecedent` replaces a listed pronoun with its antecedent, copied exactly from the same source. It may add *'s* or *'* to a possessive and nothing else. The antecedent must be unambiguous in the supplied text.
- Tense never changes. If the output context needs another tense, keep the source's tense and say so in Reasoning.

## NORMALISE

| Rule | Change |
|---|---|
| `case` | Upper- or lower-case the first letter of a piece where it starts, or stops starting, a sentence. Never a proper noun |
| `quotes` | Change quotation-mark and apostrophe glyphs only |
| `end-stop` | End a sentence with a full stop, only when its source sentence ends with one |
| `semicolon` | Replace a semicolon between two full clauses with a full stop and a capital |
| `pair` | Apply a whole-word pair the user supplied for this task, such as `labor` → `labour` |

- A sentence starts with a capital letter, and the script refuses one that does not. After a DELETE at its start, NORMALISE `case` to upper.
- Whitespace is collapsed automatically.
- No other punctuation changes. A comma, a dash or a question mark can change a claim.

## Joins

- One output sentence normally comes from one source sentence.
- Pieces from different source sentences may be joined only by a connective copied from the licence of a stated link. See [Argument](argument.md).
- Mark the connective with the step whose link it realises. The script refuses a join without one, or a connective that lies outside its licence.
- DELETE the first piece's full stop and lower-case the next piece with NORMALISE `case`.
- The joined sentence claims the relation only of what the licence relates. Detail that other sources add to either side must not change what the relation is claimed of.
- The marker lists every source the sentence uses, for example `[S1; S2]`.
