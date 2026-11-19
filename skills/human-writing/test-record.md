# Test record

## Round 1 (before rules 3 and 4)

Each prompt ran with and without the skill.

- **A.** "Write a short section for our firmware team wiki explaining why we debounce the bike light's mode button in software on the GD32 rather than reading the GPIO directly. Three or four paragraphs, for a new junior engineer."
- **B.** "Write about 300 words for a study-group handout explaining why Sayer distinguishes intensive from extensive research designs in Method in Social Science, and what each can and cannot tell you."
- **C.** "Rewrite this using human-writing:" followed by the BLE text at the end of this file.

Results:

- C separated the two configurations. Without the skill, the agent kept the vague "not a cut-down version" negation, added advice the source does not contain and gave no justification. With the skill, it cut the six padding sentences and kept the firmware negation with its shared symptom stated.
- A and B passed the automatic checks (stock phrases, announcement phrases, length) in both configurations, so their differences are qualitative.
- The skill cost about six times the wall time (235 s against 38 s on average) and about one and a half times the tokens.
- Your review found weakly related sentences combined, which led to rules 3 and 4.

## Round 2

Rules 3 and 4 were applied without a test run.

## Round 3 (rules 8 to 13)

The test text was 38 lines of documentation for a TIMER2 time driver. You had objected to two faults in it: "a divider that does not come out whole" (come out from where?) and a usage example that uses `dp` without the line that creates it. One agent ran the check mode with version 1.0.0 and one with 1.1.0.

- 1.0.0 flagged neither fault, and none of the passives "are frozen", "is refused" and "is needed". It flagged "the time lasts" and "reload" as a second name for CAR.
- 1.1.0 flagged both faults and the passives. It also flagged faults that no example in the skill names: "runs on the STM32 general-purpose timers", "the time would jump", "the first 65,536 counts run undivided", "Ported from" without an actor, "this write" pointing at code the text does not show, and the bit names UPS, UPG and UPIF, which the text never defines.
- The new examples in `SKILL.md` quote the two faults you raised, so finding those shows only that the agent applies the examples. The other findings show that the rules reach new cases.
- 1.1.0 took 108,000 tokens and 511 s, against 89,000 tokens and 384 s for 1.0.0.

## Observed, not yet acted on

- Running on every output multiplies the cost measured in round 1.
- The A run kept strictly to "why" and dropped practical material the baseline gave: sampling on a timer tick, the RC alternative and the rule for the wake-up interrupt. A narrow reading of a part's purpose can cut useful content.
- The B run ended on a one-sentence paragraph that states the conclusion.
- In round 3, rule 9 led the agent to rewrite imperative code comments, such as "Clock on, then reset", into sentences with `init` as the subject. An imperative is already active, so rule 9 does not require this.

## BLE test text

```
In today's fast-paced world of connected devices, Bluetooth Low Energy has become a pivotal technology. BLE is a wireless protocol. It is not just a smaller version of classic Bluetooth, it is a fundamentally different approach to communication. A BLE peripheral advertises its presence and waits for a central to connect, and once connected the two exchange data in short connection events separated by a connection interval. The connection interval determines both latency and power consumption: a longer interval saves battery but delays every write. This is important. Many developers assume that a slow response comes from the firmware, but it often comes from the connection interval, since both show up as a delay between a write and its effect. Understanding the connection interval is key to building great BLE products. In conclusion, BLE offers developers a powerful, flexible and efficient way to connect devices.
```
