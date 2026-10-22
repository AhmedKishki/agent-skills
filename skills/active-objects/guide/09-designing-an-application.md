# 9. Designing an application

Chapter 9 walks through the design of a complete application in six steps. The example is Edsger Dijkstra's Dining Philosophers Problem (DPP), which Samek uses to test every port of his framework (section 9.2). Five philosophers sit at a round table with a fork between each pair, and a philosopher needs both neighbouring forks to eat. The problem is a small model of tasks that compete for shared resources.

## Step 1: Requirements

The design starts from what the application must do, which for a small application is the problem specification (section 9.2.1). A philosopher alternates between thinking and eating. To eat, a philosopher has to acquire the two forks beside it, eats for a while, then puts them down and thinks again. Each fork can be used by only one philosopher at a time.

## Step 2: Sequence diagrams

Sequence diagrams of the main scenarios come next (section 9.2.2). Drawing them forces a split into [active objects](glossary.md#active-object), chosen to keep the coupling between objects low: no shared resources, and as few and as small events as possible.

The forks are the shared resource of the problem. The general strategy for shared resources in an active object system is to encapsulate them in a dedicated object that manages them for the rest of the system. The forks therefore belong to a *Table* object, and the philosophers ask the Table for permission to eat. A typical scenario reads:

1. A philosopher starts in *thinking* and arms a one-shot timer on entry.
2. When the timeout arrives, the philosopher becomes *hungry* and posts HUNGRY, with its number as the parameter, to the Table.
3. The Table finds both forks free and publishes EAT with the philosopher's number.
4. The philosopher enters *eating* and arms its timer again.
5. A neighbour gets hungry meanwhile, and the Table, whose forks are now partly in use, grants nothing. The neighbour stays *hungry*.
6. When eating ends, the philosopher publishes DONE on its way out of *eating*.
7. The Table returns the forks, finds the hungry neighbour and lets it eat.

## Step 3: Signals, events and active objects

The sequence diagrams reveal the events, and ‘The choice of signals and [event parameters](glossary.md#event-parameter) is perhaps the most important design decision in any event-driven system’ (section 9.2.3). The signals in turn shape the events and the state machines.

- All signals of a small application go into one enumeration, which keeps them unique. User signals start after the reserved signals of the [event processor](glossary.md#event-processor).
- The published signals (EAT, DONE, TERMINATE) come first, followed by the directly posted ones (HUNGRY). The philosophers post HUNGRY straight to the Table, so the application shows both delivery mechanisms.
- An event with parameters, such as the philosopher's number, is a structure that begins with the plain event.
- Each [active object](glossary.md#active-object) lives in its own C file. Its structure and its state handlers stay private there, and the rest of the application sees only a constructor and an opaque pointer, enough to post to the object and nothing more.

## Step 4: State machines

‘In fact, your main job in developing your QP application consists of elaborating the state machines of your [active objects](glossary.md#active-object)’ (section 9.2.4). A philosopher's life cycle is three states: *thinking*, *hungry* and *eating*. The philosopher posts HUNGRY in the [entry action](glossary.md#entry-action) of *hungry* and publishes DONE in the [exit action](glossary.md#exit-action) of *eating*, because these events mean exactly entering hunger and leaving the meal. Generating them on the TIMEOUT transitions would not keep that meaning safe from later changes to the machine. Hence the guideline: ‘Favor entry and exit actions over actions on transitions.’

The Table's state machine is almost trivial. It keeps track of the forks and the hungry philosophers in [extended state variables](glossary.md#extended-state-variable), and a diagram of its single state adds little to its code.

## Step 5: Initialising and starting

Starting each [active object](glossary.md#active-object) forces several decisions (section 9.2.5): its priority, the size of its event queue, which depends on the priority (see [Events and queues](02-events-and-queues.md)), a private stack in some ports, and the order in which the objects start. The start order matters under an RTOS, where a new thread may start running at once and post to an object that does not exist yet. Locking the scheduler until all objects have started avoids that.

The start-up sequence in `main()` is the same for every port: the objects' constructors, the board, the framework, the [publish-subscribe](glossary.md#publish-subscribe) lists, the [event pools](glossary.md#event-pool) in order of increasing block size, the active objects, and finally the framework's loop, which may never return.

## Step 6: Terminating

Embedded programs seldom terminate, since they usually run until the power goes (section 9.2.6). The fail-safe reaction to a CPU exception or a failed [assertion](glossary.md#assertion) is a catastrophic shutdown, perhaps followed by a reset, and needs its own design and testing (see [Errors](08-errors.md)). A graceful shutdown matters on a general-purpose operating system. DPP publishes a TERMINATE event, every object that must clean up subscribes to it, and the last subscriber stops the framework. An [active object](glossary.md#active-object) can also stop itself, but only after it has released its resources, unsubscribed from all signals and made sure that nothing posts to it any more.

## Devices belong to one active object

Device drivers fit the event-driven model too: a driver can post or publish events like any other code (section 9.4.3). Samek recommends treating every device as a shared resource and restricting its access to one [active object](glossary.md#active-object). [Run to completion](glossary.md#run-to-completion) inside that object then makes even non-reentrant driver code safe, and no mutual blocking between objects can cause priority inversion. One active object may encapsulate several devices.

## In the skill

The skill's rules on ownership follow the same strategy: each resource has one owning object, which serves the others' requests as events (`references/objects-and-messages.md`). Each object lives in its own `.c` file, and peers see only an incomplete type they can post to (decision D13). Decision D2 sets the priorities and the start order, and D6 the queue sizes. `references/diagrams.md` asks for one statechart per object and a network diagram of all objects and their events, in the spirit of the sequence diagrams of step 2.
