# 10. A reference kernel in C

The skill's `references/kernel.md` states what any kernel must do. This
guide shows one way to meet those rules in C: the layers, a full interface,
the port of a cooperative kernel, its ring queue, and RTOS threads on
FreeRTOS and Zephyr. Every project chooses its own names and types.

## Layers

```text
objects (one .c file each)      include ao.h, and ao_object.h for themselves
ao.h, ao_object.h               the interface below
kernel core                     queues, timers, dispatching
port  or  RTOS adaptation       critical sections, idle, ticks / RTOS calls
```

Objects never include the port or RTOS headers for kernel purposes. Moving
from the cooperative kernel to RTOS threads changes the kernel core and the
adaptation layer, and leaves the objects as they are.

## Interface sketch

The types belong to the project. A small `ao_types.h`, written for each
project, defines them:

| Type | What it is | Decided in |
|---|---|---|
| `ao_signal_t` | wide enough for every signal in the project | D3 |
| `ao_data_t` | the data an event carries, either a single value or a fixed payload struct | D3 |
| `ao_tick_t` | an unsigned tick count that wraps around | D14 |
| `ao_qindex_t` | holds the largest queue size, and the target reads it in one indivisible access | D6 |
| `ao_prio_t` | holds the highest priority | D2 |

Every module may include `ao.h`:

```c
/* ao.h */
#ifndef AO_H
#define AO_H

#include "ao_types.h"            /* the project's types (D3, D6, D14, D2) */

typedef struct ao ao_t;          /* incomplete here: peers can only post */

enum {
    AO_SIG_START = 0,            /* delivered once, before any other event */
    AO_SIG_TIMEOUT,              /* posted by the object's own timer */
    AO_SIG_ENTRY,                /* state machines only, never posted: */
    AO_SIG_EXIT,                 /*   entry and exit actions, */
    AO_SIG_INIT,                 /*   initial transitions (nesting), */
    AO_SIG_EMPTY,                /*   asking a state for its outer state */
    AO_SIG_FIRST_USER            /* the application's signals start here */
};

typedef struct {
    ao_signal_t sig;
    ao_data_t   data;            /* the type chosen in D3 */
} ao_event_t;

/* Any context. Copies the event and returns at once. Never blocks and
 * never calls the receiver. A full queue is a bug: AO_ERROR() reports it
 * (D12), and if that returns, the new event is dropped. */
void ao_post(ao_t *to, ao_signal_t sig, ao_data_t data);

/* Reports a bug where it happened, such as a full queue. A development
 * build stops here; D12 decides whether a production build returns. The
 * code after the call is the fallback for when it does. */
#define AO_ERROR() ao_on_error(__FILE__, __LINE__)
void ao_on_error(const char *file, int line);

#endif
```

Only object modules and the kernel include `ao_object.h`. Peers include
`ao.h` alone, where `ao_t` is incomplete, so they cannot reach its fields
(D13):

```c
/* ao_object.h */
#ifndef AO_OBJECT_H
#define AO_OBJECT_H

#include "ao.h"

typedef void (*ao_handler_t)(const ao_event_t *e);

/* Fixed for the object's whole life, so it can live in read-only memory.
 * The RTOS form adds the thread's stack and its static RTOS objects. */
typedef struct {
    ao_handler_t handler;
    ao_event_t  *queue;          /* storage defined in the object's .c file */
    ao_qindex_t  size;           /* D6 */
    ao_prio_t    priority;       /* D2 */
} ao_config_t;

/* The kernel's bookkeeping. Objects allocate it and never touch it. Zero
 * at start-up means an empty queue and a stopped timer. */
struct ao {
    const ao_config_t *config;
    volatile ao_qindex_t head;   /* oldest event; posts from interrupts */
    volatile ao_qindex_t count;  /* events waiting */
    ao_tick_t            timer_start;
    ao_tick_t            timer_ticks;  /* 0 when stopped */
    ao_data_t            timer_data;
};

/* Once, from the owner's set-up function. */
void ao_add(ao_t *self, const ao_config_t *config);

/* Handler context only. These act on the object being dispatched, so no
 * other object's timer can be named. ticks must be at least 1. Starting
 * stops the timer first, then sets its data, then starts it again. The
 * timeout carries `data` back, for example a count that recognises late
 * timeouts (D8). */
void ao_timer_start(ao_tick_t ticks, ao_data_t data);
void ao_timer_stop(void);

/* Handler context only, at most once per handler call. Copies a deferred
 * event to the front of the running object's queue, so that it is handled
 * next. A full queue is reported as in ao_post(). */
void ao_recall(const ao_event_t *e);

#endif
```

