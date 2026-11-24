# Teaching

A lesson teaches concepts: it builds the student's intuition for why each thing works as it does. Its exercise then teaches how to use them, as [exercises.md](exercises.md) describes.

## Lessons

Start from what the level assessment says the student holds, and build each idea on the one before it.

Explain each concept in this order, so that each part answers the question the part before it raises:

1. **The problem it solves.** Say what goes wrong, or what the student can't do, without the concept, and that the concept is the answer, in a sentence or two the student could repeat. This is the point of the concept, and it comes before any detail of how it works. Use the source's own statement of it where it has one.
2. **How it solves it.** The mechanism underneath, and why it is built that way.
3. **Its own problems.** What it costs and where it breaks.
4. **The other solutions.** What else solves the same problem, and when each is the better choice. A line on each is enough, with the lesson that teaches it where the syllabus has one.
5. **How to apply it.** Where it is used and what the student writes to use it. Leave procedure and tooling to the exercise.
6. **The intuition.** The picture the student keeps: the source's own where it has one, tied to something the student already knows, such as a C++ vector set against a Python list for a student who knows Python.

Keep each part as short as the concept allows, and leave a part out only when the concept has nothing for it. Throughout the lesson:

- **Go deep, not broad.** Teach each concept until the student could predict what happens in a case the lesson didn't show. Apart from the other solutions in part 4, don't mention an idea in passing: a mention without an explanation leaves a gap the student trips on. An idea that doesn't fit at that depth belongs in another lesson, since breadth comes from more lessons.
- **Be concrete.** Say exactly what happens: which code runs, in what order, what is in memory before and after, which value results. Replace every vague phrase, such as "handles", "takes care of", "under the hood" or "builds it twice", with the steps it stands for, and show a claim about behaviour (an order, a count, a cost) with a run or a trace the student can check. A sentence the student couldn't redraw as a concrete picture needs rewriting.
- **Explain every construct you show.** The student must be able to read each line of an example. Syntax they haven't been taught, such as what `T x{arg};` declares or why a class definition ends in `;`, is explained where it first appears.
- **Motivate every point.** A sentence, an example or a detail belongs in the lesson when it answers a question the student has at that moment, because the student accepts an idea more easily when it answers a question they already have. If you can't say why the student needs a point here, leave it out.
- **Keep it simple.** Use the simplest language, form and example that carry the point: if a plainer word, a simpler layout or a smaller example would say the same, use it. State each point once. Don't narrate the structure ("first I will explain X, then Y") or summarise what you just said.
- **Keep examples short.** Give an idea at most one example, a few lines long, cut down to the lines that show the idea. Longer worked material belongs in the exercise.
- **Draw a diagram wherever one can show a concept**: a memory layout, a data structure, a state machine, events over time, data flowing between components, the state before and after a step, alternatives side by side. A diagram shows a whole structure at once, where prose makes the student rebuild it sentence by sentence. Give each diagram one idea and label every part. Draw it in ASCII, which displays everywhere, including the chat; use Mermaid only where the student reads the notes in a viewer that draws it, and save what ASCII can't show, such as a plot, as an image beside the lesson note and link it. Use a table for a comparison.
- **Define each term** where it is first used. When the lesson needs a term or result from an earlier lesson, restate it in a sentence instead of pointing back, because the student rereads each lesson note on its own.
- **Teach a text's argument by its structure**: the question it answers, the claim, its grounds, the steps from grounds to claim and the limits of the conclusion. Keep the source's qualifications, since dropping one changes what the source claims.
- **Follow the lesson's primary source** and cite a source for every claim, as [sources.md](sources.md) describes.

Supplements and answers in the chat follow the same rules. An answer to a narrow question gives the point first, then only the parts the question needs.

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
