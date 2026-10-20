---
name: active-objects
description: >-
  Use when designing, writing, reviewing or refactoring event-driven software
  built from active objects: objects that each own private state and a private
  event queue and handle one event at a time under a dispatcher. Also use when
  a module is about to call, query, set or share another module's state, wait
  or block inside an event handler, or do application work inside an
  interrupt.
---

# Active objects

An active object owns its state and its resources and reacts to one event at
a time. Other code reaches it only by posting an event to its queue. Every
rule in this skill protects one of three properties:

1. **One owner.** Each piece of state and each resource belongs to exactly
   one object.
2. **Queues only.** Objects communicate only by posting events into each
   other's queues.
3. **Run to completion.** A handler processes one event and returns; it never
   waits.

The rules say what a code base must do to follow the pattern, not how to lay
it out: sizes, types, names and data layouts are the code base's own
decisions. A language that lets code reach another object's members does not
make that access permitted. Existing code that breaks a rule is debt to
remove, not an example to copy.

## The parts

| Part | What the pattern requires |
|---|---|
| State | Private to its object and kept from one event to the next. |
| Handler | Called once per event; returns when that event is handled. |
| Queue | The object's own; anyone may post to it, only the dispatcher takes from it. |
| Timers | Belong to the object and deliver timeout events into its own queue. |
| Dispatcher | Picks the next event, calls its object's handler, and sleeps when no work is left. |

An event is a signal, which names what happened, together with exactly the
data that signal is agreed to carry. The framework copies and delivers events
without interpreting their data, and provides nothing beyond posting, the
queues, timers and the dispatcher.

## Rules by topic

| Read | Covers | When |
|---|---|---|
| [Messaging](references/messaging.md) | Queue-only communication, state and events, message contracts, full queues | Before adding or changing any interaction between objects |
| [Handlers](references/handlers.md) | Run to completion, waiting, sequences, publishing state, timers, startup | Before writing or reviewing a handler |
| [Interrupts and ownership](references/interrupts-and-ownership.md) | Work in interrupts, data shared with them, owned hardware | When an interrupt, a register or a shared resource is involved |
| [Framework](references/framework.md) | What posting, queues, the dispatcher, timers and sleep must guarantee | Before writing or reviewing the framework itself |

## Red flags: stop and redesign

| Thought | Reality |
|---|---|
| "Just a small read-only getter." | It ties the reader to the owner's representation and timing and skips the queue's ordering. It is a bypass. |
| "The receiver can fetch the value when it is notified." | The receiver then acts on whatever the producer holds now, not on the event. Ordering and freshness become undefined. |
| "Put the shared state in a common module." | It is the same access under a different name. |
| "A short loop until the flag is set." | Only a bounded wait shorter than every deadline is allowed. Otherwise, start a timer and return. |
| "The interrupt already has the data; it can do the work." | Interrupts capture and post. Work inside them delays every other interrupt and breaks run-to-completion reasoning. |
| "Calling the handler directly is simpler." | Only the dispatcher calls handlers; a direct call runs one handler inside another. |
| "The structure is visible, so I can use its members." | Visibility is not permission. |
| "Pick a payload or a retry now; change it later." | Message contracts are agreed before they are implemented. |
| "Post it anyway; someone might need it." | An event exists only for a consumer that acts on it. |
| "The existing code already does it." | Existing bypasses are debt to remove, not a pattern. |

## Adding or changing an active object

1. Name the interaction's producer, consumer, the state involved and the
   events.
2. Agree each message: meaning, signal and data, initial-state delivery,
   ordering and freshness, full-queue behaviour.
3. Add each new signal to the central list with its producers, consumers and
   data.
4. Keep the state private; expose only a handle that names the destination.
5. Write the handler: one event per call, explicit state for sequences, the
   object's own timers for delays, then return.
6. Let interrupts only capture data and post.
7. Configure owned hardware in its owner; begin the behaviour on the start
   event; deliver initial peer state by message.
8. Place the object in the priority order by deadline, and check the longest
   handler against the deadlines of every higher-priority object.