`main()` calls one function:

```c
/* ao_kernel.h */
void ao_run(void);   /* start events, then outside senders, then dispatch;
                        never returns */
```

The lamp object below uses the interface:

```c
/* lamp.c */
#include "ao_object.h"
#include "lamp.h"                /* extern ao_t *const lamp; */

#define LAMP_QUEUE_LEN 8u        /* D6 */
#define LAMP_PRIORITY  2u        /* D2 */

static void handler(const ao_event_t *e);

static ao_event_t queue[LAMP_QUEUE_LEN];
static const ao_config_t config = {
    handler, queue, LAMP_QUEUE_LEN, LAMP_PRIORITY
};
static ao_t self;                /* zero: empty queue, stopped timer */
ao_t *const lamp = &self;        /* the only thing peers can use */

void lamp_init(void)             /* called once from main(), in start order */
{
    /* configure only the pins and timers the lamp owns; its interrupts
     * are enabled later, on its start event */
    ao_add(&self, &config);
}

static void handler(const ao_event_t *e)
{
    (void)e;                     /* the state machine goes here */
}
```

Every handler matches `ao_handler_t` exactly. In C, calling a function
through a mismatched pointer type is undefined behaviour, and a cast does
not make the call safe.

With a payload struct (D3), `ao_post()` takes the payload by pointer and
copies it. With pooled events, the queue holds pointers and `ao_post()`
takes an event from the pool. The rules stay the same in both cases.

When D13 chooses an object type with several instances, the handler type
becomes `void (*)(ao_t *self, const ao_event_t *e)`. Each instance is a
struct whose first member is its `ao_t`, so the handler can convert `self`
back into the instance:

```c
typedef struct {
    ao_t    ao;                  /* first member */
    uint8_t channel;             /* example field */
    /* the instance's state and kept values */
} led_t;
```

## Cooperative kernel: port and queue

### Port

Each target supplies one small port file with the functions below, and no
other kernel code touches the hardware.

```c
/* ao_port.h */
#include "ao_types.h"

typedef unsigned ao_crit_t;      /* whatever the target's saved state needs */

/* Save the interrupt state, mask interrupts (D15), return the saved state. */
ao_crit_t ao_port_crit_enter(void);

/* Restore exactly the saved state. Never a plain "enable". */
void ao_port_crit_exit(ao_crit_t saved);

/* Called inside a critical section, after the last check found nothing to
 * do. Sleeps (D14) so that an interrupt that is already pending, or becomes
 * pending, wakes the CPU at once. Returns still inside the critical
 * section; the pending interrupt runs when the caller restores the state. */
void ao_port_idle(void);

/* A free-running tick count that wraps around (D14). */
ao_tick_t ao_port_ticks(void);

/* Unmask the CPU's interrupts once all start events have run. */
void ao_port_start(void);
```

