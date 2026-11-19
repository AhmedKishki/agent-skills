# human-writing: maintainer notes

These notes record the reason behind each part of the skill, so that a later change can be checked against the reason for the rule it touches. Install it in Claude Code 2.1.275 or later with `/plugin install human-writing --marketplace AhmedKishki/agent-skills`; for other agents, see the [collection README](../../README.md#install).

## Purpose

The skill serves the generation phase of every output. It makes the agent justify each sentence before delivery and cut or repair any sentence that makes no logical connection. Checking and rewriting supplied text use the same method on sentences the agent did not write. Because the skill runs on every output, its own text has to stay short and plain, and it has to pass its own rules.

## Files

| File | Holds |
|---|---|
| `SKILL.md` | the definitions, the thirteen rules with examples, the justification format and the generation steps |
| `references/justification.md` | a weak part, its justification and its revision, worked through |
| `references/detect-and-rewrite.md` | the check and rewrite modes for supplied text |
| `references/semantic-tests.md` | from the humaniser: noun-verb fit, complete claims, referents, comparisons, logical links, lists |
| `references/argument-order.md` | from the humaniser: where claims, evidence and conclusions go, and how a part opens |
| `references/formulaic-phrases.md` | from the humaniser: the stock-phrase checklist |
| `test-record.md` | the test rounds, their prompts and the BLE test text |
| `changelog.md` | the changes in each version |

`SKILL.md` holds everything that generation needs, so an ordinary reply runs without loading a module.

## Core idea

A sentence is artificial when it makes no logical connection. The agent judges a sentence in its place: what it does for the purpose of its part (a section, subsection, paragraph, list or table), and how it relates to the sentence before it and the sentence after it. A sentence that does nothing for its part's argument is cut.

## Decisions

### The justification is internal by default

The agent writes the justification, revises from it and delivers only the prose. The user sees the justification on request, and always in the check and rewrite modes, where it is the evidence for every cut.

### Rule 2: a plain assertion stays when its context gives it work

"X is Y" and "X is not Y" connect nothing by themselves. Two stricter options were considered: an explicit connector inside every such sentence, or moving every bare assertion into a list or table. Under the chosen rule, a definition or premise earns its place through the sentence that reasons from it.

### Rules 3 and 4: addition is not a connection

These rules came out of the first test round. The justification checked each sentence as a whole, so two claims joined by "and" shared one entry and the link between them was never tested. The agent also accepted "also" as a link to the previous sentence. Rule 3 covers both cases. Rule 4 states when two claims may share a sentence, and the `joins` line records the relation that allows it.

A sentence from round 1 that the rules now split: "Extensive findings also seldom hold for other populations, and reading individual behaviour off aggregate figures commits the ecological fallacy."

### Rule 5: a negation needs a confusable feature

"Not X but Y" stays only when X has something a reader could mistake for Y. Without that feature the negation rejects a position nobody holds. The `confusable` line makes the agent name the feature, so the check shows in the justification.

### Rule 6: connectors match the content

A connector that claims a relation the content lacks hides a gap in the argument. Filling the gap with an invented fact would replace a weak link with a false one, so the rule sends an unsupported relation to a move or a cut.

### Rule 7: lists and tables

The skill discourages superficial information in the prose and leaves lists and tables free. A fact the reader needs that argues nothing can therefore sit in a list or table, where each item answers the purpose of its list. This reading came from me and you accepted it.

### Rules 8 to 13: words and order

You set these rules after reviewing the documentation of a timer driver. There, "a divider that does not come out whole" left you asking "come out from where?", and a usage example used `dp` without the line that creates it. Rule 8 replaces the verb, not the noun, because the noun names what the sentence is about. Rule 9 makes the active voice a rule without exceptions, as you asked. Rule 12 forbids invented examples, so an agent without a real example asks the user for one. Rule 13 groups by kind before time and place, following your CV example. The tests for rules 8 to 12 sit in `references/semantic-tests.md` and the ordering details in `references/argument-order.md`.

### What came from the humaniser

The semantic tests, the argument-order rules and the formulaic-phrase checklist became modules. Two parts stayed behind:

- the two-stage workflow, since a request to rewrite produces the rewrite in the same turn and checking without rewriting is its own mode
- the ban on semicolons and em dashes, although the skill's own text avoids both, following house style

### Modes for supplied text

- Check returns the justification of the input, with a fix on every repair, split or cut verdict, and no rewrite.
- Rewrite returns the rewritten prose, its justification and the removed sentences with the rule each failed.
- When the request does not say which mode, the agent asks.

### Trigger

The description tells the agent to use the skill for any prose, even when the user does not name it. A skill triggers only through its description, so a narrow description would leave most generation unchecked.

## Test record

The test rounds, their prompts and results are in `test-record.md`.
