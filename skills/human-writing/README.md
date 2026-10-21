# human-writing: maintainer notes

These notes record the reason behind each part of the skill, so that a later change can be checked against the reason for the rule it touches.

## Purpose

The skill serves the generation phase of every output. It makes the agent justify each sentence before delivery and cut or repair any sentence that makes no logical connection. Checking and rewriting supplied text use the same method on sentences the agent did not write. Because the skill runs on every output, its own text has to stay short and plain, and it has to pass its own rules.

## Files

| File | Holds |
|---|---|
| `SKILL.md` | the definitions, the seven rules with examples, the justification format and the generation steps |
| `references/justification.md` | a weak part, its justification and its revision, worked through |
| `references/detect-and-rewrite.md` | the check and rewrite modes for supplied text |
| `references/semantic-tests.md` | from the humaniser: noun-verb fit, complete claims, referents, comparisons, logical links, lists |
| `references/argument-order.md` | from the humaniser: where claims, evidence and conclusions go, and how a part opens |
| `references/formulaic-phrases.md` | from the humaniser: the stock-phrase checklist |

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

### Round 1 (before rules 3 and 4)

Each prompt ran with and without the skill.

- **A.** "Write a short section for our firmware team wiki explaining why we debounce the bike light's mode button in software on the GD32 rather than reading the GPIO directly. Three or four paragraphs, for a new junior engineer."
- **B.** "Write about 300 words for a study-group handout explaining why Sayer distinguishes intensive from extensive research designs in Method in Social Science, and what each can and cannot tell you."
- **C.** "Rewrite this using human-writing:" followed by the BLE text at the end of these notes.

Results:

- C separated the two configurations. Without the skill, the agent kept the vague "not a cut-down version" negation, added advice the source does not contain and gave no justification. With the skill, it cut the six padding sentences and kept the firmware negation with its shared symptom stated.
- A and B passed the automatic checks (stock phrases, announcement phrases, length) in both configurations, so their differences are qualitative.
- The skill cost about six times the wall time (235 s against 38 s on average) and about one and a half times the tokens.
- Your review found weakly related sentences combined, which led to rules 3 and 4.

### Round 2

Rules 3 and 4 were applied without a test run.

### Observed, not yet acted on

- Running on every output multiplies the cost measured in round 1.
- The A run kept strictly to "why" and dropped practical material the baseline gave: sampling on a timer tick, the RC alternative and the rule for the wake-up interrupt. A narrow reading of a part's purpose can cut useful content.
- The B run ended on a one-sentence paragraph that states the conclusion.

## BLE test text

```
In today's fast-paced world of connected devices, Bluetooth Low Energy has become a pivotal technology. BLE is a wireless protocol. It is not just a smaller version of classic Bluetooth, it is a fundamentally different approach to communication. A BLE peripheral advertises its presence and waits for a central to connect, and once connected the two exchange data in short connection events separated by a connection interval. The connection interval determines both latency and power consumption: a longer interval saves battery but delays every write. This is important. Many developers assume that a slow response comes from the firmware, but it often comes from the connection interval, since both show up as a delay between a write and its effect. Understanding the connection interval is key to building great BLE products. In conclusion, BLE offers developers a powerful, flexible and efficient way to connect devices.
```
