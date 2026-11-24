# Records

Keep subject folders where the student says. If they don't say, create `<subject-slug>/` in the current working directory and tell them the path.

```text
<subject-slug>/
├── progress.md
├── lessons/
│   ├── 01-<lesson-slug>.md
│   ├── 02-<lesson-slug>.md
│   └── 02-1-<supplement-slug>.md   supplement 1 to lesson 2
└── exercises/
    └── 02-<lesson-slug>/
        ├── README.md               the exercise for lesson 2
        └── ...                     starter files, tests and the student's work
```

## Progress file

`progress.md` holds the course's state:

```markdown
# <Subject>

Goal: <the concrete goal, in the student's words where possible>
Resources:
- <author, title, edition; path or URL>: <what it is used for>
Syllabus: draft | approved | complete (revision <n>, <date>)
Current: Lesson <n>, <lesson | exercise | check | re-explanation>

## Level (<date>)
| Strand | Level | Evidence |
|---|---|---|
| <strand> | solid / shaky / missing | <answers that show it> |

Misconceptions: <each wrong model found, or "none found">

## Syllabus
| # | Lesson | Concepts | Exercise | Sources | Status |
|---|---|---|---|---|---|
| 1 | <title> | <key ideas> | <what the student does> | <primary source, sections; secondary sources> | done |
| 2 | <title> | <key ideas> | <what the student does> | <primary source, sections; secondary sources> | in progress |
| 3 | <title> | <key ideas> | <what the student does> | <primary source, sections; secondary sources> | pending |

## Log
- <date>: Diagnosis complete, syllabus drafted.
- <date>: Syllabus approved.
- <date>: Lesson 1 exercise passed, check 3/3, done.
- <date>: Lesson 2 exercise passed, check 1/3, missed <idea> (held <wrong model>), re-explained in supplement 2-1.
- <date>: Revision 2: inserted lesson 2a "<title>" for a missing prerequisite.
- <date>: Supplement 2-2 "<title>" for the student's question on <topic>.
```

## Lesson notes

A lesson note holds the lesson as delivered and its references:

```markdown
# Lesson <n>: <title>

<the lesson as delivered, with numbered references>

## References
1. <full entry>
```

Write the note once, when you deliver the lesson, and never change it afterwards. Whatever you write for the lesson afterwards goes elsewhere: a deeper answer, a re-explanation or a correction becomes a supplement, and exercise and check results go in the log.

## Exercises

`exercises/<n>-<lesson-slug>/README.md` holds the exercise as set: the task, its steps with the practical explanation each one needs, how the student checks their work, and the references. Starter files, tests and the student's work sit beside it.

## Supplements

A supplement is a file of its own that belongs to a delivered lesson. It holds an answer that needs more depth than a short answer in the chat, a re-explanation of ideas the student missed, or a correction to the lesson. If you find that something you taught was wrong, tell the student and write the correction, with its reference, as a supplement. A quick question gets its answer in the chat and needs no supplement.

- Name the file `lessons/<n>-<m>-<slug>.md`: `<n>` is the lesson's number, `<m>` counts that lesson's supplements from 1, and the slug names the supplement's own topic, as in `04-1-traits-and-closures.md`.
- Open it with `# Supplement <n>-<m>: <title>`, the lesson it belongs to and what prompted it: the student's question verbatim, or the idea they missed.
- Write it like a lesson, as [teaching.md](teaching.md) describes, and log it in `progress.md`.

## Writing

Save lessons, exercises and supplements in full, because the student rereads them to study and a summary would lose the explanation. Write each record in the same turn as the event it records, before the reply that reports it, so an interrupted conversation loses nothing. If a write fails, tell the student.

## Resuming

Read `progress.md`, the current lesson's note and its exercise. Tell the student in a line or two where the course stands, then continue from the recorded stage. If a check was posed but not answered, pose a new one. If you can't find the subject's folder, ask where it is instead of starting over.
