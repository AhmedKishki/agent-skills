---
name: active-objects
description: >-
  Use when designing, writing or reviewing embedded C built from active
  objects (modules that own their data, take work only as events from their
  own queue and handle one event at a time with a state machine) on any
  kernel or RTOS, or when drawing their statecharts and network diagram in
  PlantUML. Also use when code is about to read or change another module's
  data, wait inside a handler, add a flag in place of a state, or do long
  work in an interrupt or callback.
---

# Active objects

An active object is a module that owns its data and the hardware it drives. Other code reaches it only by posting an event to its queue. The object takes its events one at a time, finishes each one before starting the next, and keeps track of where it is with a state machine. None of this depends on the kernel underneath.

## Contracts and decisions

Every design detail is either a contract or a decision. In the reference modules, a rule is a contract unless it names a decision by its number, D1 to D16.

A **contract** is intransitive: it holds in every project and on every kernel. Enforce contracts in all code you write or review, kernel code included. When code breaks a contract, name the contract, say what goes wrong because of the break and propose a fix. Build nothing on top of a break. A contract can be set aside only when the user explicitly approves an exception and gives a reason. Record the exception and mark it in the code.

A **decision** is transitive: it belongs to the project, and the user makes it. Before any code depends on a decision, put the question to the user with the options, what each option gains and costs, and the default if there is one. Wait for a clear yes, then record the answer where the user wants it.

Ask whenever something is unclear. If C allows an access, that does not make it permitted. Existing code that breaks a contract is debt to pay off. Never copy it as an example.

## Three properties

Every contract protects one of three properties.

1. **One owner.** Each piece of data and each resource belongs to exactly one object.
2. **Queues only.** Objects communicate only by posting events, so every posted event must arrive.
3. **Run to completion.** A handler deals with one event fully and returns without waiting.

## Never

- Read, write, call or share another object's internals. That rules out getters, setters, shared modules and globals that alias an object's data.
- Block or wait in a handler, or save a position inside it.
- Rely on a full queue to drop or delay an event. A full queue, store or pool is a bug, like a stack overflow: size each one so it never fills.
- Do long work in an interrupt, a callback or another thread, or let it touch an object's data. It works briefly on its own data and posts the result.
- Use a flag where the object needs a state.
- Start, stop or inspect another object's timer.
- Call a handler from anywhere except the kernel.
- Make a project decision on the user's behalf.

## Where to go

Read the module for the task before writing or reviewing code. When a task touches several areas, read each module it touches.

| Task | Module |
|---|---|
| Settling a project choice: kernel, priorities, event types, delivery, sizes, timers, state-machine coding, boundaries, errors, hiding, ticks and sleep, interrupt levels, diagrams | `references/decisions.md` |
| Designing objects, events, signals, the messages between objects, or who owns which resource | `references/objects-and-messages.md` |
| Writing a handler, or code that runs in an interrupt, a callback or another thread | `references/handlers.md` |
| Designing or coding an object's behaviour: states, transitions, guards, entry and exit actions, nesting, deferred events | `references/state-machines.md` |
| Using timers, or handling a timeout that may be late | `references/timers.md` |
| Writing, reviewing or adapting the kernel: queues, posting, the dispatcher, idle, the RTOS adaptation, start-up and shutdown | `references/kernel.md` |
| Drawing an object's statechart or the network of objects in PlantUML, or checking a diagram against the code | `references/diagrams.md` |
| Finishing or reviewing any change | `references/review.md` |
