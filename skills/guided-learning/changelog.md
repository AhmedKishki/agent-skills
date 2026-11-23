---
name: changelog.md
description: Records the enduring user-visible history of the guided-learning skill.
---

# Changelog

This is the single enduring changelog for `guided-learning`. Current behaviour is governed by `SKILL.md`; historical entries describe the behaviour of their version.

## 1.6.0 — 2026-11-23

- A lesson teaches concepts through intuition: why each thing works as it does, in direct, concise language. Every idea is motivated, an idea gets at most one example of a few lines, and a diagram shows a concept wherever one can.
- Every lesson has a guided exercise, set after the student's questions. Each of its ordered steps has the student use one of the lesson's concepts and explains the practical side: the procedure, syntax, tools or method. The exercise is written to `exercises/<n>-<slug>/README.md`, beside its starter files and tests, and the teacher does it before setting it.
- Lesson types (concept, skill, argument) are gone, and with them the long worked example inside a skill lesson. The syllabus names each lesson's concepts and exercise in place of a type, and the check after the exercise is 1–5 questions on the key ideas.
- A lesson note holds the lesson and its references, is written once and never changes. A re-explanation is a supplement, like a deep answer or a correction, and exercise and check results go in the progress log.

## 1.5.0 — 2026-11-23

- The lesson reviewer is gone: lessons, supplements and re-explanations go to the student without a review pass. `prompts/lesson-reviewer.md` and `references/review.md` are removed, and the progress log no longer records review findings.

## 1.4.0 — 2026-11-19

- A delivered lesson's text never changes. While a lesson is current, its note still gains the student's questions, the checks and re-explanations; after that it stays as it is.
- A conceptual question that needs more depth than a short answer gets a supplement: `lessons/<n>-<m>-<slug>.md`, for supplement `<m>` to lesson `<n>`, reviewed like a lesson and logged. A quick question is answered in the chat.
- A correction to a delivered lesson goes into a supplement to that lesson. The lesson note's Corrections section is gone.

## 1.3.0 — 2026-11-18

- The teacher's role is a system prompt, `prompts/teacher.md`, which the agent takes on before anything else.
- A lesson reviewer, a subagent with its own system prompt in `prompts/lesson-reviewer.md`, reviews every lesson, every part of a skill lesson and every re-explanation once before the student sees it. It reports unmotivated steps, superfluous sentences and AI tells, and claims that the cited sources, code runs or calculations don't bear out, each with its evidence.
- The teacher fixes the findings that hold up and ignores the rest, without a second review round. The student sees only the revised lesson; the review stays out of the subject folder, and the progress log records the number of findings and fixes.
- On a host without subagents, the teacher runs the reviewer prompt as a separate pass over the finished draft.

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