Most cores wake from a pending interrupt while interrupts are still masked.
On those cores, the port runs the core's wait-for-interrupt instruction
inside the [critical section](glossary.md#critical-section). A core that wakes only with interrupts enabled
needs its documented enable-and-sleep sequence, which leaves no gap between
enabling and sleeping. In both cases, something must wake the CPU when a
timer falls due: the periodic tick interrupt, or a hardware timer set for
the next due timer (D14).

### Queue

- Each object has a ring buffer with `head`, the index of the oldest event,
  and `count`, the number of events waiting.
- A post writes at `(head + count) % size` and increments `count`. A take
  reads at `head`, moves `head` on and decrements `count`. Both happen
  inside a critical section.
- A recall also runs inside a critical section. It first checks for room,
  because an interrupt may have filled the queue in the meantime. It then
  moves `head` back one place, writes the event there and increments
  `count`.
- `head` and `count` are `volatile`, because interrupts post. Reading
  `count` outside a critical section is safe only where the target reads it
  in one indivisible access.
- A post from an interrupt costs a function call and a critical section.
  Measure that cost against the interrupt's time budget.

## RTOS threads

This is the alternative form under D1. Each object is one thread, and the
thread waits in exactly one place: the receive on its own queue. A higher
priority preempts a lower one. Each object still handles its own events one
at a time, and because nothing is shared, objects need no locks between
them.

### Mapping

| Part | FreeRTOS | Zephyr |
|---|---|---|
| queue | `xQueueCreateStatic()` of `ao_event_t` | `k_msgq_init()` or `K_MSGQ_DEFINE` of `ao_event_t` |
| thread | `xTaskCreateStatic()` | `k_thread_create()` |
| post from a thread | `xQueueSend(q, &e, 0)` | `k_msgq_put(q, &e, K_NO_WAIT)` |
| post from an interrupt | `xQueueSendFromISR(q, &e, &woken)`, then `portYIELD_FROM_ISR(woken)` | `k_msgq_put(q, &e, K_NO_WAIT)` |
| timer | `xTimerCreateStatic()`, one-shot. Its callback runs in the timer service task. | `k_timer_init()`. Its expiry function runs in interrupt context. |
| priority | A larger number is more urgent. | A smaller number is more urgent. Use non-negative (preemptible) priorities. |
| interrupts that post (D15) | at or below `configMAX_SYSCALL_INTERRUPT_PRIORITY` | any interrupt except a zero-latency one |

`struct ao` holds the RTOS queue, thread and timer objects in place of
`head`, `count` and the timer fields. Each thread's stack size is part of
D6.

### Thread body

```text
handle AO_SIG_START                           (before anything else)
repeat forever:
    if the recall slot holds an event:
        take it
    else:
        receive from the queue, waiting forever   (the only blocking point)
    call the handler with the event
```

- Recall uses each object's one-event recall slot in place of the RTOS
  queue, so it works whether or not the RTOS can insert at the front of a
  queue. One slot is enough,
  because a handler recalls at most once per call. Only the object's own
  thread touches the slot, so the slot needs no protection.
- On FreeRTOS, waiting forever with `portMAX_DELAY` requires
  `INCLUDE_vTaskSuspend` to be 1. Without it, loop around the receive.

### Posting

- `ao_post()` uses a zero wait (`0` or `K_NO_WAIT`), so it never blocks. A
  failed send means a full queue, a bug that `ao_post()` reports with
  `AO_ERROR()` (D12).
- On FreeRTOS, `ao_post()` uses the interrupt-safe call when an interrupt
  calls it, for example by checking `xPortIsInsideInterrupt()` where the
  port provides it. Alternatively the project provides a separate
  `ao_post_from_isr()`.

### Timers

- A timer's callback or expiry function only calls `ao_post()` with
  `AO_SIG_TIMEOUT` and the timer's data. It runs no application code.
- `ao_timer_start()` and `ao_timer_stop()` find the calling object through
  the current thread, so an object can still name only its own timer.
- `ao_timer_start()` stops the timer before setting the new data. A timer
  that fires in between therefore cannot carry the new data.
- Stopping an RTOS timer cannot take back a timeout that was already
  posted. A count carried in the timeout and checked by a [guard](glossary.md#guard) works in
  every case (D8).
- On FreeRTOS, start and stop are commands sent to the timer service task.
  Give that task a higher priority than every object, so that each command
  takes effect before the object's handler continues. Send the commands
  with a block time of 0. The timer command queue is sized under D6, and a
  failed command is an error under D12.

### Start-up

- If the CPU starts with interrupts enabled, `main()` masks them first.
- Create every queue, timer and thread before any thread runs. On FreeRTOS,
  create them all before calling `vTaskStartScheduler()`. On Zephyr, create
  the threads with a start delay of `K_FOREVER`, then call
  `k_thread_start()` on each in the order approved under D2.
- Each thread handles its own start event before its first receive. Events
  posted to the thread earlier wait in its queue.
- Each owner enables its own peripheral interrupts on its start event, after
  its queue exists.

### Calls that block

`vTaskDelay`, `k_sleep`, `xSemaphoreTake`, `k_sem_take`, `k_mutex_lock`,
`xQueueReceive` or `k_msgq_get` with a non-zero wait, and any blocking
driver call all make a handler wait. Every RTOS call in a handler therefore
uses a zero timeout. These calls are easy to reach for under RTOS threads,
and each of them breaks [run to completion](glossary.md#run-to-completion). Driver and stack calls block as
well, for example Zephyr's `i2c_transfer`, `spi_transceive` and `adc_read`;
their asynchronous or callback forms post the completion as an event.

### Shared resources

By default nothing is shared. The only exception allowed, once approved and
recorded, is a short, bounded priority-ceiling section around a resource
that several objects must use. The section uses
`vTaskSuspendAll()`/`xTaskResumeAll()` or `k_sched_lock()`/`k_sched_unlock()`,
or raises the holder to the highest priority among the users for its
duration. It makes no RTOS calls, and no user ever waits for it. These locks
cover one core only. A blocking mutex between objects is never allowed.

### Idle

The RTOS idle thread does the idling, including any tickless low-power mode
(D14). No object puts the CPU to sleep.
