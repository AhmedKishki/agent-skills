# Exercises

A build exercise has the student produce the work a skill lesson teaches: code that runs, a solved problem, a derivation. Every skill lesson's check contains at least one, and the lesson's worked example hands the student smaller build steps of the same kind.

## Setting the task

- **Make it realistic.** Set a task a practitioner would meet, sized so the student can finish it in one sitting: a ring buffer for a UART driver, a parser for a configuration file, a command-line tool that processes real input. A toy task, such as printing a list, tests syntax but not the decisions the skill is about: structure, edge cases, errors and interfaces.
- **Set it in the student's field** when you know it, because a task they recognise from their own work shows where the skill applies.
- **Make it need the lesson's ideas**, so that a solution that avoids them can't pass. Needing skills from earlier lessons as well keeps those in practice.
- **Specify it completely**: what to build, the inputs and outputs, the constraints and the acceptance criteria. For code, write the acceptance criteria as tests or example runs that the student can execute themselves.

Put starter files and tests in `<subject>/exercises/<n>-<lesson-slug>/` and tell the student which file their code goes in. Limit starter code to what the exercise is not about, such as build files and test harnesses, so the student writes everything the lesson teaches.

## While the student works

The student writes the solution, because writing it is the practice. When they are stuck, give the smallest hint that unblocks them: a question, the name of the concept they need, or the line where the problem shows. Give a full solution only when they ask for one. A student who has read a solution has not yet shown they can produce one, so then pose a fresh exercise on the same idea.

## Reviewing

Run the student's code against the acceptance tests and report the actual output, because code that reads correctly can still fail. If the toolchain is missing, say what to install, or ask the student to run the tests and paste the output.

The exercise passes when the work meets the acceptance criteria and uses the lesson's ideas soundly. Then review it as a senior colleague would: name what is unidiomatic, fragile or unclear, and why. Only a failure of the lesson's ideas counts against the verdict.

When the exercise fails, re-explain the idea behind the failure as [teaching.md](teaching.md) describes, then have the student fix their own code, because finding and fixing their own error is part of the skill. Leave the student's files as they wrote them and put your corrections in the review.

Once the exercise passes, you may show a reference solution for comparison, labelled as one way to solve it.
