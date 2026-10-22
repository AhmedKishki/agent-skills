# 8. Errors

Operating systems usually report errors through return codes, `errno` or C++ exceptions, and leave the checking to the application. Section 6.7 argues that a framework can do better. Through [inversion of control](glossary.md#inversion-of-control) it already controls much of the application, so it can watch that the application keeps its side of the agreement and stop when it does not.

## Design by contract

Samek takes the method of *[Design by Contract](glossary.md#design-by-contract)* (DbC) from Bertrand Meyer (section 6.7.1). A system is a set of components that collaborate on the basis of precisely defined mutual obligations, the *contracts*. In C, contracts are written as [assertions](glossary.md#assertion) and checked at run time.

A contract does not prevent an error and does not handle it. It declares a condition to be an error. Samek's framework, for example, asserts that a published signal lies in the configured range. An application that publishes a signal out of range is stopped, because such a signal means that the program has lost the consistency of its signals, ‘a sure sign of a larger problem (a broken build, perhaps)’.

*Defensive programming* takes the opposite line: it makes operations accept a wider range of inputs and orders, and so it lets the code ‘wonder around’ while it quietly works around invalid conditions. Samek's objection is that defensive programming often hides bugs. DbC holds that a program is either in full control of what happens or it is not, and that a failed safeguard calls for facing the problem at once and putting the system into a fail-safe state.

## Errors and exceptional conditions

The method rests on a distinction between two kinds of trouble (section 6.7.2):

- An **error** is a bug, a persistent defect in design or implementation, such as an array index out of range or a NULL pointer dereferenced. [Assertions](glossary.md#assertion) document such ‘logically impossible situations’ so that they are discovered. Once the impossible has happened, the program can no longer be trusted, so the first priority is to detect it early.
- An **[exceptional condition](glossary.md#exceptional-condition)** is a rare situation that can legitimately arise in the life of the system, such as a failed sensor. The design must handle it with a recovery strategy.

Handling a bug as if it were an exceptional condition makes things worse. It adds code that only hides the bug and can bring new bugs. Assertions have the opposite effect: every condition they declare an error is a condition the code does not have to handle, which simplifies the software.

### Exceptional conditions are states

In an [active object](glossary.md#active-object), a change of behaviour is a change of state, so a state machine is the natural place to handle an exceptional condition (section 6.7.4). A common [superstate](glossary.md#superstate) holds a high-level transition to the *exceptional* part of the machine, and its submachine holds the normal behaviour. An action that meets the exceptional condition posts a [Reminder](glossary.md#reminder) event to the object itself, which triggers the high-level transition. The [exit actions](glossary.md#exit-action) on the way out clean up the normal context. Samek advises against C++ exceptions in event-driven code, because unwinding the stack conflicts with [run-to-completion](glossary.md#run-to-completion) processing.

## Assertions in practice

The book's [assertion](glossary.md#assertion) macros resemble the standard `assert()` and add a few things (section 6.7.3):

| Macro | Purpose |
|---|---|
| `Q_ASSERT(test)` | a general assertion |
| `Q_REQUIRE`, `Q_ENSURE`, `Q_INVARIANT` | assertions that document a precondition, a postcondition and an invariant, names taken from the Eiffel language |
| `Q_ALLEGE(test)` | an assertion whose test is evaluated even when assertions are disabled, for tests with side effects |
| `Q_ERROR()` | an assertion that always fails |

Every failed assertion calls one application-defined function, `Q_onAssert(file, line)`. On an embedded system it typically disables interrupts, tries to put the system into a fail-safe state and resets it. It should also leave ‘a “trail of bread crumbs”’ such as the file name and line number in non-volatile memory, and during development it is the ideal place for a breakpoint. Each file stores its name once, so that the assertions do not fill the code memory with copies of the same string.

## Shipping with assertions

Common practice uses [assertions](glossary.md#assertion) during development and removes them from the product. Samek quotes C.A.R. Hoare, who compared that to wearing a lifebelt during practice and leaving it ashore for the real voyage (section 6.7.5). Two questions decide the matter. The first is overhead: Samek's view is that assertions should be part of the software, with the hardware sized for them, and that they often pay for themselves by replacing error-handling code that hides bugs. The second is the response in the field, which has to be designed. Safety-critical systems may need redundancy and a recovery strategy. For many other products, ‘a simple system reset turns out to be the least inconvenient action from the user’s perspective’, and certainly better than a locked-up application.

## Event delivery is a contract

A queue that overflows or a pool that is exhausted is an error of the same kind as a stack overflow (section 6.7.6). The framework asserts that every queue accepts every event and that every requested event can be allocated, and sizing the queues and pools is the application's job. [Events and queues](02-events-and-queues.md) describes the argument and the sizing methods.

## In the skill

The skill reports a bug with `AO_ERROR()`, which mirrors `Q_ERROR()` and `Q_onAssert()`. A development build always stops there. Decision D12 sets what a production build does: by default it records the fault, makes the outputs safe and restarts, as section 6.7.5 recommends. The other option records the fault and returns, so that the fallback written after the call keeps the product working. `references/handlers.md` applies the distinction of section 6.7.2: expected problems become states and events, and only real errors reach D12.
