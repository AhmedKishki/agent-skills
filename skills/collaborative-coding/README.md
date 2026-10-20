# Collaborative Coding

An anti-vibe-coding skill: the user directs the work, and the agent proposes,
explains, and applies one agreed code patch at a time.

## Use

Load `collaborative-coding` in your agent and describe the goal. For example:

> Use collaborative-coding to add input validation. Explain at Standard level.

Agree on the task plan, then review each proposed patch and its check before the
agent acts. Approve it, ask a question, or suggest a change. The agent reports the
result and waits for acceptance before moving on.

Choose one explanation level and change it whenever needed:

- **Beginner:** learner or student; algorithm, language primitives, and step-by-step code.
- **Standard:** junior developer; algorithm and code summary.
- **Expert:** senior or academic; algorithm only.

Suggested code is self-documenting: variable, function, and class names reveal
their purpose. Short names and familiar abbreviations are preferred, but clarity
comes first.

The shared plan lives at `<workspace-root>/collab-coding/TASKS.md`. Both parties
can edit it. It holds remaining work in execution order, not a growing history.
Completed items disappear after agreed checks and user acceptance.

The agent's entry point is [SKILL.md](SKILL.md). Install the complete directory
so its linked references remain available. The skill provides instructions;
approval enforcement depends on the host agent following them.
