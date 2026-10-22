# The kernel

The rules below hold on any kernel, whether it is new or an existing one
being adapted (D1). The kernel follows the same rules as the objects. It
never blocks on a handler's behalf, never shares an object's data and gives
objects no way to reach each other.

## What every kernel must do

1. The kernel is the only code that calls handlers, and it never runs one
   object's handler twice at the same time.
2. Each object handles its start event before any other event sent to it.
3. An object receives its events one at a time, in the order they were
   posted. A recalled event is the only exception and goes to the front.
4. A post copies the event, or passes a pooled one (D3), and returns at
   once. It never blocks, never calls the receiver, keeps no pointer into
   the sender's data and works from every context that posts. A full queue
   is a bug, like a stack overflow: the post reports it with `AO_ERROR()`
   (D12) and, if that returns, drops the new event.
5. A timer only posts a timeout into its own object's queue, and an object
   can name only its own timers.
6. Idle never misses an event that arrives just before the CPU or the thread
   goes idle.
7. The kernel protects its queues, timers and pools against every context
   that touches them, on every core that runs objects or posts.
8. The kernel calls a handler only when an event is waiting for it, and
   never polls an idle object.
9. Priority (D2) decides which object runs next. On RTOS threads, priority
   also lets a higher-priority object preempt a lower one. Priority alone
   does not show that a deadline is met, so measure the handler times
   against the deadlines.
10. Only the kernel decides when the CPU sleeps. On an RTOS, the idle thread
    makes that decision.
11. The kernel offers posting, timers and recall, and nothing that lets one
    object reach another. It adds no layers or wrappers without a real
    need.

## Start-up and shutdown

- If the CPU starts with interrupts enabled, `main()` masks them before
  doing anything else.
- Every queue, and every event pool, exists before anything can post to it.
- Each owner's set-up runs once and configures only what that owner owns.
- Each object handles its start event before any other event. Peers receive
  their starting values as messages from the owner, usually sent on the
  owner's start event.
- An interrupt that posts is enabled only once every queue it posts to
  exists. In practice, each owner enables its own interrupts on its start
  event. On a cooperative kernel, the CPU's interrupts are unmasked after
  every start event has run.
- The start order is approved as part of D2.
- An object that can stop first makes sure that nothing posts to it any
  more, then releases what it owns.

## Interface

Objects use only the kernel's interface, never the port or RTOS headers, so
changing the kernel leaves the objects as they are. The names below are the
ones the examples use; each project chooses its own names and types (D3,
D6, D14).

| Name | Contract |
|---|---|
| `ao_post(to, sig, data)` | Any context. Copies the event and returns at once, as rule 4 says. |
| `ao_timer_start(ticks, data)`, `ao_timer_stop()` | Handler only. They act on the running object's own timer. Start stops the timer first, then sets its data; `ticks` is at least 1, and the timeout carries `data` back. |
| `ao_recall(e)` | Handler only, at most once per handler call. Copies a deferred event to the front of the running object's queue. A full queue is reported as in `ao_post()`. |
| `AO_ERROR()` | Reports a bug where it happened. A development build stops; D12 decides whether a production build returns, and the code after the call is the fallback. |
| `AO_SIG_START`, `AO_SIG_TIMEOUT` | The kernel's own signals: the start event, delivered once before any other, and a timeout from the object's timer, one signal per timer when D7 allows several. |
| `AO_SIG_ENTRY`, `AO_SIG_EXIT`, `AO_SIG_INIT`, `AO_SIG_EMPTY` | Reserved for the state machines and never posted. The application's signals follow them. |
| `ao_event_t`, `ao_t` | A signal and its data (D3); a handle that peers see as an incomplete type, so they can post to it and nothing more (D13). |

Every handler matches the handler type exactly. In C, a call through a
mismatched function pointer is undefined behaviour, and a cast does not
make it safe.

## Cooperative kernel

One loop runs on one stack. No handler interrupts another, and only
interrupts can interrupt a handler. Priority decides which handler runs
next, so check every object's longest handler against the deadlines of all
higher-priority objects.

```text
for each object, highest priority first:
    call its handler with AO_SIG_START        (queued events wait)
unmask the CPU's interrupts                   (they start last)
repeat forever:
    for each running timer that is due:
        stop it, then post AO_SIG_TIMEOUT with its data
    pick the highest-priority object with an event waiting
    if there is one:
        take its oldest event inside a critical section
        call its handler with that copy
    else:
        enter a critical section
        if still no event waiting and no timer due:
            sleep until an interrupt is pending
        leave the critical section             (a pending interrupt runs here)
    start the scan again from the top
```

Equal priorities are allowed only if D2 says how ties are broken.

- A critical section saves the interrupt state and restores exactly that
  state, never a plain "enable", because the caller may have had interrupts
  masked.
- Idle sleeps inside the critical section, so an interrupt that is pending,
  or becomes pending, wakes the CPU at once. A core that wakes only with
  interrupts enabled needs its documented enable-and-sleep sequence, which
  leaves no gap between enabling and sleeping. Something must wake the CPU
  when a timer falls due: the periodic tick, or a hardware timer set for
  the next due timer (D14).
- A recall runs inside a critical section and first checks for room,
  because an interrupt may have filled the queue in the meantime.
- A queue's count is read outside a critical section only where the target
  reads it in one indivisible access.
- A timer is due when `(ao_tick_t)(now - start) >= ticks`. Unsigned
  subtraction makes counter wrap-around harmless.
- Only handlers and the loop touch the timer fields. They never run at the
  same time, so the fields need no critical section.
- A post from an interrupt costs a function call and a critical section.
  Measure that cost against the interrupt's time budget.

## RTOS threads

- Each object is one thread, and the thread waits in exactly one place: the
  receive on its own queue.
- Each thread's stack size is part of D6.

## Measuring handler time

D2 needs each handler's worst-case time, measured on the target. Read a
cycle counter before and after the handler, or toggle a spare pin around it
and watch the pin with a logic analyser. Record the worst case seen under
the heaviest load.
