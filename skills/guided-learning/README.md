# Guided Learning

Learn a topic, book or subject with an agent that acts as your teacher. It measures your level first, plans a syllabus from there to your goal, and teaches it lesson by lesson until each lesson's ideas hold.

Start with a request such as:

> I want to learn Bayesian statistics well enough to read applied papers. Here is the book I'm using: ~/books/statistical-rethinking.pdf

The agent asks for anything the request leaves open and then poses diagnostic questions: multiple-choice in a clickable dialog, free-thought in the chat. It shows your results and your level per concept, and proposes a syllabus that skips what you already know. Teaching starts once you approve the syllabus, and you can change it at any point.

After each lesson you can ask questions. When you have none, the agent checks your understanding with one to five questions. If you miss something, it re-explains that idea from a different angle and checks again with new questions before it moves on.

Every claim cites your resources or a web source, with a page or section, so you can check it. Ebooks are read through an ebook MCP server such as ebook-hero when one is connected.

Each subject gets a folder:

- `progress.md`: goal, level, syllabus with status, and a log of check results.
- `lessons/<n>-<slug>.md`: each lesson as taught, with your questions, the checks, re-explanations and references.

Say "continue my <subject> course" to resume in a later conversation.

Guided Learning replaces Collaborative Learning, which has been removed from this collection; its source and citation rules carry over. The diagnosis and check design adapt ideas from [LearnHarness](https://github.com/amosblomqvist/learnharness).

See [SKILL.md](SKILL.md) for the agent workflow.
