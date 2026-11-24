# Guided Learning

Install it in Claude Code 2.1.275 or later with `/plugin install guided-learning --marketplace AhmedKishki/agent-skills`; for other agents, see the [collection README](../../README.md#install).

Learn a topic, book or subject with an agent that acts as your teacher. It measures your level first, plans a syllabus from there to your goal, and teaches it lesson by lesson until each lesson's ideas hold.

Start with a request such as:

> I want to learn Bayesian statistics well enough to read applied papers. Here is the book I'm using: ~/books/statistical-rethinking.pdf

The agent asks for anything the request leaves open and then poses diagnostic questions: multiple-choice in a clickable dialog, free-thought in the chat. It shows your results and your level per concept, and proposes a syllabus that skips what you already know. Teaching starts once you approve the syllabus, and you can change it at any point.

A lesson teaches a few concepts in depth: it builds your intuition for why each thing works as it does, in direct, concrete language, following one primary source with at most two secondary ones. More breadth comes from more lessons. Every idea opens with the problem it solves, an example stays a few lines long, and a diagram shows a concept wherever one can: memory layouts, state machines, timelines, data flow.

After each lesson you can ask questions. When you have none, the agent sets the lesson's exercise: a realistic task in ordered steps. Each step has you use one of the lesson's concepts and explains the practical side of it, such as the syntax, the tools or the method. You do the work, with hints when you are stuck, and the agent runs and reviews it. A short check of questions on new cases follows. If you miss something, the agent re-explains that idea from a different angle and checks again before it moves on.

Every claim cites your resources or a web source, with a page or section, so you can check it. Ebooks are read through an ebook MCP server such as ebook-hero when one is connected.

Each subject gets a folder:

- `progress.md`: goal, level, syllabus with status, and a log of exercise and check results.
- `lessons/<n>-<slug>.md`: each lesson as taught, with its references. It is written once and never changes.
- `lessons/<n>-<m>-<slug>.md`: supplements to lesson `<n>`. An answer that needs depth, a re-explanation or a correction to a lesson gets a supplement; a quick question is answered in the chat.
- `exercises/<n>-<slug>/`: the lesson's exercise in `README.md`, with its starter files, tests and your work.

Say "continue my <subject> course" to resume in a later conversation.

Guided Learning replaces Collaborative Learning, which has been removed from this collection; its source and citation rules carry over. The diagnosis and check design adapt ideas from [LearnHarness](https://github.com/amosblomqvist/learnharness).

See [SKILL.md](SKILL.md) for the agent workflow.
