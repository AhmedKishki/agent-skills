# Active-object kernel

The kernel is three operations over fixed, statically allocated objects:
post an event, start the object's own timer, and run the dispatcher. The
examples are AVR C; the rules in SKILL.md do not depend on the core.

## Interface

```c
struct aoEvent {
	uint16_t signal;		/* an enum aoSignal */
	uint16_t word;			/* an agreed quantity, or 0 */
};

void aoPost(const struct ao *ao, enum aoSignal signal, uint16_t word);
void aoTimerStart(const struct ao *ao, uint16_t ms);	/* the caller's own object only */
void aoRun(const struct ao *const objects[], uint8_t objectCount);
```

- `aoPost()` copies the signal and the word into the destination queue and
  returns at once. It never calls the receiver and never waits for it. It
  keeps no pointer to the producer's storage, so messages need no heap and no
  transfer of ownership.
- `aoPost()` may run in a handler or an interrupt. `aoTimerStart()` and
  `aoRun()` run only in the foreground.
- Every internal event is one value of a single enum, which lists each
  signal with its producers, its consumers and its word. Two values belong
  to the kernel: a start signal, delivered once to every handler, and a
  timeout signal, posted by an object's own timer.

## An object in memory

Each object has a part that never changes and a part that changes all the
time:

- The descriptor, a `const` structure, holds the handler's address and the
  address of the queue. It can stay in flash.
- The queue and the timer live in RAM, in static storage that starts at
  zero: an empty queue and a stopped timer. Nothing has to initialise them.
- The handler is `static`, so other modules cannot name it. The dispatcher
  calls it through the descriptor.
- The module's behaviour state is separate `static` variables in the same
  file, not members of the descriptor.

Modules are singletons behind a common descriptor type: one object per owned
responsibility. Copying a descriptor does not create a second, independent
object: the copy shares the handler, the queue and the module's state.

Every handler matches `void (*)(const struct aoEvent *)` exactly. A
function-pointer cast is not an adapter: calling a function through an
incompatible type is undefined behaviour.

Peers may see only a destination handle. When the header defines the whole
descriptor and queue structures, C lets any includer reach the handler and
the queue. How to hide them (an opaque type, a kernel-private header) is a
design decision to agree. Until it is enforced, review enforces the rule.

## The queue

A queue is a ring of `AO_QUEUE_LENGTH` events with two counters: `head`, the
index of the oldest event, and `count`, the number waiting. A post writes to
`(head + count) % AO_QUEUE_LENGTH`; a take reads `head` and advances it.
Events come out in the order they went in.

Posting from an interrupt and from a handler is safe because the queue is
changed only with interrupts blocked, and the previous interrupt state is
restored afterwards:

```c
void aoPost(const struct ao *ao, enum aoSignal signal, uint16_t word) {
	struct aoQueue *queue = ao->queue;
	uint8_t sreg = SREG;			/* the interrupt state to restore */
	volatile struct aoEvent *slot;

	cli();
	if (queue->count < AO_QUEUE_LENGTH) {	/* full: the new event is dropped */
		slot = &queue->events[(queue->head + queue->count) % AO_QUEUE_LENGTH];
		slot->signal = signal;
		slot->word = word;
		queue->count++;
	}
	SREG = sreg;
}
```

- Restoring the saved `SREG` instead of calling `sei()` leaves interrupts as
  `aoPost()` found them, so the same function works inside an interrupt,
  where they are already blocked.
- The event slots, `head` and `count` are `volatile`, because interrupts
  write them. The timer fields are touched only by the foreground and need
  no protection.
- Calling a function from an interrupt makes the compiler save and restore
  more registers. Measure that cost against the interrupt's timing budget.

## The dispatcher

```text
 start: call every handler once with the start signal, directly, in list order
 forever:
   1. timers: for each due timer, stop it, then post its timeout
   2. pick:   the first object in the list whose queue holds an event
   3a. found: block interrupts, copy its oldest event, unblock;
              call its handler with the copy; go to 1
   3b. none:  block interrupts; if still no event and no tick since step 1,
              sleep atomically; unblock; go to 1
```

- Queued events wait until every start call has returned, so each object
  handles its start event first.
- After every event the scan starts again at the top of the list. A waiting
  higher-priority event therefore runs next, but never interrupts a running
  handler.
