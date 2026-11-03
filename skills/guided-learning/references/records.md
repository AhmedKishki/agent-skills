# Records

Keep subject folders where the student says. If they don't say, create `<subject-slug>/` in the current working directory and tell them the path.

```
<subject-slug>/
├── progress.md
├── lessons/
│   ├── 01-<lesson-slug>.md
│   └── 02-<lesson-slug>.md
└── exercises/
    └── 02-<lesson-slug>/   starter files, tests and the student's code
```

## Progress file

`progress.md` holds the course's state:

```markdown
# <Subject>

Goal: <the concrete goal, in the student's words where possible>
Resources:
- <author, title, edition; path or URL>: <what it is used for>
Syllabus: draft | approved | complete (revision <n>, <date>)
Current: Lesson <n>, <teaching | questions | check | re-explanation>

## Level (<date>)
| Strand | Level | Evidence |
|---|---|---|
| <strand> | solid / shaky / missing | <answers that show it> |

Misconceptions: <each wrong model found, or "none found">

## Syllabus
| # | Lesson | Type | Covers | Sources | Status |
|---|---|---|---|---|---|
| 1 | <title> | concept | <key ideas> | <source, sections> | done |
| 2 | <title> | skill | <key ideas> | <source, sections> | in progress |
| 3 | <title> | argument | <key ideas> | <source, sections> | pending |

## Log
- <date>: Diagnosis complete, syllabus drafted.
- <date>: Syllabus approved.
- <date>: Lesson 1 check 3/3, done.
- <date>: Lesson 2 check 1/3, missed <idea> (held <wrong model>), re-explained with <angle>.
- <date>: Revision 2: inserted lesson 2a "<title>" for a missing prerequisite.
```

## Lesson notes

Each lesson note holds what the student would want to reread:

```markdown
# Lesson <n>: <title>

## Lesson
<the lesson as delivered, with numbered references>

## Questions
**Student:** <their question, verbatim>
**Teacher:** <the answer as given>

## Check <k>
1. <question with its options, or the exercise task>
   - Answer: <the student's answer, or the path to their code and the test output>
   - Verdict: correct | incorrect, <reason> [<ref>]

## Re-explanation <k>
<the re-explanation as delivered>

## Corrections
- <date>: <what was wrong, what is right> [<ref>]

## References
1. <full entry>
```

Save lessons, answers and re-explanations as delivered, because the student rereads the notes to study and a summary would lose the explanation. If you find that something you taught was wrong, tell the student, correct it with a reference and add it under Corrections instead of rewriting the original, so the note shows what changed.

## Writing

Write each record in the same turn as the event it records, before the reply that reports it, so an interrupted conversation loses nothing. If a write fails, tell the student.

## Resuming

Read `progress.md` and the current lesson's note. Tell the student in a line or two where the course stands, then continue from the recorded stage. If a check was posed but not answered, pose it again. If you can't find the subject's folder, ask where it is instead of starting over.
