# Handlers, interrupts and other contexts

## Handlers run to completion

A handler that waits holds up every event queued behind it, and anything it read before waiting may be out of date when it resumes.

- Handle one event and return. To wait, start the object's timer, or return and handle the next event when it arrives.
- Never block. Every RTOS call in a handler uses a zero timeout, which rules out a delay, a semaphore or mutex take, and any receive that waits. A loop that waits for a flag or a register blocks too.
- Many driver and stack calls block. Use their asynchronous or callback forms, and post the completion as an event.
- A short busy-wait with a fixed bound, such as one ADC conversion, is allowed only if it is shorter than every deadline, including its failure path. Record it with the decisions.
- Never save a position inside the function. Protothreads, `switch`-based coroutine macros, `setjmp`/`longjmp` and private stacks all do this. The object's state records its progress.
- Keep values that later events need in the object's state. Use local variables only within the current call.
- Never keep a pointer to the event. To keep an event for later, defer it (`state-machines.md`).
- Never call a handler directly, including the object's own. Only the kernel calls handlers. To continue later, post to the object's own queue or start its timer.
- Keep handlers short. The longest handler sets how fast the system can respond, and its worst-case time is measured under D2 (`decisions.md`).
- Check before changing anything, so that a handler never leaves its object half-changed. Expected problems become states or events. Real errors are handled as decided in D12.

## Interrupts, callbacks and other threads

These rules apply to every context outside an object's handler: interrupt handlers, RTOS timer callbacks, library callbacks such as a BLE stack's, and any other thread.

- Code in these contexts does short, bounded work on data it owns, such as filtering a reading or deciding whether anything changed, and then posts. Work that is long, or that needs an object's state, goes to that object's handler. Its worst-case time delays every handler and every lower interrupt, so it counts against every deadline (D2).
- An interrupt that drives a resource an object owns needs an approved exception with a recorded reason. For example, a waveform interrupt may set the object's output pins, because the waveform cannot wait for a handler.
- Posting must be safe from every context that posts. Code that disables interrupts saves the interrupt state first and restores it afterwards. It never simply re-enables interrupts, because the caller may have had them disabled. On an RTOS, an interrupt posts through the RTOS's interrupt-safe call.
- An interrupt that posts runs at a level that the kernel's critical sections mask (D15).
- Data shared between an interrupt and its own object's handler is `volatile`, and the handler accesses it with interrupts disabled. Between threads, pass data by posting, and where posting is impossible, use C11 atomics. `volatile` on its own does not synchronise threads.
- When an object's handler and its own interrupt both touch a hardware register, change the register in one of two ways: with one write that affects only the intended bits, as a set/clear register allows, or with a read-modify-write done with interrupts disabled. An interrupt must never be able to split the change.
