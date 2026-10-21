# Timers

These rules cover timers as objects use them. `kernel.md` covers how the
kernel implements them.

## Rules

- A timer only posts a timeout into its own object's queue. No application
  code runs in the timer's context.
- An object starts and stops only its own timers, and only from its own
  handler. The timer interface leaves no way to name another object's timer.
- D7 (`decisions.md`) sets how many timers an object has and whether any
  of them repeat.
- Restarting a timer replaces the running one. The handler restarts a
  one-shot timer for each further timeout.
- Timeouts are approximate. Interrupts, the running handler and queued
  events all delay them.
- A timer starts partway through a tick, so its first tick can be almost
  zero long. To wait at least N full ticks, set N + 1. The tick period is
  D14.
- Each timer belongs to one state. Stop it when that state is left, normally
  in the state's exit action. With one timer per object, two nested states
  never both use it.
- A lost timeout stops anything that restarts only on that timeout. Take
  this into account in D5.

## Late timeouts (D8)

A timeout may already be in the queue when its timer is stopped or
restarted. When it arrives, it looks like a current one, and the object
reacts to something that no longer applies. Every object with a timer
needs a way to recognise late timeouts. Put these options to the user:

- **A count in the timeout.** Increment a count at every start, pass it as
  the timeout's data, and handle a timeout only when its data matches the
  current count. This works on every kernel, including RTOS timers whose
  stop takes effect later. The button example in `state-machines.md` uses
  this method.
- **A stop that reports.** The stop tells the caller whether the timeout was
  already posted, and the object then skips exactly one timeout. This needs
  support from the kernel and a stop that takes effect at once.
- **A kernel that removes it.** On stop, the kernel deletes any queued
  timeout for that timer. Every stop then costs a search of the queue.

A separate signal per timer distinguishes one timer from another. It cannot
distinguish an old timeout from a new one of the same timer.
