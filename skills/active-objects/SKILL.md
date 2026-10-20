---
name: active-objects
description: >-
  Use when designing, writing, reviewing or refactoring event-driven embedded C
  firmware built from active objects: run-to-completion event handlers, each
  with a private event queue and a software timer, run by a dispatcher. Also
  use when a module is about to call, query, set or share another module's
  state, wait or block inside a handler, or do application work inside an
  interrupt.
---

# Active objects

An active object owns its state and its hardware and reacts to one event at
a time. Other code reaches it only by posting an event to its queue. Every
rule below protects one of three properties: each piece of state has one
owner, objects communicate only through queues, and a handler runs to
completion without waiting.

C allows accesses the pattern forbids: a header that defines a structure lets
any includer reach its members. If C allows an access, that does not make it
permitted. Existing code that breaks a rule is debt to migrate, not an
example to copy.

## The parts

| Part | What it is |
|---|---|
| Private state | `static` variables of the owning module, kept from one event to the next |
| Handler | `void handler(const struct aoEvent *e)`: called once per event, returns when that event is handled |
| Queue | the object's own FIFO of events; anyone may post to it, only the dispatcher takes from it |
| Timer | one one-shot software timer that posts a timeout event into the object's own queue |

An event is a signal, which names what happened, and one small data word,
which carries an agreed quantity or is 0. The kernel provides only posting,
the object's own timer and the dispatcher. The kernel interface, posting from
an interrupt, the dispatcher loop, safe sleeping and handler examples are in
[references/kernel.md](references/kernel.md); read it before writing or
reviewing kernel or handler code.

## Communication: queues only

The implementation must:

- Pass every piece of information between objects as an event, posted
  through the one messaging API (such as `aoPost()`) into the receiver's
  private queue.
- Make each message complete: its signal and data carry everything the
  receiver needs in order to act.
- Let a receiver keep its own copy of what it received. The producer remains
  the authority for that state.
- Agree each message before implementing it: its meaning, its signal and
  data, how the receiver gets the initial state, ordering and freshness, and
  what happens when the receiver's queue is full.

The implementation must not:

- Add getters or setters between objects. A read-only getter is still a
  bypass.
- Call another object's handler, read its variables, hand out pointers to its
  state, or alias that state through shared globals.
- Send a notification that sends the receiver back to the producer for the
  data ("the mode changed, read it with `modeGet()`").
- Replace getters with a central shared-state module. It is the same back
  door under a different name.
- Expose an object's handler, queue storage, queue counters, timer fields or
  private state to peers. A public handle names a destination and nothing
  else.
- Start, stop or inspect another object's timer.
- Choose a payload layout, retry, acknowledgement or coalescing policy
  without agreement.

Drivers, the clock and pure utilities that are not active objects need an
explicit boundary decision. Calling a function a driver or a utility does
not exempt it from these rules.

## State and events

- State is persistent. Its owner holds it and keeps applying it until it
  changes. Persistent does not mean stored in EEPROM.
- An event is transitory. It is consumed by its designated consumers, not
  necessarily by every object.
- A request is not proof of an applied state. The owner records a state when
  it has actually applied the change, and nothing reports a request as an
  applied result before then.
- A state change becomes an event only where a consumer needs it. Post an
  event only when a consumer acts on it.
- Model the states and events the current work needs, not every physical
  transition. A PWM duty cycle is state and a duty change is an event; the
  PWM edges are not events, because nothing consumes them.
- The signal names the event itself: `DOOR_OPENED_SIG` and `DOOR_CLOSED_SIG`
  are two events, not one signal with a 0/1 word. The word carries agreed
  data (a hold time, a sample) and is 0 otherwise.
- One enum lists every internal signal, each with its producers, its
  consumers and the meaning of its word. One event may go to several objects
  under the same signal, and one signal may have several producers.
- Internal events carry no wire protocol: no protocol tags, byte layouts or
  checksums. The protocol module converts at the border and takes part
  through ordinary events, not through a privileged path into other modules.

## Handlers: run to completion

The implementation must:

- Handle one event and return. The dispatcher calls no other handler until
  this one returns.
- Wait by returning: start the object's own timer, or return and handle the
  producer's later event.
- Keep values that later events need in the module's static storage.
- Represent a sequence in time with an explicit state variable, such as
  `static enum phase phase`, and select the work with it.
- Use ordinary local variables only for work within the current call.
- Copy any value it needs from the event. The event pointer is valid only
  during the call, because the dispatcher reuses that storage.
- Ignore signals it does not use.
- Keep its work short. The longest handler adds to the delay of every
  higher-priority event.

The implementation must not:

- Wait for another event, or loop until a condition becomes true.
- Busy-wait, except for a bounded operation shorter than every deadline
  (such as one ADC conversion), including its failure path.
- Save a position inside a function: no protothreads, continuation macros,
  coroutines, `setjmp` or private task stacks.
- Store the event pointer.
- Call a handler directly. Only the dispatcher calls handlers.

## Timers

- Each object has one one-shot timer, which posts a timeout event to that
  object's own queue.
