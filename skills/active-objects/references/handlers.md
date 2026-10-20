# Handlers

## Run to completion

The implementation must:

- Handle one event per call and return. The dispatcher calls no other
  handler until this one returns.
- Wait by returning: start one of the object's own timers, or return and
  handle the producer's later event.
- Keep values that later events need in the object's private, persistent
  state, and use temporary values only for work within the current call.
- Represent a sequence in time with an explicit state variable that says
  which step comes next, and select the work with it.
- Copy any value it needs from the event during the call. The framework may
  reuse the event's storage once the handler returns.
- Ignore signals it does not use.
- Keep its work short. The longest handler adds to the delay of every
  higher-priority event.

The implementation must not:

- Wait for another event, or loop until a condition becomes true.
- Busy-wait, except for a bounded operation shorter than every deadline, such
  as one short conversion by a peripheral, including its failure path.
- Save a position inside a function: no coroutines, continuation macros,
  protothreads or private task stacks.
- Keep a reference to the event after the call.
- Call a handler directly. Only the dispatcher calls handlers.

Handlers never overlap, so they need no locks between them.

## Sequences

A sequence keeps its position in explicit state. In pseudo-code, a button
whose pins must settle before they are read:

    on each event:
        if phase is IDLE and the event is START or TIMEOUT:
            switch the pins to sensing
            phase = SENSING
            start own timer (settling time)
        else if phase is SENSING and the event is TIMEOUT:
            read and debounce the pins
            phase = IDLE
            start own timer (rest of the poll interval)

Every call starts at the top; `phase` says which step comes next. The handler
waits for the settling time by starting its timer and returning, not by
looping. Any other event leaves the sequence unchanged.

## Publishing state

An owner posts its state itself, not a hint to fetch it, at start and after
every change:

    on each event:
        before = mode
        update mode from the event
        if the event is START or mode differs from before:
            post the new mode to each receiver

The mode can be its own signal per value, or one signal whose data is the
mode; the message contract decides. Each receiver stores what it receives and
never calls back into the owner.

## Timers

- A timer belongs to one object and delivers a timeout event into that
  object's own queue.
- A timer is one-shot. Starting it again replaces the running one, and the
  handler restarts it for every further timeout.
- Intervals are nominal. Interrupts, the running handler and queued work
  delay a timeout's handling, so a restarted interval is not exact periodic
  execution.

## Startup

- Each owner configures the hardware it owns once, before the dispatcher
  runs.
- The dispatcher delivers a start event to every object, in priority order,
  before any queued event. An object begins its behaviour there.
- Peers receive initial state as messages, typically posted on the owner's
  start event.
