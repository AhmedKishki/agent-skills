# 2. Events and queues

[Active objects](glossary.md#active-object) exchange nothing but events. The exchange is reliable only when the events, their delivery, their memory and the size of the queues are designed together.

## An event is a signal with parameters

An event is an occurrence in time and space that has significance to the system.[^1] Strictly, the word names the kind of occurrence, and each concrete occurrence is an *event instance*, which can carry *parameters* with quantitative information, such as the scan code of a keystroke.

An event instance passes through three stages. The instance is *received* when it is placed in a queue, *dispatched* when the state machine starts to process it as the *current event*, and *consumed* when the processing ends.[^2]

In code, an event is one object with two parts: the *signal*, an integer that names the kind of occurrence, and the parameters.[^3] An event with parameters is a structure that begins with the plain event structure, so every event can travel as a pointer to that common part.

### Signals of the right size

The granularity of signals affects the complexity and efficiency of a state machine more than anything else. Signals are too fine when groups of them are always handled alike, as the digits 1 to 9 are in a calculator, which therefore uses one signal for all of them. Signals are too coarse when handlers keep testing a parameter to find out what happened, as Windows programs do with the WM_COMMAND message, whose parameter values are the real signals. The cure is to remap the signals before they reach the state machine.[^4] A calculator, for example, turns its PLUS, MINUS, MULTIPLY and DIVIDE buttons into one OPER signal, which saves repeating four triggers on every transition that accepts an operator.

## Two ways to deliver an event

Any code can produce events, including interrupts, device drivers and code outside the framework, but only [active objects](glossary.md#active-object) consume them, because only active objects have queues.[^5] The two delivery mechanisms can coexist in one application.

| | Direct posting | [Publish-subscribe](glossary.md#publish-subscribe) |
|---|---|---|
| How | The producer posts the event straight into the receiver's queue.[^6] | The producer publishes the event to the framework, which delivers it to every object that subscribed to its signal.[^7] |
| Coupling | Strong: the producer must know the receiver and which events it wants. | Loose: producers and consumers need not know each other. |
| Conditions | A thread-safe post operation in the framework. | Signals known to all and meaning the same to all, and subscriber lists that can change at run time. |
| Fits | A group of objects, or an object and an interrupt, that together provide one service. | Events that many parts of the system care about. |

A *raw* thread-safe queue, with no active object behind it, never blocks and carries events from the task level to an interrupt.[^8]

## Event memory

An event's memory must not be reused before every object has finished processing it. Overwriting the current event in the middle of an RTC step breaks [run to completion](glossary.md#run-to-completion) and is one of the hardest bugs to find.[^9] A typical case is an interrupt that writes a new event into the memory that the main loop is still reading.

### Copying whole events

Copying each event into the queue and out again is safe and costly. Every queue slot and every buffer must hold the largest event, each event is copied at least twice, and the queue is locked during the copies.[^10] Sending only a pointer to a large buffer through a message queue saves the copies but brings back a shared buffer, which the producer may overwrite before the consumer has read it.

### Zero-copy delivery

A framework controls the whole life of an event, so it can avoid copying altogether:

1. The producer gets a new event from an [event pool](glossary.md#event-pool) through the framework.
2. The producer fills in the parameters and posts a pointer to the event.
3. The receiver reads the event through the pointer during its RTC step.
4. When the step is over, the framework *garbage-collects* the event and returns it to its pool.[^11]

The framework makes sure that an event is never recycled too early. Events whose content never changes, such as a clock tick, can be allocated once as *static* events, which the framework recognises and never recycles.

### Many receivers

A published event can go to several objects at once. All of them receive a pointer to the same event, and a *reference counter* in the event decides when it can be recycled.[^12] Each insertion into a queue increments the counter, and each garbage collection at the end of an RTC step decrements it. The event returns to its pool when the counter reaches zero. The counter falls only after the processing, because an event is in use for the whole RTC step and not only while it waits in a queue.

### Who may touch an event

The producer owns a new event, with permission to write, from its allocation until it posts or publishes the event, and must not touch it afterwards. A producer that decides not to post an event hands it back to the garbage collector. The receiving object owns the current event read-only, and only for the duration of its RTC step.[^13]

### Pools in place of the heap

A heap is a poor source of events in a real-time system. It fragments, it wastes memory on block headers, its timing is often nondeterministic, and its functions are often not reentrant.[^14] Frameworks therefore allocate events from pools of fixed-size blocks.

### Small systems copy

Microcontrollers with very little RAM have no room for pools. Restricting events to one scalar parameter of up to four bytes lets them be copied by value into and out of the queues, which removes the need for pools and for [reference counting](glossary.md#reference-counting).[^15]

## Queues: guaranteed delivery and their size

A function call is trusted to work, and that trust rests on an adequate stack. Posting an event deserves the same trust, which rests on queues and pools of adequate size. Running out of either is therefore an error of the same kind as a stack overflow.[^16] A framework can detect it with an [assertion](glossary.md#assertion) that every queue accepts every posted event. RTOS message queues offer ways around the guarantee, such as losing an event when the queue is full or blocking the sender until there is room. Both are an abuse of event queues, because they destroy the guarantee of delivery.[^17]

### How big a queue must be

A queue works only while events are, on average, consumed at least as fast as they are produced. Bursts are fine if they are short and far enough apart for the queue to drain. Two methods give the size:

- **Measurement.** Run the system under its heaviest load, then read the lowest number of free slots each queue reached, its low-water mark.
- **Analysis.** The lower an object's priority, the deeper its queue must be. The highest-priority object handles every event from other objects at once, so its queue only has to hold events from interrupts. A lower-priority queue must hold everything that higher-priority objects and interrupts can post to it during its object's longest RTC step, preemptions included, and several events posted in one RTC step add to the need.[^18]

Queues and pools are best oversized early and shrunk near the end of development, because every change in timing or event traffic can invalidate the numbers.[^19] Starting the [active objects](glossary.md#active-object) in order of priority, lowest first, is generally safest, because the low-priority objects tend to have the biggest queues.[^20]

## Changing the order of events

### Deferring an event

An event sometimes arrives when the object cannot handle it yet, such as a new transaction request while the previous transaction is still in progress. Ignoring the request may be wrong, and handling two transactions at once makes the state machine much harder. The object therefore *defers* the request and *recalls* it later.

UML defines deferral as a list of [deferred events](glossary.md#deferred-event) in each state, which nesting makes expensive. The Deferred Event pattern does the same work explicitly:

1. A high-level state traps the early event, often in an [internal transition](glossary.md#internal-transition), and defers it into a separate queue.
2. The state that can handle the event recalls it in its [entry action](glossary.md#entry-action).
3. The recall posts the event to the object's own queue with the LIFO policy, so it is the next event processed and no other event can change the state first.[^21]
4. The object handles the recalled event like any other, in a normal transition, never inside the entry action.

### Posting to self, FIFO or LIFO

An object can also post an event to itself, which the [Reminder](glossary.md#reminder) pattern uses (see [State patterns](05-state-patterns.md)). A reminder posted FIFO goes to the back of the queue, so events that arrived meanwhile are handled first, which suits long work cut into steps. A reminder posted LIFO is guaranteed to be the next event, which suits a sequence that must not be interrupted. LIFO changes the order of events, and several LIFO posts in a row reverse it.[^22]

## In the skill

The skill's rules on events, messages and queues are in `references/objects-and-messages.md`. Copying versus pooled events is decision D3, direct posting versus [publish-subscribe](glossary.md#publish-subscribe) is D4, and the size of every queue, deferral store and pool is D6. A full queue is a bug, and decision D12 sets what the product does if one fills anyway. Deferral and recall are in `references/state-machines.md`.

[^1]: Miro Samek, *Practical UML Statecharts in C/C++: Event-Driven Programming for Embedded Systems*, 2nd ed. (Newnes, 2009), §2.2.6, p. 66.
[^2]: Ibid., §2.2.6, p. 67.
[^3]: Ibid., §3.2.1, p. 106.
[^4]: Ibid., §4.7.8, p. 197.
[^5]: Ibid., §6.4, p. 279.
[^6]: Ibid., §6.4.1, p. 280.
[^7]: Ibid., §6.4.2, p. 282.
[^8]: Ibid., §6.4, p. 279.
[^9]: Ibid., §6.5, p. 282.
[^10]: Ibid., §6.5.1, p. 283.
[^11]: Ibid., §6.5.2, p. 285.
[^12]: Ibid., §6.5.4, p. 286.
[^13]: Ibid., §6.5.6, p. 288.
[^14]: Ibid., §6.5.7, p. 289.
[^15]: Ibid., §12.1, p. 613.
[^16]: Ibid., §6.7.6, p. 302.
[^17]: Ibid., §9.4.1, p. 477.
[^18]: Ibid., §9.4.1, p. 478.
[^19]: Ibid., §9.4, p. 476.
[^20]: Ibid., §9.4.1, p. 479.
[^21]: Ibid., §7.5.4, p. 342.
[^22]: Ibid., §5.2.5, p. 218.
