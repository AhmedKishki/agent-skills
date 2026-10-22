# Glossary

## A

### Action
Code that a state machine executes in response to an event: changing a variable, performing input or output, calling a function, posting an event or changing state (section 2.2.7).

### Active object
An object with its own thread of control, its own event queue and a state machine, which communicates with other objects only by exchanging events asynchronously. The UML defines it as ‘an object having its own thread of control’ (section 6.3).

### Assertion
A run-time check of a condition that only a bug can make false. A failed assertion calls one application-defined function, which in an embedded system typically makes the system safe and resets it (section 6.7.3). See Design by contract.

### Asynchronous preemption
In a preemptive run-to-completion kernel, the case where an interrupt posts an event to a task of higher priority than the interrupted one, so the kernel starts that task when the interrupt ends (section 10.2.3).

## B

### Behavioural inheritance
Samek's name for the relation between a substate and its superstates: a substate inherits the behaviour of its superstates and defines only its differences. The relation is *is in*, as class inheritance is *is a* (section 2.3.3).

## C

### Choice pseudostate
A diagram node that splits a transition into several paths, chosen by guards that may depend on the results of actions taken earlier in the same run-to-completion step (section 2.3.12).

### Composite state
A state that contains other states. A state without inner states is a leaf state (section 2.3.2).

### Critical section
A stretch of code that runs with interrupts locked, so that no interrupt can change shared data in the middle of it. A framework protects its queues and timers with critical sections (section 7.3).

## D

### Deferred event
An event that a state cannot handle yet and keeps for later. UML states can list events they defer. Samek's Deferred Event pattern defers and recalls them explicitly (sections 2.3.11 and 5.3).

### Design by contract
Bertrand Meyer's method of specifying the mutual obligations of software components as contracts, embedded in the code as assertions and checked at run time (section 6.7.1).

### Direct event posting
Delivery of an event straight into the queue of a named receiver. The producer must know the receiver (section 6.4.1). See Publish-subscribe.

### Dispatch
To hand one event to a state machine for processing. In the book's interface, `dispatch()` processes one event in one run-to-completion step (section 3.2).

## E

### Entry action
Code that runs every time a state is entered, whichever transition enters it. Entry and exit actions ‘provide means for guaranteed initialization and cleanup’ (section 2.3.6).

### Event
‘an occurrence in time and space that has significance to the system’ (section 2.2.6). In code, an event is a signal plus optional parameters.

### Event parameter
Quantitative information that an event carries, such as the scan code of a keystroke (section 2.2.6).

### Event pool
A pool of fixed-size memory blocks from which dynamic events are allocated and to which they return after use (section 6.5.7).

### Event processor
The generic code that executes state machines: it calls the state-handler functions, follows the hierarchy and runs the exit and entry actions of each transition. The book's processor is called QEP (chapter 4).

### Exceptional condition
A rare situation that can legitimately arise during the life of a system and needs a recovery strategy. Samek distinguishes it from an error, which is a bug (section 6.7.2).

### Exit action
Code that runs every time a state is left, whichever transition leaves it (section 2.3.6). See Entry action.

### Extended state variable
A variable that a state machine keeps besides its state, for the quantitative aspects of its history, such as a counter (section 2.2.4).

### External transition
A transition between a state and one of its own substates that leaves the outer state and enters it again (section 2.3.9). See Local transition.

## F

### Finite state machine
A model of behaviour as a limited number of states, with transitions between them triggered by events (section 2.2).

### Framework
Software that calls the application's code, as opposed to a toolkit that the application calls. Inversion of control makes event-driven infrastructures frameworks (section 6.1).

## G

### Guard
A Boolean condition on extended state variables and event parameters that enables or disables a transition (section 2.2.5).

## H

### Hierarchical state machine
A state machine whose states can contain other states, also called a statechart (section 2.3.2).

### History pseudostate
A diagram node that stands for the most recently active substate of a composite state (shallow history) or its whole most recent configuration (deep history) (section 2.3.12).

## I

### Idle condition
The situation in which all event queues are empty. The vanilla kernel then performs idle processing, typically a low-power sleep (section 6.3.7).

### Initial transition
The transition that a state machine, or a composite state, takes into its first inner state. The transition has no trigger and no guard (section 2.3.12).

### Internal transition
A reaction to an event that executes actions without leaving the state, so no exit or entry action runs (section 2.3.7).

