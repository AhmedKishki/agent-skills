---
name: active-objects
description: >-
  Use when designing, writing or reviewing embedded C built from active
  objects: modules that own their data, receive work only as events in their
  own queue, and handle one event at a time with a state machine. Covers the
  objects, events, signals, queues, handlers, state machines, timers,
  interrupts and the kernel beneath them, whether a cooperative kernel
  written for the project or RTOS threads on FreeRTOS or Zephyr. Enforces
  the pattern's contracts and puts every project decision to the user for
  approval. Also use when code is about to read or change another module's
  data, wait inside a handler, add a flag instead of a state, or do real work
  in an interrupt or callback.
---

# Active objects

An active object is a module that owns its data and the hardware it drives.
It has its own queue of events and handles them one at a time, start to
finish, using a state machine to remember where it is. Other code reaches it
only by posting an event to its queue. The pattern does not depend on the
kernel underneath.

## How to work

Every design detail is one of two kinds.

- **Contract** (intransitive): holds in every project and on every kernel.
  Enforce it in everything you write or review, kernel code included. When
  code breaks one, say which, what goes wrong and how to fix it; don't build
  on the break. Set one aside only when the user explicitly approves an
  exception for a stated reason, and record and mark it.
- **Decision** (transitive): chosen per project. Before code relies on one,
  put it to the user with its options, trade-offs and default (if it has
  one), and wait for a clear yes. Never choose for the user. Record approved
  decisions where the user says.

When anything is unclear, ask. If C lets code reach something, that does not
make the access allowed. Existing code that breaks a contract is debt, not a
precedent.

## The three promises

Every contract protects one of these.

1. **One owner.** Each piece of data and each resource belongs to one object.
2. **Queues only.** Objects talk only by posting events.
3. **Run to completion.** A handler deals with one event fully and returns
   without waiting.

## Never

- Read, write, call or share another object's internals: no getters,
  setters, shared modules or aliasing globals.
- Block or wait in a handler, or save a position inside it.
- Do more than capture data and post in an interrupt, callback or foreign
  thread.
- Let a flag stand in for a state.
- Start, stop or inspect another object's timer.
- Call a handler from anywhere but the kernel.
- Pick a project decision yourself.

## Where to go

Read the module that matches the task before writing or reviewing code.
Read several when the task spans them.

| Task | Read |
|---|---|
| Settling any project choice: kernel, priorities, event data, delivery, full queues, sizes, timers, state-machine coding, boundaries, errors, hiding, ticks and sleep, interrupt levels | `references/decisions.md` |
| Designing objects, events, signals, messages between objects, or who owns which resource | `references/objects-and-messages.md` |
| Writing a handler, or code in an interrupt, callback or other thread | `references/handlers.md` |
| Designing or coding an object's behaviour: states, transitions, guards, entry and exit, nesting, deferring | `references/state-machines.md` |
| Using timers, or dealing with late timeouts | `references/timers.md` |
| Writing or reviewing the kernel: queues, posting, the dispatcher, idle, the RTOS adaptation, start-up and shutdown | `references/kernel.md` |
| Finishing or reviewing any change | `references/review.md` |
