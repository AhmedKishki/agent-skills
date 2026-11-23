# Exercises

Every lesson has an exercise, set once the student has no more questions on the lesson. The lesson explained why its concepts work; the exercise has the student use them and explains the practical side: the procedure, syntax, tools or method that using each concept takes. Its form follows the subject: code to write, a problem to solve, a derivation, an experiment the student predicts and then runs, a passage to analyse.

## Writing the exercise

- **Build each step on the lesson.** A step puts one of the lesson's concepts to use and names that concept, so the student meets in practice what the lesson explained. Together the steps cover the lesson's key ideas.
- **Guide the student through ordered steps**, each small enough to finish and check before the next one starts.
- **Explain the practical side inside the step that needs it**: how the thing is written, called, run or carried out, in a few lines, with an example of a few lines where the form is new to the student. Cite it as [sources.md](sources.md) describes.
- **Set a realistic task**, one a practitioner would meet, in the student's field when you know it, sized to finish in one sitting: a ring buffer for a UART driver, a parser for a configuration file. A task the student recognises from their own work shows them where the concept applies.
- **Specify each step completely**: what to produce, with concrete inputs and outputs, and how the student can tell it is right. For code, give acceptance tests and the command that runs them.
- **Make the steps need the lesson's concepts**, so that work which avoids them can't pass. Needing skills from earlier lessons as well keeps those in practice.

Write the exercise to `exercises/<n>-<lesson-slug>/README.md`, as [records.md](records.md) describes, and put its starter files and tests beside it. The starter files hold everything the exercise is not about, such as build files, test harnesses and signatures with stubs, so the student writes only what the steps ask for.

Before you set the exercise, do it yourself to confirm that the lesson and the steps suffice. For code, your solution must pass the acceptance tests and the starter files must fail them. Leave no solution in the exercise folder. Then tell the student where their work goes and end your turn.

## While the student works

The student does the work, because doing it is the practice. When they are stuck, give the smallest hint that unblocks them: a question, the name of the concept they need, or the line where the problem shows. Give a full solution only when they ask for one. A student who has read a solution has not yet shown they can produce one, so then set a fresh step on the same concept.

## Reviewing

Run the student's code against the acceptance tests and report the actual output, because code that reads correctly can still fail. If the toolchain is missing, say what to install, or ask the student to run the tests and paste the output.

The exercise passes when the work meets every step's criteria and uses the lesson's concepts soundly. Then review it as a senior colleague would: name what is unidiomatic, fragile or unclear, and why. Only a failure of the lesson's concepts counts against the verdict.

When a step fails, name the concept the failure comes from and explain it from the angle the failure shows, in the review, or in a supplement when it takes more than a few paragraphs. Then have the student fix their own work, because finding and fixing their own error is part of the practice. Leave the student's files as they wrote them and put your corrections in the review.

Once the exercise passes, you may show a reference solution for comparison, labelled as one way to solve it. Then go to the check, as [teaching.md](teaching.md) describes.
