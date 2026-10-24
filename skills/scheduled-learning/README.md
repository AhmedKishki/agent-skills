# Scheduled Learning

Use this skill to study a book, paper or set of texts across successive runs. A Markdown progress file records completed coverage and the next part to explain.

## Typical usage

> Use scheduled-learning to plan a section-by-section study of this paper. Show me the plan for approval before starting any explanations.

After setup, a prompt such as this continues the track:

> Use the scheduled-learning skill with the progress file at progress-my-paper.md.

## What to expect

- A concrete plan approved before runs begin; setup alone does not start run 1.
- Source-grounded explanations of arguments and concepts, with short verified quotes.
- At most 2,000 words per explanation; dense units can be split into further runs.
- Saved coverage, stopping points and plan changes in the agreed progress file.

Runs can be triggered manually. An external scheduler is separate from the progress file and must be set up separately for unattended runs. Unattended runs stop if required inputs are missing or ambiguous.

See [SKILL.md](SKILL.md) for the full workflow.
