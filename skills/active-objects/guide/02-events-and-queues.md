# 2. Events and queues

[Active objects](glossary.md#active-object) exchange nothing but events, so the book spends a good part of chapter 6 on what an event is, how it reaches its receiver and where its memory lives (sections 6.4 and 6.5). Sections 6.7.6 and 9.4 add how big the queues must be, and chapter 5 adds two ways of changing the order of events.

## An event is a signal with parameters

An event is ‘an occurrence in time and space that has significance to the system’ (section 2.2.6). Strictly, the UML word *event* names the kind of occurrence. Each concrete occurrence is an *event instance*. An instance can carry *parameters* with quantitative information, such as the scan code of a keystroke.

An event instance has a life cycle of three stages. The instance is *received* when it is placed in a queue, *dispatched* when the state machine starts to process it as the *current event*, and *consumed* when the processing ends. A consumed event is gone.

In code, an event is one object with two parts (section 3.2.1). The *signal* is an integer that names the kind of occurrence, such as UP, DOWN or TICK. The parameters follow in the same structure. In Samek's C framework an event with parameters is a structure that begins with the plain event structure, so every event can travel as a pointer to that common part.

### Signals of the right size

‘Nothing affects state machine complexity and efficiency as much as the right granularity and semantics of events’ (section 4.7.8). Signals are too fine when groups of them are always handled alike. The calculator of chapter 2 handles the digits 1 to 9 identically, so it uses one signal for all of them. Signals are too coarse when handlers keep testing a parameter to find out what happened, as Windows programs do with the WM_COMMAND message. In that case the parameter values are the real signals. The cure is to remap the signals before they reach the state machine. Section 2.4.2 applies the same remedy: the calculator turns the PLUS, MINUS, MULTIPLY and DIVIDE buttons into one OPER signal, which saves repeating four triggers on every transition that accepts an operator.

## Two ways to deliver an event

Any code can produce events: interrupts, device drivers, legacy code outside the framework. Only [active objects](glossary.md#active-object) consume them, because only active objects have queues (section 6.4). Frameworks offer two delivery mechanisms, and they can coexist in one application.

| | Direct posting | [Publish-subscribe](glossary.md#publish-subscribe) |
|---|---|---|
| How | The producer posts the event straight into the receiver's queue. | The producer publishes the event to the framework, which delivers it to every object that subscribed to its signal. |
| Coupling | Strong. The producer must know the receiver and which events it wants. | Loose. Producers and consumers need not know each other. |
| Conditions | The framework offers a thread-safe post operation. | The signals are known to all, mean the same to all, and the framework keeps the subscriber lists, which can change at run time. |
| Fits | A group of objects, or an object and an interrupt, that together provide one service. | Events that many parts of the system care about. |

A framework can also provide *raw* thread-safe queues with no active object behind them. Such a queue never blocks and carries events from the task level to an interrupt (section 6.4).

## Event memory

An event's memory must not be reused before every object has finished the RTC step that processes it (section 6.5). Overwriting the current event in the middle of a step breaks [run to completion](glossary.md#run-to-completion) and is ‘one of the hardest bugs to resolve’. Section 4.7.10 gives the classic case: an interrupt writes a new event into the memory that the main loop is still reading.

### Copying whole events

The plain solution copies each event into the queue and out again (section 6.5.1). Copying is safe and costly. Every queue slot and every buffer must hold the largest event, each event is copied at least twice, and the queue is locked during the copies. Sending only a pointer to a large buffer through a message queue saves the copying but brings back a shared buffer, which the producer may overwrite before the consumer has read it.

### Zero-copy delivery

A framework can do better than an RTOS because, through [inversion of control](glossary.md#inversion-of-control), it controls the whole life of an event (section 6.5.2):

1. The producer asks the framework for a new event, which comes from an [event pool](glossary.md#event-pool).
2. The producer fills in the parameters and posts a pointer to the event.
3. The receiver reads the event through the pointer during its RTC step.
4. When the step is over, the framework *garbage-collects* the event and returns it to its pool.

The event is never copied, and the framework makes sure it is never recycled too early. Events whose content never changes, such as a clock tick, can be allocated once as *static* events, which the framework recognises and never recycles.

### Many receivers: reference counting

A published event can go to several objects at once. All of them receive a pointer to the same event, and a *reference counter* inside the event decides when it can be recycled (section 6.5.4). Each insertion into a queue increments the counter. Each garbage collection at the end of an RTC step decrements it. The event returns to its pool when the counter reaches zero. The counter falls only after the processing, because an event is in use for the whole RTC step and not only while it waits in the queue.

### Who may touch an event

Section 6.5.6 sets ownership rules for dynamic events. The producer owns a new event, with permission to write, from its allocation until it posts or publishes the event. After that the producer must not touch it. A producer that changes its mind must hand the event back to the garbage collector. The receiving object owns the current event read-only, and only for the duration of the RTC step.

### Pools in place of the heap

Dynamic events could come from `malloc()` and `free()`, but the heap is a poor fit for real-time systems (section 6.5.7). It fragments, it wastes memory on block headers, its timing is often nondeterministic, and its functions are often not reentrant. Frameworks use pools of fixed-size blocks.

### Small systems copy

Very small microcontrollers have no room for pools. The book's version for them, QP-nano, allows only events with one scalar parameter of up to four bytes: ‘Small, fixed-size events are simply copied by value into and out of event queues in an inherently thread-safe manner’ (section 12.1). Copying removes the need for pools and for [reference counting](glossary.md#reference-counting).

## Queues: guaranteed delivery and their size

A function call is assumed to work. Section 6.7.6 argues that posting an event deserves the same trust, and that the trust rests on queues and pools of adequate size, just as the trust in function calls rests on an adequate stack. Samek concludes that ‘[event pools](glossary.md#event-pool) and event queues should be treated on equal footing as the execution stacks’. Running out of either is an error, and his framework stops with an [assertion](glossary.md#assertion) when a queue overflows. RTOS message queues offer ways around the guarantee, such as losing an event when the queue is full or blocking the sender until there is room. Section 9.4.1 calls both ‘an abuse of event queues’.

### How big a queue must be

A queue works only while events, on average, are consumed at least as fast as they are produced (section 9.4.1). Bursts of production are fine if they are short and far enough apart for the queue to drain. Two methods give the size:

- **Measurement.** Run the system under load, then read the lowest number of free slots each queue reached. Samek's queue keeps this low-water mark for that purpose.
- **Analysis.** The deeper a queue must be, the lower its object's priority. The highest-priority object handles every event from other objects at once, so its queue only has to hold events from interrupts. For lower priorities, a queue must hold everything that higher-priority objects and interrupts can post to it during its object's longest RTC step, preemptions included. Several events posted in one RTC step add to the need.

The book's advice is to start with oversized queues and pools and to shrink them near the end of development, because every change in timing or event traffic can invalidate the numbers. It also notes that ‘it is safest to start [active objects](glossary.md#active-object) in the order of their priority, beginning from the lowest-priority active objects because they tend to have the biggest event queues’.

## Changing the order of events

### Deferring an event

Sometimes an event arrives when the object cannot handle it yet, such as a new transaction request while the previous transaction is still in progress (section 5.3). Ignoring the request may be wrong, and handling two transactions at once makes the state machine much harder. The object therefore *defers* the request and *recalls* it later.

UML statecharts define deferral as a list of [deferred events](glossary.md#deferred-event) in each state, which nesting makes expensive. The book's *Deferred Event* pattern does the same work explicitly:

1. A high-level state traps the early event, often in an [internal transition](glossary.md#internal-transition), and defers it into a separate queue.
2. The state that can handle the event recalls it in its [entry action](glossary.md#entry-action).
3. The recall posts the event to the object's own queue with the LIFO policy, so it is the next event processed and no other event can change the state first (section 7.5.4).
4. The object handles the recalled event like any other event, in a normal transition.

The recalled event is never processed inside the entry action, even though the recall makes it available there.

### Posting to self, FIFO or LIFO

An object can also post an event to itself, which the *[Reminder](glossary.md#reminder)* pattern uses (see [State patterns](05-state-patterns.md)). A reminder posted FIFO goes to the back of the queue, so events that arrived meanwhile are handled first. That suits long work cut into steps. A reminder posted LIFO is guaranteed to be the next event, which suits a sequence that must not be interrupted. Samek warns that LIFO changes the order of events and reverses the order of several LIFO posts (section 5.2.5).

## In the skill

The skill's rules on events, messages and queues are in `references/objects-and-messages.md`. Copying versus pooled events is decision D3, direct posting versus [publish-subscribe](glossary.md#publish-subscribe) is D4, and the size of every queue, deferral store and pool is D6. A full queue is a bug, as in section 6.7.6, and decision D12 sets what the product does if one fills anyway. Deferral and recall are in `references/state-machines.md`.
