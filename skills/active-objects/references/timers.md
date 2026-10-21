# Timers

Read this when an object uses a timer, or when a timeout might arrive late.
Everything here is a contract unless a decision (D-number) is named; see
`decisions.md`. How the kernel implements timers is in `kernel.md`.

## Contracts

- A timer only posts a timeout into its own object's queue. No application
  code runs in the timer's context.
- An object starts and stops only its own timers, and only from its own
  handler. The timer interface makes other objects' timers unreachable.
- How many timers an object has, and whether any repeat, is D7.
- Restarting replaces the running timer. A one-shot timer is restarted by
  the handler for each further timeout.
- Times are approximate: interrupts, the running handler and queued events
  delay the timeout.
- A timer starts partway through a tick, so its first tick can be almost
  zero long. To wait at least N full ticks, set N + 1. The tick period is
  D14.
- Each timer belongs to one state and is stopped when that state is left,
  normally in its exit action. With one timer per object, nested states
  never both use it.
- A lost timeout stops anything that restarts only on its timeout. Account
  for it in D5.

## Late timeouts (D8)

A timeout can already be in the queue when its timer is stopped or
restarted. When it arrives, it looks like a fresh one, and the object reacts
to something that no longer applies. Every object with a timer needs a way
to recognise this. Put the options to the user:

- **A count in the timeout.** Increment the count at every start, pass it
  as the timeout's data, and handle a timeout only if the data matches the
  current count. This works on every kernel, including RTOS timers whose
  stop is not immediate. `state-machines.md` shows it in the button example.
- **A stop that reports.** The stop tells the caller whether the timeout was
  already posted; the object then skips exactly one timeout. This needs
  kernel support and a stop that takes effect at once.
- **A kernel that removes it.** On stop, the kernel deletes any queued
  timeout for that timer. This costs a queue search on every stop.

A separate signal per timer tells timers apart, but not an old timeout from
a new one of the same timer.
