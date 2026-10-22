# Glossary

## A

### Action
Code that a state machine executes in response to an event: changing a variable, performing input or output, calling a function, posting an event or changing state.

### Active object
An object with its own thread of control, its own event queue and a state machine, which communicates with other objects only by exchanging events asynchronously. The UML defines it as ‘an object having its own thread of control’.[^1]

### Assertion
A run-time check of a condition that only a bug can make false. A failed assertion calls one application-defined function, which in an embedded system typically makes the system safe and resets it. See Design by contract.

### Asynchronous preemption
In a preemptive run-to-completion kernel, the case where an interrupt posts an event to a task of higher priority than the interrupted one, so that the kernel starts that task when the interrupt ends.

## B

### Behavioural inheritance
The relation between a substate and its superstates: a substate inherits the behaviour of its superstates and defines only its differences. The relation is *is in*, as class inheritance is *is a*.[^2]

## C

### Choice pseudostate
A diagram node that splits a transition into several paths, chosen by guards that may depend on the results of actions taken earlier in the same run-to-completion step.

### Composite state
A state that contains other states. A state without inner states is a leaf state.

### Critical section
A stretch of code that executes with interrupts locked, so that no interrupt can change shared data in the middle of it. A framework protects its queues and timers with critical sections.

## D

### Deferred event
An event that a state cannot handle yet and keeps for later. A UML state can list the events it defers, and the Deferred Event pattern defers and recalls them explicitly.

### Design by contract
Bertrand Meyer's method of specifying the mutual obligations of software components as contracts, embedded in the code as assertions and checked at run time.[^3]

### Direct event posting
Delivery of an event straight into the queue of a named receiver, which the producer must know. See Publish-subscribe.

### Dispatch
To hand one event to a state machine for processing. `dispatch()` processes one event in one run-to-completion step.

## E

### Entry action
Code that runs every time a state is entered, whichever transition enters it, which guarantees the state's initialisation.

### Event
An occurrence in time and space that has significance to the system. In code, an event is a signal plus optional parameters.

### Event parameter
Quantitative information that an event carries, such as the scan code of a keystroke.

### Event pool
A pool of fixed-size memory blocks from which dynamic events are allocated and to which they return after use.

### Event processor
The generic code that executes state machines: it calls the state-handler functions, follows the hierarchy and executes the exit and entry actions of each transition. The QP framework's processor is called QEP.

### Exceptional condition
A rare situation that can legitimately arise during the life of a system and needs a recovery strategy, as opposed to an error, which is a bug.[^4]

### Exit action
Code that runs every time a state is left, whichever transition leaves it, which guarantees the state's cleanup. See Entry action.

### Extended state variable
A variable that a state machine keeps besides its state, for the quantitative aspects of its history, such as a counter.

### External transition
A transition between a state and one of its own substates that leaves the outer state and enters it again. See Local transition.

## F

### Finite state machine
A model of behaviour as a limited number of states, with transitions between them triggered by events.

### Framework
Software that calls the application's code, as opposed to a toolkit that the application calls. Inversion of control makes event-driven infrastructures frameworks.

## G

### Guard
A Boolean condition on extended state variables and event parameters that enables or disables a transition.

## H

### Hierarchical state machine
A state machine whose states can contain other states, also called a statechart.

### History pseudostate
A diagram node that stands for the most recently active substate of a composite state (shallow history) or for its whole most recent configuration (deep history).

## I

### Idle condition
The situation in which all event queues are empty. The vanilla kernel then performs idle processing, typically a low-power sleep.

### Initial transition
The transition that a state machine, or a composite state, takes into its first inner state. The transition has no trigger and no guard.

### Internal transition
A reaction to an event that executes actions without leaving the state, so no exit or entry action runs.

### Inversion of control
The arrangement in which the infrastructure calls the application when an event arrives, so that control resides in the infrastructure.[^5]

## L

### Leaf state
A state with no inner states.

### Least common ancestor
The innermost state that contains both the source and the target of a transition. A transition exits states up to it and enters states down from it.

### Liskov Substitution Principle for states
The rule that a substate must stay consistent with its superstate, so that reasoning at the superstate's level remains valid.[^6]

### Local transition
A transition between a state and one of its own substates that stays inside the outer state, without leaving or re-entering it. The QEP processor supports only local transitions.[^7]

