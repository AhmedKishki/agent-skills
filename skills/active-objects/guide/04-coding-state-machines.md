# 4. Coding state machines

A state machine can be written in C in several standard ways. They differ in how much they repeat, how well they show the structure of the machine and whether they extend to nested states.

## Two functions drive every state machine

State machine code is often tangled with one concurrency model, such as a polling loop that reads events straight from hardware registers. A better design separates the two with an interface of two functions.[^1] `init()` takes the top-level [initial transition](glossary.md#initial-transition) once, and `dispatch()` delivers one event. Whoever owns the machine calls `init()` once and `dispatch()` for each event. An event reaches `dispatch()` as one object with a signal and optional parameters (see [Events and queues](02-events-and-queues.md)).

## Four standard techniques

| Technique | How it works | Gains | Costs |
|---|---|---|---|
| Nested `switch` | A `switch` on a state variable, with a `switch` on the signal inside each case. | Simple, and one small state variable in RAM. | One monolithic function, no reuse, no hierarchy. Entry and exit actions have to be repeated on every transition into and out of a state.[^2] |
| [State table](glossary.md#state-table) | A two-dimensional table indexed by state and signal holds pointers to action functions. | Regular, constant dispatch time, and the table can live in ROM. | A large, sparse table whose initialisation must match the enumerations. A new state needs a whole new row, so programmers avoid adding states and add guards and flags in their place. No hierarchy.[^3] |
| Object-oriented State pattern | One class per state, and the context object delegates each event to its current state object. | Efficient transitions and dispatch, typed [event parameters](glossary.md#event-parameter). | Needs C++. Every state class needs access to the context's data, which breaks its encapsulation. A new event changes the abstract state interface. No hierarchy.[^4] |
| State-handler functions | One function per state, and the state variable is a pointer to the current state's function. | Every element of the machine appears in the code exactly once, one pointer of RAM, a tiny generic processor, and a direct path to hierarchy. | Signals must be enumerated.[^5] |

[State-handler functions](glossary.md#state-handler-function) offer the best combination of performance and memory footprint of the four.[^6] In all of them except the nested `switch`, even the explicit test of the state variable disappears from the code.

Two points apply to every technique. A [guard](glossary.md#guard) maps to an `if`, and a choice point to a chain of `if` and `else if` with non-overlapping conditions. Entry and [exit actions](glossary.md#exit-action) can be added to a flat machine by sending reserved ENTRY and EXIT signals: on a transition, the processor sends EXIT to the source and ENTRY to the target.[^7]

## State-handler functions

A [state-handler function](glossary.md#state-handler-function) receives every event that arrives while its state is active and returns a status that tells the [event processor](glossary.md#event-processor) what happened.[^8] In the QEP processor the statuses are:

- `Q_HANDLED()`: the event was handled, and the state stays.
- `Q_IGNORED()`: the event was ignored, in flat machines and in the [top state](glossary.md#top-state).
- `Q_TRAN(target)`: take a transition to `target`. The macro assigns the state variable and returns the status in one expression.
- `Q_SUPER(parent)`: this state does not handle the event, so pass it to `parent`, in nested machines.

The reserved signals `Q_ENTRY_SIG`, `Q_EXIT_SIG` and `Q_INIT_SIG` arrive at the same function, so a state's [entry action](glossary.md#entry-action), [exit action](glossary.md#exit-action) and [initial transition](glossary.md#initial-transition) sit in the same `switch` as its reactions. User signals begin after them, at `Q_USER_SIG`. A keyboard with a *default* and a *caps_locked* state could be written as follows:

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

The flat processor needs only a few lines. `dispatch()` saves the current state, calls its function with the event and, if the answer is a transition, calls the old state with EXIT and the new state with ENTRY.[^9] The transition's own actions have already run inside the handler, before it returned `Q_TRAN()`, which gives the order action, exit, entry (see [State machines](03-state-machines.md)).

### Nesting

For nested states, each state-handler function ends with `return Q_SUPER(&parent);` in place of `return Q_IGNORED();`. An event that the state does not handle, or whose [guard](glossary.md#guard) fails, therefore goes to its [superstate](glossary.md#superstate). The outermost states name `QHsm_top`, the top state, which ignores every event and must never be the target of a transition.[^10] A state with [substates](glossary.md#substate) answers `Q_INIT_SIG` with `Q_TRAN()` to one of them, its initial transition, which has no guard and must target a direct or indirect substate.[^11]

The machine starts from an *initial [pseudostate](glossary.md#pseudostate)*, a function that may execute actions and names the default state. `QHsm_init()` takes this topmost initial transition exactly once and then follows the nested initial transitions down to a [leaf state](glossary.md#leaf-state).

Dispatching an event to a nested machine works in two parts:

1. The processor calls the current leaf state, and then its superstates in turn, until one handles the event or the top state ignores it.
2. If the handler returned a transition, the processor finds the [least common ancestor](glossary.md#least-common-ancestor) of source and target, exits the states up to it, enters the states down to the target, and then follows initial transitions down to a leaf.[^12]

The processor learns a state's superstate by calling the state with a reserved *empty* signal that no state handles, so the state answers `Q_SUPER()`. Much of the processor's code orders the possible source and target configurations so that it makes as few of these calls as possible.

Every element of the state machine maps to code precisely, unambiguously and exactly once, and the hierarchy is never flattened. A state machine needs one function pointer of RAM, and the processor takes about 600 bytes of code for nested machines and about 120 bytes for flat ones on an ARM Cortex-M3.[^13]

## Pitfalls

| Pitfall | What goes wrong | Remedy |
|---|---|---|
| Incomplete state handlers | A helper function hides a transition, so the state can no longer be drawn from its handler alone. | Code each state as one complete handler. The code is as much a specification of the machine as an implementation.[^14] |
| Ill-formed state handlers | Constructs that no diagram can show, such as a state nested inside itself, crash the processor or fail its [assertions](glossary.md#assertion). | Avoid them: an ill-formed machine is wrong whatever it was meant to do. |
| Transition in an entry or [exit action](glossary.md#exit-action) | The designer treats a state as a stage of a flowchart, and UML does not allow such a transition. | Two transitions with complementary [guards](glossary.md#guard) and different targets.[^15] |
| Wrong event cast | One signal serves several event structures, and a handler casts the event to the wrong one. | Each signal identifies exactly one event structure. |
| [Event parameters](glossary.md#event-parameter) in entry or exit actions | By the time the target's [entry action](glossary.md#entry-action) runs, the triggering event is out of reach, and the action receives the reserved ENTRY event. | Act on the parameters in the transition, or store them in [extended state variables](glossary.md#extended-state-variable) first.[^16] |
| [Initial transition](glossary.md#initial-transition) to a state outside the composite | The machine is ill-formed and the processor crashes. | Target a direct or indirect [substate](glossary.md#substate). |
| Code outside the `switch` | The processor calls handlers several times per event, for the empty signal among others, so code outside the `switch` executes on each call. | Keep all code, including the initialisation of local variables, inside the cases.[^17] |
| Wrong signal granularity | Too many signals bloat the handlers, too few force guards on parameters. | Remap signals before dispatching (see [Events and queues](02-events-and-queues.md)). |
| Breaking [run to completion](glossary.md#run-to-completion) | An interrupt dispatches an event to a machine that is still busy with the previous one. | Queue events and dispatch them one at a time. |
| Corrupting the current event | The memory of the current event is overwritten before the RTC step ends. | Queues, and a framework that controls event memory. |

## In the skill

Decision D9 defaults to [state-handler functions](glossary.md#state-handler-function), and `references/state-machines.md` shows them flat and nested in the skill's own names. Its rules require that each state's function holds all of that state and works only inside its `switch`, that [initial transitions](glossary.md#initial-transition) have no [guard](glossary.md#guard) and target an inner state, and that no state change happens inside an entry or [exit action](glossary.md#exit-action).

[^1]: Miro Samek, *Practical UML Statecharts in C/C++: Event-Driven Programming for Embedded Systems*, 2nd ed. (Newnes, 2009), §3.2, p. 105.
[^2]: Ibid., §3.3.2, p. 112.
[^3]: Ibid., §3.4.3, p. 122.
[^4]: Ibid., §3.5.2, p. 130.
[^5]: Ibid., §3.6.3, p. 142.
[^6]: Ibid., §3.8, p. 147.
[^7]: Ibid., §3.7.4, p. 146.
[^8]: Ibid., §3.6.1, p. 133.
[^9]: Ibid., §3.6.1, p. 137.
[^10]: Ibid., §4.5.3, p. 165.
[^11]: Ibid., §4.6.7, p. 190.
[^12]: Ibid., §4.5.8, p. 178.
[^13]: Ibid., §4.1, p. 150.
[^14]: Ibid., §4.7.1, p. 192.
[^15]: Ibid., §4.7.3, p. 193.
[^16]: Ibid., §4.7.5, p. 195.
[^17]: Ibid., §4.7.7, p. 196.
