# Framework

The framework provides posting, one queue per object, timers and the
dispatcher, and nothing else. It owns no application state and carries event
data without interpreting it. No scheduling library, wrapper or extension
mechanism is added without a concrete need.

## Posting

- Posting copies the event into the destination's queue and returns at once.
  It never calls the receiver and never waits for it.
- The copy keeps no reference to the producer's storage, so the producer may
  reuse that storage at once and messages need no dynamic allocation.
- Posting works from handlers and from interrupts; see
  [interrupts and ownership](interrupts-and-ownership.md).
- Posting does not prove delivery: a full queue may drop the event.

## Queues

- Each object has its own first-in, first-out queue. Events come out in the
  order they went in.
- Every queue is bounded, and posting to a full queue has one defined,
  documented behaviour.
- Only the dispatcher takes events out, and it does so without interference
  from interrupts that may be posting.

## The dispatcher

    deliver the start event to every object directly, in priority order
    forever:
        turn every due timer into a timeout event in its object's queue
        if some queue holds an event:
            take the oldest event of the highest-priority such object
            call that object's handler with it
        else:
            sleep until an interrupt, without missing one (below)

- Queued events wait until every start delivery has returned, so each object
  handles its start event first.
- After every event the choice starts again from the highest priority. A
  waiting higher-priority event runs next but never interrupts a running
  handler: priority decides which handler runs next, not which one preempts.
- An idle object is not polled. After startup its handler runs only for an
  event.
- Order the objects by deadline. Priority alone does not prove a deadline:
  the longest handler, interrupt service and queued work all add delay, so
  measure the timing.

## Sleeping without missing an event

If an interrupt posts after the last check for work but before the processor
sleeps, the event waits until some later interrupt wakes the processor. The
last check and entering sleep must therefore form one step with respect to
interrupts: hold interrupts off for the check, then enter sleep through the
processor's mechanism that lets a pending interrupt end the sleep at once.
The same check must notice a timer that has become due.

## Timers

- A timer is a recorded start and interval, measured against a time base. It
  needs no peripheral of its own.
- The dispatcher posts a timer's timeout once its interval has elapsed and
  stops the timer, so a timeout fires once per start.
- A timeout posted into a full queue is lost like any other event.

## Compared with an RTOS task

| Task mechanism | Active-object framework |
|---|---|
| Separate stack, suspended call | Handlers share one stack; explicit state records progress. |
| Delay the task | Start a timer, return, handle the timeout. |
| Block on a queue | Return; the dispatcher calls the handler with the next event. |
| Send to another task | Posting copies an event without waiting for the receiver. |
| Preemption by a higher-priority task | Priority picks the next handler; only interrupts preempt a running one. |
| Locks between tasks | None between handlers; data shared with interrupts still needs protection. |
| Idle task | The dispatcher's sleep. |

A bounded wait inside a handler, such as one short peripheral conversion,
also lets several objects share that peripheral without a request queue,
because handlers never overlap.