### Inversion of control
The arrangement in which the infrastructure calls the application when an event arrives, so control resides in the infrastructure (section 6.1).

## L

### Leaf state
A state with no inner states (section 2.3.2).

### Least common ancestor
The innermost state that contains both the source and the target of a transition. A transition exits states up to it and enters states down from it (section 2.3.8).

### Liskov Substitution Principle for states
The rule that a substate must stay consistent with its superstate, so that reasoning at the superstate's level remains valid (section 2.3.4).

### Local transition
A transition between a state and one of its own substates that stays inside the outer state, without leaving or re-entering it. Samek's processor supports only local transitions (section 2.3.9).

## O

### Orthogonal Component
Samek's state pattern that replaces orthogonal regions with component state machines owned by a container object (section 5.4).

### Orthogonal region
An independent part of a composite state. All regions of a state are active at once (section 2.3.5).

## P

### Priority-ceiling mutex
A lock that, while held, prevents preemption by tasks up to a set priority, the ceiling, and is immune to priority inversion. Samek's preemptive kernel offers one for resources that must be shared (section 10.4.1).

### Pseudostate
A transient node in a state diagram, such as an initial pseudostate, a choice, a junction or a history node (section 2.3.12).

### Publish-subscribe
Delivery of an event to every object that subscribed to its signal, through the framework. Producers and consumers need not know each other (section 6.4.2).

## Q

### QK
Samek's preemptive run-to-completion kernel. Its tasks are one-shot functions that share one stack, scheduled by priority like nested interrupts (chapter 10).

## R

### Reference counting
Counting the queues that hold a dynamic event, so that the event returns to its pool only after the last receiver has finished with it (section 6.5.4).

### Reminder
Samek's state pattern of inventing an event and posting it to the object itself, for example to split long processing into short steps (section 5.2).

### Run to completion
The rule that a state machine finishes processing one event before it starts the next. The processing of one event is a *run-to-completion step*, or *RTC step* (section 2.2.8).

## S

### Self-transition
A transition whose source and target are the same state. The state is left and entered again, so its exit and entry actions run (section 2.3.7).

### Signal
The part of an event that names the kind of occurrence, an integer such as UP, DOWN or TICK (section 3.2.1).

### State
A chunk of behaviour in which the response to an event depends only on the event. ‘A state captures the relevant aspects of the system’s history very efficiently’ (section 2.2.1).

### State configuration
The set of states that are active at one moment in a hierarchical state machine, a tree from the top state down to the active leaf states (section 2.3.8).

### State-handler function
A function that implements one state. It receives every event in that state, including the reserved entry, exit and initial-transition signals, and returns whether it handled the event, ignored it, took a transition or passes it to its superstate (sections 3.6 and 4.4).

### State table
A two-dimensional table, indexed by state and signal, that holds the actions and next states of a state machine (section 3.4).

### Static event
An event without changing parameters, allocated once and never recycled (section 6.5.3).

### Substate
A state nested inside another state (section 2.3.2).

### Superstate
A state that contains other states (section 2.3.2).

### Synchronous preemption
In a preemptive run-to-completion kernel, the case where a task posts an event to a task of higher priority, which the kernel starts at once (section 10.2.3).

### System clock tick
The periodic interrupt that drives the time events, usually between 10 Hz and 100 Hz (section 6.6.2).

## T

### Task-level response
The delay between making a high-priority task ready to run and actually starting it (section 6.2.2).

### Time event
An event that a framework posts to an active object at a set time. The object arms it, may disarm it, and handles it like any other event (section 6.6.1).

### Top state
The implicit outermost state that contains every other state of a UML state machine. In Samek's processor it ignores every event and is never the target of a transition (sections 2.3.2 and 4.5.3).

### Transition
A change from one state to another, caused by a triggering event (section 2.2.7).

## U

### Ultimate Hook
The pattern of passing every event first to the specific code and letting unhandled events flow back to a generic layer. In state machines it becomes state nesting (sections 2.3.1 and 5.1).

## V

### Vanilla kernel
Samek's cooperative kernel: one loop that dispatches one event at a time from the highest-priority non-empty queue, with no per-task stacks (section 6.3.7).

## Z

### Zero-copy event delivery
Event delivery in which queues hold only pointers to events allocated from pools, and the framework recycles each event after use (section 6.5.2).
