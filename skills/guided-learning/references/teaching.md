# Teaching

A lesson teaches concepts: it builds the student's intuition for why each thing works as it does. Its exercise then teaches how to use them, as [exercises.md](exercises.md) describes.

## Lessons

Start from what the level assessment says the student holds, and build each idea on the one before it.

- **Teach each concept through intuition.** Explain the mechanism underneath it and why it is built that way, in terms of something the student already knows, such as a C++ vector set against a Python list for a student who knows Python. Leave procedure, syntax and tooling to the exercise.
- **Motivate everything in the lesson.** Open each idea with the problem it solves or the question it answers, because the student accepts an idea more easily when it answers a question they already have. If you can't say why the student needs a point here, leave it out.
- **Write directly and concisely.** State each point once, in plain words. Don't narrate the structure ("first I will explain X, then Y") or summarise what you just said.
- **Keep examples short.** Give an idea at most one example, a few lines long, cut down to the lines that show the idea. Longer worked material belongs in the exercise.
- **Draw a diagram wherever one can show a concept**: a memory layout, a data structure, a state machine, events over time, data flowing between components, the state before and after a step, alternatives side by side. A diagram shows a whole structure at once, where prose makes the student rebuild it sentence by sentence. Give each diagram one idea and label every part. Draw it in ASCII, which displays everywhere, including the chat; use Mermaid only where the student reads the notes in a viewer that draws it, and save what ASCII can't show, such as a plot, as an image beside the lesson note and link it. Use a table for a comparison.
- **Define each term** where it is first used. When the lesson needs a term or result from an earlier lesson, restate it in a sentence instead of pointing back, because the student rereads each lesson note on its own.
- **Teach a text's argument by its structure**: the question it answers, the claim, its grounds, the steps from grounds to claim and the limits of the conclusion. Keep the source's qualifications, since dropping one changes what the source claims.
- **Cite a source for every claim**, as [sources.md](sources.md) describes.

Supplements and answers in the chat follow the same rules.

Write the lesson note as [records.md](records.md) describes and deliver the lesson in one turn. At the end, ask whether the student has questions and end your turn.

Answer each question the student asks, with references, then ask whether there are more. Answer a quick question in the chat. When a question needs a deeper explanation than a few paragraphs, write a supplement to the lesson, as [records.md](records.md) describes. A question that belongs to a later lesson gets a short answer and the lesson number that covers it. If a question shows that a prerequisite is missing, propose a syllabus change as [planning.md](planning.md) describes. When the student has no more questions, set the lesson's exercise as [exercises.md](exercises.md) describes.

## Check

Once the exercise passes, check whether the student understands the lesson's concepts. Pose 1–5 questions, one for each key idea, multiple-choice and free-thought, as [questions.md](questions.md) describes.

A good check question:

- can be answered from what the lesson and its exercise taught and what the student already held;
- makes the student use the idea on a new case (predict, apply, compare, find the error, say where an objection hits an argument) instead of repeating the lesson's sentences, because a student can repeat words they haven't understood;
- has multiple-choice distractors that each match a specific wrong idea, so a wrong pick tells you what to re-explain.

Grade each answer as correct or incorrect and give the reason in a line, with its reference. Judge free-thought answers by their reasoning, not their wording. A slip, such as an arithmetic error inside sound reasoning, counts as correct; point it out.

- **All correct:** mark the lesson `done`, name the next lesson and start it when the student says so.
- **Any incorrect:** go to re-explanation.

## Re-explanation

Re-explain only the ideas the student missed, in a supplement to the lesson, as [records.md](records.md) describes.

- **Start from the wrong answer.** It shows the student's model: name that model plainly and show the case where it breaks.
- **Come at the idea from a new angle**, such as a different example, an analogy, a diagram, smaller steps or a direct contrast with the wrong model. The first explanation already failed for this student, so repeating it rarely helps. A second source that explains the idea differently can supply the new angle.
- **Check again with new questions** on the missed ideas. The student now knows the answers to the old questions, so those can no longer show understanding.

If the student misses the same idea after two re-explanations, the syllabus has probably assumed a prerequisite they lack. Ask a question or two to find it, then propose a lesson for it as [planning.md](planning.md) describes.

## Completion

When the last lesson is done, mark the syllabus `complete` and tell the student. Offer a final check that mixes questions and exercises from across the course, graded and re-explained like any other check.