- Step 2 may read a one-byte `count` without blocking, because an 8-bit CPU
  reads a byte in one instruction. A wider counter needs blocking.
- A due timer is stopped before its timeout is posted. If the queue is full,
  that timeout is lost.

## Sleeping without missing an event

If an interrupt posts after the last check but before the sleep instruction,
the CPU sleeps with an event waiting. The check and the sleep must therefore
form one atomic step with respect to interrupts.

On AVR, the instruction after `sei` always runs before a pending interrupt:

```c
cli();				/* from the last check to the sleep, nothing may post */
if (aoReady(objects, objectCount) == NULL && getMs() == now) {
	sei();			/* the sleep runs before any waiting interrupt */
	sleep_cpu();
}
sei();
```

An interrupt that arrives after the check is held until the CPU sleeps and
then wakes it at once. Other cores need their own equivalent; on Cortex-M,
for example, `WFI` executed with interrupts masked still wakes on a pending
interrupt. The `getMs()` comparison makes the dispatcher loop instead of
sleeping when a tick has passed, because a timer may have become due.

Idle sleep keeps the peripherals running, so any interrupt, including the
periodic tick, wakes the CPU.

## Timers

An object's timer is a recorded start time and interval, checked against a
hardware tick counter; it is not a separate peripheral.

- `aoTimerStart(&buttonAo, 10)` records the current tick and 10. Starting
  again replaces the running timer.
- The dispatcher posts the timeout once `now - start >= interval`, with
  unsigned arithmetic, so a counter wrap-around does not matter.
- The timer is one-shot. The handler rearms it for each further timeout.

## Handler examples

A sequence in time keeps its position in an explicit static phase:

```c
enum phase { BUTTON_IDLING, BUTTON_SENSING };

static enum phase phase;	/* static: kept between events; starts at BUTTON_IDLING */

static void buttonHandler(const struct aoEvent *e) {
	switch (phase) {
	case BUTTON_IDLING:
		if (e->signal == AO_START_SIG || e->signal == AO_TIMEOUT_SIG) {
			buttonSenseBegin();
			phase = BUTTON_SENSING;
			aoTimerStart(&buttonAo, BTN_SETTLE_MS);
		}
		break;

	case BUTTON_SENSING:
		if (e->signal == AO_TIMEOUT_SIG) {
			buttonGesture(buttonDebounce(buttonSenseEnd()));
			phase = BUTTON_IDLING;
			aoTimerStart(&buttonAo, BTN_POLL_MS - BTN_SETTLE_MS);
		}
		break;
	}
}
```

- Every call starts at the top; `phase` says which step comes next. If
  `phase` were a local, every call would begin sensing and none would read
  the button.
- The handler waits for the settling time by starting its timer and
  returning, not by looping.
- Any other event matches neither check and leaves the poll unchanged.

An owner publishes its state with the data in the event, at start and after
every change, so each receiver keeps its own copy:

```c
static uint8_t mode;		/* the lamp's state: owned here, applied by pwm */

static void lampHandler(const struct aoEvent *e) {
	uint8_t before = mode;	/* a local: needed only during this call */

	if (e->signal == BUTTON_SINGLE_PRESS_SIG) {
		mode = lampNextMode(mode);
	} else if (e->signal == AMBIENT_DARK_SIG) {
		mode = lampForDark(mode);
	}
	if (e->signal == AO_START_SIG || mode != before) {
		aoPost(&pwmAo, LAMP_MODE_SIG, mode);	/* the state itself, not a hint to read it */
	}
}
```

The receiver stores the word in its own state. It never calls back into the
lamp module.

## Compared with an RTOS task

| Task mechanism | Active-object kernel |
|---|---|
| Separate stack, suspended call | Handlers share the foreground stack; static state records progress. |
| Delay the task | Start the timer, return, handle the timeout. |
| Block on a queue | Return; the dispatcher calls the handler with the next event. |
| Send to another task | `aoPost()` copies an event without waiting for the receiver. |
| Preemption by a higher-priority task | Priority picks the next handler; only interrupts preempt a running handler. |
| Locks between tasks | None between handlers; interrupt-shared data still needs protection. |
| Idle task | The dispatcher's sleep. |

A bounded busy wait inside a handler, such as one ADC conversion, also lets
several objects share a peripheral without a request queue: foreground calls
never overlap.