## O

### Orthogonal Component
A state pattern that replaces orthogonal regions with component state machines owned by a container object.[^8]

### Orthogonal region
An independent part of a composite state. All regions of a state are active at once.

## P

### Priority-ceiling mutex
A lock that, while held, prevents preemption by tasks up to a set priority, the ceiling, and is immune to priority inversion. The QK kernel offers one for resources that must be shared.[^9]

### Pseudostate
A transient node in a state diagram, such as an initial pseudostate, a choice, a junction or a history node.

### Publish-subscribe
Delivery of an event, through the framework, to every object that subscribed to its signal. Producers and consumers need not know each other.

## Q

### QK
A preemptive run-to-completion kernel. Its tasks are one-shot functions that share one stack, scheduled by priority like nested interrupts.[^10]

## R

### Reference counting
Counting the queues that hold a dynamic event, so that the event returns to its pool only after the last receiver has finished with it.

### Reminder
A state pattern that invents an event and posts it to the object itself, for example to split long processing into short steps.[^11]

### Run to completion
The rule that a state machine finishes processing one event before it starts the next. The processing of one event is a *run-to-completion step*, or *RTC step*.[^12]

## S

### Self-transition
A transition whose source and target are the same state. The state is left and entered again, so its exit and entry actions run.

### Signal
The part of an event that names the kind of occurrence, an integer such as UP, DOWN or TICK.

### State
A chunk of behaviour in which the response to an event depends only on the event, a compact record of the relevant part of the system's history.

### State configuration
The set of states that are active at one moment in a hierarchical state machine, a tree from the top state down to the active leaf states.

### State-handler function
A function that implements one state. It receives every event in that state, including the reserved entry, exit and initial-transition signals, and returns whether it handled the event, ignored it, took a transition or passes it to its superstate.

### State table
A two-dimensional table, indexed by state and signal, that holds the actions and next states of a state machine.

### Static event
An event without changing parameters, allocated once and never recycled.

### Substate
A state nested inside another state.

### Superstate
A state that contains other states.

### Synchronous preemption
In a preemptive run-to-completion kernel, the case where a task posts an event to a task of higher priority, which the kernel starts at once.

### System clock tick
The periodic interrupt that drives the time events, typically between 10 Hz and 100 Hz.

## T

### Task-level response
The delay between making a high-priority task ready to run and actually starting it.[^13]

### Time event
An event that a framework posts to an active object at a set time. The object arms it, may disarm it, and handles it like any other event.

### Top state
The implicit outermost state that contains every other state of a UML state machine. In the QEP processor it ignores every event and is never the target of a transition.

### Transition
A change from one state to another, caused by a triggering event.

## U

### Ultimate Hook
The pattern of passing every event first to the specific code and letting unhandled events flow back to a generic layer. In state machines it becomes state nesting.[^14]

## V

### Vanilla kernel
A cooperative kernel: one loop that dispatches one event at a time from the highest-priority non-empty queue, with no per-task stacks.[^15]

## Z

### Zero-copy event delivery
Event delivery in which queues hold only pointers to events allocated from pools, and the framework recycles each event after use.[^16]

[^1]: Miro Samek, *Practical UML Statecharts in C/C++: Event-Driven Programming for Embedded Systems*, 2nd ed. (Newnes, 2009), §6.3, p. 266.
[^2]: Ibid., §2.3.3, p. 72.
[^3]: Ibid., §6.7.1, p. 294.
[^4]: Ibid., §6.7.2, p. 296.
[^5]: Ibid., §6.1, p. 256.
[^6]: Ibid., §2.3.4, p. 73.
[^7]: Ibid., §2.3.9, p. 81.
[^8]: Ibid., §5.4.3, p. 231.
[^9]: Ibid., §10.4.1, p. 515.
[^10]: Ibid., §6.3.8, p. 276.
[^11]: Ibid., §5.2.1, p. 211.
[^12]: Ibid., §2.2.8, p. 68.
[^13]: Ibid., §6.2.2, p. 261.
[^14]: Ibid., §5.1.1, p. 205.
[^15]: Ibid., §6.3.7, p. 275.
[^16]: Ibid., §6.5.2, p. 285.
