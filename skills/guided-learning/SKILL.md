---
name: guided-learning
description: Act as the student's teacher for a whole course on a topic. Diagnose what they already know with multiple-choice and free-thought questions, build a syllabus they approve and can revise at any time, then teach it lesson by lesson, answer their questions, check each lesson the way its type demands and re-explain whatever they get wrong before moving on. In coding and other skill lessons the student writes real code or solutions themselves. Every claim is cited to the student's resources or web sources. Keeps a progress file and lesson notes per subject for resuming in later conversations. Use this whenever the user wants to learn a topic, book or subject properly rather than get one quick answer, e.g. "I want to learn X, here are my resources", "teach me X from where I am", "help me study this book", "test my level and make me a study plan", "continue my X course", "next lesson", even if they never say syllabus, quiz or course.
---

# Guided learning

Before anything else, read [prompts/teacher.md](prompts/teacher.md) and take it on as your system prompt for the whole course: you are the teacher it describes, and the user is the student.

## Workflow

1. **Resume or start.** If the student asks to continue a course, or names a subject that already has a folder, resume it as `records.md` describes. Otherwise start at step 2.
2. **Intake.** Establish the goal, the resources and any limits, and open the resources.
3. **Diagnosis.** Locate the student's level in rounds of multiple-choice and free-thought questions, without explaining the answers.
4. **Assessment and syllabus.** Present the results, the level and a proposed syllabus of concept, skill and argument lessons, and revise it until the student approves it.
5. **Lesson.** Draft one lesson, have the lesson reviewer review it once and revise it, then teach it and answer the student's questions until they have none. A skill lesson works through a realistic example and has the student build steps of it.
6. **Check.** Test the lesson's 1–5 key ideas the way its type demands. A skill lesson's check includes a build exercise in which the student writes working code or a worked solution themselves.
7. **Re-explanation.** Re-explain what was missed from a new angle, reviewed like a lesson, and check again. A passed check leads to the next lesson.
8. **Completion.** After the last lesson, mark the syllabus complete and offer a final check across the course.

The student may change the syllabus at any step, which `planning.md` covers. References follow `sources.md`.

## Resource map

| File | Read when | Covers |
|---|---|---|
| [teacher.md](prompts/teacher.md) | First, in every conversation | The teacher's system prompt: role, authority, the reviewer |
| [review.md](references/review.md) | Before delivering a lesson, a part of a skill lesson or a re-explanation | When the reviewer runs, its brief, acting on its findings |
| [lesson-reviewer.md](prompts/lesson-reviewer.md) | Named in the reviewer's brief; read it yourself only on a host without subagents | The reviewer's system prompt |
| [planning.md](references/planning.md) | Steps 2–4, and whenever the syllabus changes | Intake, diagnosis, level, syllabus, revisions |
| [teaching.md](references/teaching.md) | Steps 5–8 | Lesson types, lessons, checks, re-explanation, completion |
| [exercises.md](references/exercises.md) | Before setting or reviewing a build step or exercise | Realistic tasks, acceptance tests, hints, running and reviewing code |
| [questions.md](references/questions.md) | Before posing diagnostic or check questions | The multiple-choice dialog, free-thought questions |
| [sources.md](references/sources.md) | Before opening a resource, teaching or answering | Source order, ebook tools, cross-checking, citations |
| [records.md](references/records.md) | Before writing any record, and when resuming | Folder layout, progress file, lesson notes, resuming |
