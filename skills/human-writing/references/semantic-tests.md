# Semantic tests

Use these when a line of a justification is thin. Each test finds a sentence whose claimed work is missing.

## Noun-verb fit

Read the subject and verb as a pair. Ask whether the subject can perform the action, and whether the verb states the relation or only makes it sound active. If the subject cannot perform the action, replace the verb with the action that happens. A metaphor fails even when its meaning is clear, so write the literal action. A verb of movement or change, such as "come out", "reach" or "lead to", fails when the reader has to ask from where or to where. Keep a nominalisation when it names a technical concept.

> Weak: The framework carries three assumptions.
>
> Better: The framework makes three assumptions.

## Complete claims

Ask what the sentence lets the reader know. A sentence that announces importance, tension, complexity or change without naming it has no work to do. The reader must be able to identify the actor, action, object or mechanism.

> Weak: This reveals a deeper tension in the debate.
>
> Better: The debate treats local autonomy as both the aim of organisation and an obstacle to coordinated action.

Give each abstract rule an example from the subject: the sources, the code, the user's data or a calculation you show. Never invent one. If you have none, ask the user for one.

> Weak: Starts TIMER2 counting at the tick rate, with an interrupt at each half of its range.
>
> Better: Starts TIMER2 counting at the tick rate, with interrupts at counts 0 and 32,768.

## Active voice

Find every passive verb, such as "is refused" or "are frozen". Name the actor and make it the subject. If you cannot name the actor, find out who or what acts before you write the sentence.

> Weak: Call it after the clocks are frozen.
>
> Better: Call it after `freeze` sets the clocks.

## Simplest words

For each noun and verb, ask whether a shorter or more common word says the same. Keep a technical term when it is the exact name of the thing. The inflated verbs in `formulaic-phrases.md`, such as "serves as" for "is", fail this test.

## Removable words

Delete each phrase in turn and reread the sentence. If it means the same, leave the phrase out. A trailing phrase that comments on the claim, such as "with nothing to show for it", often fails.

## Referents

Give every this, that, it, they, these, such, former and latter one clear antecedent. Replace the pointer when two nouns could fit, or when it points at a whole paragraph. A vague "this" often hides the relation that the back line should name. Names, symbols, abbreviations, code identifiers and cross-references such as "see above" need a target too: something the text defines, shows or links. A code example shows where each name in it comes from, so a reader of `dp.rcu.constrain()` sees the line that creates `dp`.

## Comparisons

A comparison names what it compares, the shared dimension, the baseline and the conclusion it supports. Flag unmatched categories, missing baselines and "from X to Y" ranges whose ends do not form a range.

## Logical links

Check every stated and implied connection. Each of these claims a relation the content does not have:

- chronology presented as cause
- a contrast between statements that do not conflict
- an example treated as proof
- a conclusion whose premise the reader must supply
- a shared theme presented as an explanation
- two claims joined by "and", a comma or a colon with their relation unstated
- a phrase tacked onto a sentence that adds a second claim, such as "usually through interviews" after a definition
- a jump between levels of analysis with no reason given

State the missing relation when the content supports it. Otherwise move or cut the sentence.

## Coordination and lists

Items joined by "and", "or" or a colon share a grammatical and a conceptual role. A list answers the category that introduces it. Flag forced threes, mixed levels of abstraction and a last item that is really a consequence of the others.