- Starting the timer again replaces the running one. The handler rearms it
  for every further timeout.
- Intervals are nominal. Interrupts, the running handler and queued work
  delay the timeout's handling, so a rearmed interval is not exact periodic
  execution.

## Interrupts

The implementation must:

- In an interrupt, only capture data, set flags or post events. A handler
  does the work.
- Record any exception explicitly, with its reason. For example, a waveform
  interrupt may write its output pins because the waveform must not depend
  on how long a handler runs.
- Make posting safe from handlers and interrupts alike: save the interrupt
  state, block interrupts, change the queue and restore the saved state. A
  post never re-enables interrupts unconditionally.
- Declare queue slots and counters that interrupts write `volatile`, and take
  events out with interrupts blocked.
- Change a hardware register shared between modules with a single write that
  affects only the intended bits (set/clear registers), never with a
  read-modify-write that an interrupt can split.

Handlers never overlap, so they need no locks between them. Data shared with
an interrupt still needs `volatile` and interrupt-protected access.

## Ownership

- Every peripheral, pin and mutable variable has one owning module. The
  owner configures and drives it; others ask through messages.
- Pins stay with their owning modules; there is no central GPIO module,
  because only a pin's owner knows what its level means.
- A module that needs another owner's hardware in a certain state (for
  example, outputs dark during a measurement) synchronises with that owner
  through a signal. It never writes that hardware itself.
- A register that holds settings of several peripherals gets one explicit
  owner as soon as a second module needs it.
- Only the dispatcher puts the CPU to sleep, and it owns the sleep
  controller.

## Dispatcher, priority and startup

- The dispatcher takes the oldest event of the highest-priority object that
  has one and calls that object's handler. When no event waits and no timer
  is due, it sleeps. The last check and the sleep must be atomic with respect
  to interrupts, or a freshly posted event waits for some later interrupt.
- Priority decides which handler runs next, not which one interrupts another.
  The object list is ordered by deadline. Priority alone does not prove a
  deadline; the timing has to be measured.
- An idle object is not polled: after startup its handler runs only for an
  event.
- Boot runs once through owner initialisers, each configuring the hardware
  its module owns. `main()` then hands the objects to the dispatcher in
  priority order.
- The dispatcher delivers a start event to every handler, in list order,
  before any queued event.
- A peer receives its initial state as a message, typically posted by the
  owner on its start event. It never reads the owner's internals.
- The kernel stays minimal: queues, one timer per object and the dispatcher.
  It has no scheduling library and no wrappers, layers or extension
  mechanisms without a concrete need.

## Queue capacity

- Queues have a fixed size. Document what a post to a full queue does, for
  example that it silently drops the new event.
- Do not treat a silent drop as acceptable for state delivery. For each
  message, argue why the receiver's queue cannot be full, or agree a policy.
  An argument based on priority order (every receiver ranks above the
  producer, so their queues are empty when it posts) holds only while that
  order stays; record the dependency.
- A timeout lost to a full queue stops an activity that rearms only on its
  timeout. Account for it.
- Coalescing (keeping only the newest) is a receiver's choice, made in its
  own state. It is not a kernel feature.

## Red flags: stop and redesign

Each of these thoughts means the design is about to break a rule.

| Thought | Reality |
|---|---|
| "Just a small read-only getter." | It ties the reader to the owner's representation and timing and skips the queue's ordering. It is a bypass. |
| "The receiver can read the value when it is notified." | The receiver then acts on whatever the producer holds now, not on the event. Ordering and freshness become undefined. |
| "Put the shared state in a common module." | It is the same access through a different name. |
| "A short loop until the flag is set." | Only a bounded wait shorter than every deadline is allowed, failure path included. Otherwise, start the timer and return. |
| "The interrupt already has the data; it can do the work." | Interrupts capture and post. Work inside them lengthens every interrupt's latency and breaks run-to-completion reasoning. |
| "Calling the handler directly is simpler." | Only the dispatcher calls handlers; a direct call runs one handler inside another. |
| "The header exposes the struct, so I can use its members." | C allows accesses the pattern forbids. Visibility is not permission. |
| "Pick a payload or a retry now; change it later." | Message contracts are agreed before they are implemented. |
| "Post it anyway; someone might need it." | An event exists only for a consumer that acts on it. |
| "The existing code already does it." | Existing bypasses are migration debt, not a pattern. |

## Adding or changing an active object

1. Name the interaction's producer, consumer, the state involved and the
   events.
2. Agree each message: meaning, signal and data, initial-state delivery,
   ordering and freshness, full-queue behaviour.
3. Add each new signal to the enum with its producers, consumers and word.
4. Keep the state `static` and private; export only the destination handle.
5. Write the handler: one event per call, an explicit phase for sequences,
   the own timer for delays, then return.
6. Let interrupts only capture data and post.
7. Initialise the owned hardware in the owner's initialiser; begin the
   behaviour on the start event; deliver initial peer state by message.
8. Place the object in the priority list by deadline, and check the longest
   handler against the deadlines of every higher-priority object.
