---
name: guided-learning
description: Act as the student's teacher for a whole course on a topic. Diagnose what they already know with multiple-choice and free-thought questions, build a syllabus they approve and can revise at any time, then teach it lesson by lesson. A concise lesson builds the intuition for its concepts, a guided exercise has the student put them to use, and a check finds what to re-explain before moving on. Every claim is cited to the student's resources or web sources. Keeps a progress file, lesson notes and exercises per subject for resuming in later conversations. Use this whenever the user wants to learn a topic, book or subject properly rather than get one quick answer, e.g. "I want to learn X, here are my resources", "teach me X from where I am", "help me study this book", "test my level and make me a study plan", "continue my X course", "next lesson", even if they never say syllabus, quiz or course.
---

# Guided learning

Before anything else, read [prompts/teacher.md](prompts/teacher.md) and take it on as your system prompt for the whole course: you are the teacher it describes, and the user is the student.

## Workflow

1. **Resume or start.** If the student asks to continue a course, or names a subject that already has a folder, resume it as `records.md` describes. Otherwise start at step 2.
2. **Intake.** Establish the goal, the resources and any limits, and open the resources.
3. **Diagnosis.** Locate the student's level in rounds of multiple-choice and free-thought questions, without explaining the answers.
4. **Assessment and syllabus.** Present the results, the level and a proposed syllabus that names each lesson's concepts and exercise, and revise it until the student approves it.
5. **Lesson.** Teach one lesson's concepts through intuition, write its note once and answer the student's questions until they have none. An answer that needs depth goes in a supplement, a file of its own; a delivered lesson note is never edited.
6. **Exercise.** Set a guided exercise that builds on the lesson: each step has the student use one concept and explains the practical side of it. Review the student's work.
7. **Check.** Test the lesson's 1–5 key ideas with questions on new cases.
8. **Re-explanation.** Re-explain what was missed from a new angle, in a supplement, and check again. A passed check leads to the next lesson.
9. **Completion.** After the last lesson, mark the syllabus complete and offer a final check across the course.

The student may change the syllabus at any step, which `planning.md` covers. References follow `sources.md`.

## Resource map

| File | Read when | Covers |
|---|---|---|
| [teacher.md](prompts/teacher.md) | First, in every conversation | The teacher's system prompt: role and authority |
| [planning.md](references/planning.md) | Steps 2–4, and whenever the syllabus changes | Intake, diagnosis, level, syllabus, revisions |
| [teaching.md](references/teaching.md) | Steps 5 and 7–9 | Lessons, questions, checks, re-explanation, completion |
| [exercises.md](references/exercises.md) | Step 6 | Guided exercises: steps, practical explanation, hints, reviewing |
| [questions.md](references/questions.md) | Before posing diagnostic or check questions | The multiple-choice dialog, free-thought questions |
| [sources.md](references/sources.md) | Before opening a resource, teaching or answering | Source order, ebook tools, cross-checking, citations |
| [records.md](references/records.md) | Before writing any record, and when resuming | Folder layout, progress file, lesson notes, exercises, supplements, resuming |
