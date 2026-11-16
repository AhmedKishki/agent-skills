---
name: changelog.md
description: Records the enduring user-visible history of the guided-learning skill.
---

# Changelog

This is the single enduring changelog for `guided-learning`. Current behaviour is governed by `SKILL.md`; historical entries describe the behaviour of their version.

## 1.2.0 — 2026-11-16

- Lessons, answers and re-explanations draw a picture wherever it makes an explanation clearer: memory layouts, data structures, state machines, timelines, data flow, before-and-after states. ASCII is the default because it renders everywhere; Mermaid is used where the notes' viewer draws it, and plots are saved as images beside the lesson note.
- A re-explanation can take a diagram as its new angle.

## 1.1.0 — 2026-11-04

- Each lesson has a type, recorded in the syllabus: concept, skill or argument. The type decides how the lesson is taught and how its check tests it.
- Skill lessons, such as coding lessons, work through a realistic example and hand the student steps of it to build. Their check includes at least one build exercise: a realistic task with acceptance tests that the student solves themselves.
- The agent runs the student's code against the tests and reviews it. A failed exercise goes back to the student to fix, with hints only and a full solution only on request.
- Exercise files live in `<subject>/exercises/<n>-<lesson-slug>/`. Progress files without a type column still resume.

## 1.0.0 — 2026-11-03

- First version. Replaces `collaborative-learning`, which is removed from the collection.
- Diagnoses the student's level with multiple-choice and free-thought questions, then proposes a syllabus built from that level, which the student approves and can revise at any time.
- Teaches lesson by lesson. Each lesson ends with the student's questions and a check of 1–5 questions; missed ideas are re-explained and checked again with new questions.
- Cites every claim. Ebooks are read through an ebook MCP server when one is connected, web sources are used when the student names none, and claims from the agent's own knowledge are marked unsourced when no source confirms them.
- Records `progress.md` and lesson notes per subject. Projects created by `collaborative-learning` (`learning-plan.md`, `sessions/`) are not resumed.
