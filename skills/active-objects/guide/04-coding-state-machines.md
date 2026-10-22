# 4. Coding state machines

Chapter 3 compares the standard ways of writing a state machine in C and C++, and chapter 4 builds Samek's own [event processor](glossary.md#event-processor) for nested states. Both chapters end with practical rules, which section 4.7 collects as pitfalls.

## Two functions drive every state machine

State machine code is often tangled with one concurrency model, such as a polling loop that reads events straight from hardware registers (section 3.2). Samek separates the two with an interface of two functions. `init()` takes the top-level [initial transition](glossary.md#initial-transition) once. `dispatch()` delivers one event and returns after the RTC step. Whoever owns the machine calls `init()` once and `dispatch()` for each event. An event reaches `dispatch()` as one object with a signal and optional parameters (see [Events and queues](02-events-and-queues.md)).

## Four standard techniques

Chapter 3 codes one example, a time bomb, in four ways and lists the consequences of each.

| Technique | How it works | Gains | Costs |
|---|---|---|---|
| Nested `switch` (3.3) | A `switch` on a state variable, with a `switch` on the signal inside each case. | Simple, and one small state variable in RAM. | One monolithic function, no reuse, no hierarchy. Entry and exit actions have to be repeated on every transition into and out of a state. |
| [State table](glossary.md#state-table) (3.4) | A two-dimensional table indexed by state and signal holds pointers to action functions. | Regular, constant dispatch time, the table can live in ROM. | A large, sparse table whose initialisation must match the enumerations. A new state needs a whole new row, so programmers avoid adding states and add guards and flags in their place. No hierarchy. |
| Object-oriented State pattern (3.5) | One class per state, and the context object delegates each event to its current state object. | Efficient transitions and dispatch, typed [event parameters](glossary.md#event-parameter). | Needs C++. Every state class needs access to the context's data, which breaks its encapsulation. A new event changes the abstract state interface. No hierarchy. |
| [State-handler functions](glossary.md#state-handler-function) (3.6) | One function per state, and the state variable is a pointer to the current state's function. | Every element of the machine appears in the code exactly once, one pointer of RAM, a tiny generic processor, and a direct path to hierarchy. | Signals must be enumerated. |

Samek's summary singles out the last technique because it ‘offers an optimal combination of good performance and a small memory footprint’ (section 3.8). He also notes that in all but the nested `switch`, even the explicit test of the state variable disappears from the code.

Two remarks apply to every technique (section 3.7). A [guard](glossary.md#guard) maps to an `if`, and a choice point to a chain of `if` and `else if` with non-overlapping conditions. Entry and [exit actions](glossary.md#exit-action) can be added to a flat machine by sending the reserved signals ENTRY and EXIT: on a transition, the processor sends EXIT to the source and ENTRY to the target.

## State-handler functions

A [state-handler function](glossary.md#state-handler-function) receives every event that arrives while its state is active and returns a status that tells the processor what happened (sections 3.6 and 4.4). In the book's QEP processor the statuses are:

- `Q_HANDLED()`: the event was handled, and the state stays.
- `Q_IGNORED()`: the event was ignored (flat machines and the [top state](glossary.md#top-state)).
- `Q_TRAN(target)`: take a transition to `target`. The macro assigns the state variable and returns the status in one expression.
- `Q_SUPER(parent)`: this state does not handle the event, so pass it to `parent` (nested machines).

The reserved signals `Q_ENTRY_SIG`, `Q_EXIT_SIG` and `Q_INIT_SIG` arrive at the same function, so a state's [entry action](glossary.md#entry-action), [exit action](glossary.md#exit-action) and [initial transition](glossary.md#initial-transition) sit in the same `switch` as its reactions (section 4.5.4). User signals begin after them, at `Q_USER_SIG`. The keyboard of chapter 2 written in this style looks as follows (an illustration in the book's style, with names of the guide's own):

```c
QState Keyboard_default(Keyboard *me, QEvent const *e) {
    switch (e->sig) {
        case ANY_KEY_SIG: {
            send_lower_case_scan_code();
            return Q_HANDLED();
        }
        case CAPS_LOCK_SIG: {
            return Q_TRAN(&Keyboard_caps_locked);
        }
    }
    return Q_IGNORED();
}
```

The flat processor needs only a few lines (section 3.6.1). `dispatch()` saves the current state, calls its function with the event and, if the answer is a transition, calls the old state with EXIT and the new state with ENTRY. The transition's own actions have already run inside the handler, before it returned `Q_TRAN()`, which gives the order of chapter 2: action, exit, entry.

### Nesting

For nested states, each state-handler function ends with `return Q_SUPER(&parent);` in place of `return Q_IGNORED();` (section 4.4). Any event the state does not handle, or whose [guard](glossary.md#guard) fails, therefore goes to its [superstate](glossary.md#superstate). The outermost states name `QHsm_top`, the top state, which ignores every event and must never be the target of a transition (section 4.5.3). A state with [substates](glossary.md#substate) answers `Q_INIT_SIG` with `Q_TRAN()` to one of them, which is its initial transition.

The machine starts from an *initial [pseudostate](glossary.md#pseudostate)*, a function that may run actions and names the default state. `QHsm_init()` takes this topmost initial transition exactly once and then follows the nested initial transitions down to a [leaf state](glossary.md#leaf-state) (section 4.5.6).

Dispatching an event to a nested machine works in two parts (sections 4.5.7 and 4.5.8):

1. The processor calls the current leaf state, and then its superstates in turn, until one handles the event or the top state ignores it.
2. If the handler returned a transition, the processor finds the [least common ancestor](glossary.md#least-common-ancestor) of source and target, exits the states up to it, enters the states down to the target, and then follows initial transitions down to a leaf.

The processor learns a state's superstate by calling the state with a reserved *empty* signal that no state handles, so the state answers `Q_SUPER()`. Much of the processor's code orders the possible source and target configurations so that it makes as few of these calls as possible.

Section 4.1 lists what this design achieves. Every element of the state machine maps to code ‘precisely, unambiguously, and exactly once’, the hierarchy is never flattened, a state machine needs one function pointer of RAM, and the processor takes about 600 bytes of code for nested machines and about 120 bytes for flat ones on an ARM Cortex-M3.

## Pitfalls

Section 4.7 collects the mistakes that users of the processor have made over the years.

| Pitfall | What goes wrong | Remedy |
|---|---|---|
| Incomplete state handlers (4.7.1) | A helper function hides a transition, so the state can no longer be drawn from its handler alone. | Code each state as one complete handler with the idioms of section 4.6. ‘the code is as much an implementation as it is a specification’ of the machine. |
| Ill-formed state handlers (4.7.2) | Constructs that no diagram can show, such as a state nested inside itself, crash the processor or fail its [assertions](glossary.md#assertion). | Avoid them: an ill-formed machine is wrong whatever it was meant to do, and many such cases trip an assertion inside the processor. |
| Transition in an entry or [exit action](glossary.md#exit-action) (4.7.3) | The designer treats a state as a stage of a flowchart. UML does not allow it. | Two transitions with complementary [guards](glossary.md#guard) and different targets. |
| Wrong event cast (4.7.4) | One signal is used for several event structures, and a handler casts the event to the wrong one. | Each signal identifies exactly one event structure. |
| [Event parameters](glossary.md#event-parameter) in entry or exit actions (4.7.5) | By the time the target's [entry action](glossary.md#entry-action) runs, the triggering event is out of reach. The action receives the reserved ENTRY event. | Act on the parameters in the transition, or store them in [extended state variables](glossary.md#extended-state-variable) first. |
| [Initial transition](glossary.md#initial-transition) to a state outside the composite (4.7.6) | The machine is ill-formed and the processor crashes. | Target a direct or indirect [substate](glossary.md#substate). Initial transitions have no guards (4.6.7). |
| Code outside the `switch` (4.7.7) | The processor calls handlers several times per event, for the empty signal among others, so any code outside the `switch` runs on each call. | Keep all code, including local variable initialisation, inside the cases. |
| Wrong signal granularity (4.7.8) | Too many signals bloat the handlers, too few force guards on parameters. | Remap signals before dispatching (see [Events and queues](02-events-and-queues.md)). |
| Breaking [run to completion](glossary.md#run-to-completion) (4.7.9) | An interrupt dispatches an event to a machine that is still busy with the previous one. | Queue events and dispatch them one at a time. |
| Corrupting the current event (4.7.10) | The memory of the current event is overwritten before the step ends. | Queues, and a framework that controls event memory. |

## In the skill

Decision D9 defaults to [state-handler functions](glossary.md#state-handler-function), and `references/state-machines.md` shows them flat and nested in the skill's own names. Its rules require that each state's function holds all of that state and works only inside its `switch`, that [initial transitions](glossary.md#initial-transition) have no [guard](glossary.md#guard) and target an inner state, and that no state change happens inside an entry or [exit action](glossary.md#exit-action).
