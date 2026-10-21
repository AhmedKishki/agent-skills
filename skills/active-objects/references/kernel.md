# The kernel

The pattern does not depend on the kernel. This file describes what a
recommended kernel looks like: what any kernel must do, a C interface
sketch, and how it runs in the two forms of D1. The first form is a
cooperative kernel written for the project. The second is RTOS threads,
with one FreeRTOS or Zephyr thread per object.

Read this before writing or reviewing kernel code, or before adapting an
existing kernel. Everything here is a contract unless a decision (D-number)
is named; see `decisions.md`. The kernel keeps the same contracts as the objects: it never
blocks in a handler's place, never shares an object's data and never offers
a back door between objects.

## What every kernel must do

1. **It calls every handler, and nothing else does.** It never runs one
   object's handler twice at the same time.
2. **Start first.** Each object handles its start event before any other
   event sent to it.
3. **One at a time, in order.** An object's events reach it one at a time,
   first in, first out. The only exception is a recalled event, which goes
   to the front.
4. **Posting** copies the event (or passes a pooled one, D3) and returns at
   once. It never blocks, never calls the receiver, keeps no pointer into
   the sender's data and works from every context that posts. A full queue
   is handled inside the post, as decided in D5.
5. **Timers** only post a timeout into their own object's queue. An object
   can name only its own timers.
6. **Idle** never misses an event that arrives just before the CPU or thread
   goes idle.
7. **Protection.** It guards its own queues, timers and pools against every
   context that touches them, on every core that runs objects or posts.
8. **Only on events.** It calls a handler only when there is an event for
   it; idle objects are never polled.
9. **Priority** (D2) decides which object runs next. On RTOS threads it also
   lets a higher-priority object preempt a lower one. Priority alone does not
   prove a deadline is met; measure it.
10. **Sleep.** Only the kernel decides when the CPU sleeps; on an RTOS, its
    idle thread does.
11. **Nothing more.** It offers posting, timers and recall, and nothing that
    lets objects reach each other. It adds no layers or wrappers without a
    real need.

## Start-up and shutdown

- If the CPU starts with interrupts enabled, `main()` masks them before
  anything else.
- Every queue (and event pool) exists before anything can post to it.
- Each owner's set-up runs once and configures only what it owns.
- Each object handles its start event before any other event. Peers get
  starting values as messages from the owner, usually sent on its start
  event.
- An interrupt that posts is enabled only once every queue it posts to
  exists. In practice each owner enables its own interrupts on its start
  event. On a cooperative kernel, the CPU's interrupts are unmasked after
  every start event has run.
- The start order is approved as part of D2.
- An object that can stop first makes sure nothing posts to it any more,
  then releases what it owns.

## Layers

```text
objects (one .c file each)      include ao.h, and ao_object.h for themselves
ao.h, ao_object.h               the interface below
kernel core                     queues, timers, dispatching
port  or  RTOS adaptation       critical sections, idle, ticks / RTOS calls
```

Objects never include the port or RTOS headers for kernel purposes. Moving
from the cooperative kernel to RTOS threads changes the kernel core and the
adaptation, not the objects.

## Interface sketch

The types are the project's, not the kernel's. A small `ao_types.h`,
written per project, defines them:

| Type | What it is | Decided in |
|---|---|---|
| `ao_signal_t` | wide enough for every signal in the project | D3 |
| `ao_data_t` | the data an event carries: a single value or a fixed payload struct | D3 |
| `ao_tick_t` | an unsigned tick count that wraps around | D14 |
| `ao_qindex_t` | holds the largest queue size, and the target reads it in one indivisible access | D6 |
| `ao_prio_t` | holds the highest priority | D2 |

What every module may include:

```c
/* ao.h */
#ifndef AO_H
#define AO_H

#include "ao_types.h"            /* the project's types (D3, D6, D14, D2) */

typedef struct ao ao_t;          /* incomplete here: peers can only post */

enum {
    AO_SIG_START = 0,            /* delivered once, before any other event */
    AO_SIG_TIMEOUT,              /* posted by the object's own timer */
    AO_SIG_FIRST_USER            /* the application's signals start here */
};

typedef struct {
    ao_signal_t sig;
    ao_data_t   data;            /* the type chosen in D3 */
} ao_event_t;

/* Any context. Copies the event and returns at once. Never blocks and
 * never calls the receiver. A full queue is handled here, as decided in
 * D5. */
void ao_post(ao_t *to, ao_signal_t sig, ao_data_t data);

#endif
```

What only object modules and the kernel include. Peers include only `ao.h`,
where `ao_t` is incomplete, so they cannot reach these fields (D13):

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
 * next. A full queue is handled as decided in D5. */
void ao_recall(const ao_event_t *e);

#endif
```

What `main()` calls:

```c
/* ao_kernel.h */
void ao_run(void);   /* start events, then outside senders, then dispatch;
                        never returns */
```

An object then looks like this:

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

Every handler matches `ao_handler_t` exactly. Calling a function through a
mismatched pointer type is undefined behaviour in C, and a cast does not fix
it.

With D3 set to a payload struct, `ao_post()` takes it by pointer and
copies it. With pooled events, the queue holds pointers and `ao_post()`
takes a pool event. Either way, the contracts stay the same.

With D13 set to an object type with several instances, the handler type
becomes `void (*)(ao_t *self, const ao_event_t *e)`. Each instance is a
struct whose first member is its `ao_t`, so the handler can convert `self`
back to the instance:

```c
typedef struct {
    ao_t    ao;                  /* first member */
    uint8_t channel;             /* example field */
    /* the instance's state and kept values */
} led_t;
```

## Cooperative kernel (D1 default)

One loop on one stack. Handlers never interrupt each other; only interrupts
interrupt a handler. Priority decides who runs next, so check every object's
longest handler against the deadlines of every higher-priority object.

### Port

One small file per target supplies these. No other kernel code touches the
hardware.

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

Most cores can wake from a pending interrupt while interrupts are still
masked: the port runs the core's wait-for-interrupt instruction inside the
critical section. A core that wakes only with interrupts enabled needs its
documented enable-and-sleep sequence, which leaves no gap between the two.
Either way, something must wake the CPU when a timer is due: the periodic
tick interrupt, or a hardware timer set for the next due timer (D14).

### The loop

```text
for each object, highest priority first:
    call its handler with AO_SIG_START        (queued events wait)
ao_port_start()                               (the CPU's interrupts start last)
repeat forever:
    for each running timer that is due:
        stop it, then post AO_SIG_TIMEOUT with its data
    pick the highest-priority object with an event waiting
    if there is one:
        take its oldest event inside a critical section
        call its handler with that copy
    else:
        saved = ao_port_crit_enter()
        if still no event waiting and no timer due:
            ao_port_idle()
        ao_port_crit_exit(saved)              (a pending interrupt runs here)
    start the scan again from the top
```

Equal priorities are not allowed unless D2 says how ties are broken.

### Queue

- A ring buffer per object, with `head` (the oldest event) and `count` (the
  number waiting).
- A post writes at `(head + count) % size` and increments `count`. A take
  reads at `head`, moves `head` on and decrements `count`. Both happen
  inside a critical section.
- A recall also happens inside a critical section. It checks for room
  first, because an interrupt may have filled the queue meanwhile. It then
  moves `head` back one place, writes there and increments `count`.
- `head` and `count` are `volatile`, because interrupts post. Reading
  `count` outside a critical section is safe only where the target reads
  it in one indivisible access.
- A post from an interrupt costs a function call and a critical section.
  Measure it against the interrupt's time budget.

### Timers

- Each timer is a start tick and an interval, compared with
  `ao_port_ticks()`.
- It is due when `(ao_tick_t)(now - start) >= ticks`. Unsigned subtraction
  makes counter wrap-around harmless.
- It is stopped before its timeout is posted. If the queue is full, that
  timeout is lost (D5).
- To wait at least N full ticks, set N + 1 (`timers.md`).
- Handlers and the loop are the only code that touches timer fields. They
  never run at the same time, so the fields need no critical section.

## RTOS threads (D1 alternative)

Each object is one thread that waits in exactly one place: the receive on
its own queue. Higher priority preempts lower, but each object still handles
its own events one at a time, and nothing is shared, so objects need no
locks between them.

### Mapping

| Part | FreeRTOS | Zephyr |
|---|---|---|
| queue | `xQueueCreateStatic()` of `ao_event_t` | `k_msgq_init()` or `K_MSGQ_DEFINE` of `ao_event_t` |
| thread | `xTaskCreateStatic()` | `k_thread_create()` |
| post from a thread | `xQueueSend(q, &e, 0)` | `k_msgq_put(q, &e, K_NO_WAIT)` |
| post from an interrupt | `xQueueSendFromISR(q, &e, &woken)`, then `portYIELD_FROM_ISR(woken)` | `k_msgq_put(q, &e, K_NO_WAIT)` |
| timer | `xTimerCreateStatic()`, one-shot; its callback runs in the timer service task | `k_timer_init()`; its expiry function runs in interrupt context |
| priority | a larger number is more urgent | a smaller number is more urgent; use non-negative (preemptible) priorities |
| interrupts that post (D15) | at or below `configMAX_SYSCALL_INTERRUPT_PRIORITY` | not zero-latency interrupts |

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

- Recall uses a one-event slot per object instead of the RTOS queue, so it
  works whether or not the RTOS can insert at the front. One slot is enough
  because a handler recalls at most once. Only the object's own thread
  touches the slot, so it needs no protection.
- On FreeRTOS, "waiting forever" with `portMAX_DELAY` needs
  `INCLUDE_vTaskSuspend` set to 1; otherwise loop on the receive.

### Posting

- `ao_post()` uses a zero wait (`0` or `K_NO_WAIT`), so it never blocks.
  A failed send is handled as decided in D5.
- On FreeRTOS, `ao_post()` picks the interrupt-safe call when called from an
  interrupt (for example with `xPortIsInsideInterrupt()` where the port
  provides it), or the project provides a separate `ao_post_from_isr()`.

### Timers

- A timer's callback or expiry function only calls `ao_post()` with
  `AO_SIG_TIMEOUT` and the timer's data. It runs no application code.
- `ao_timer_start()` and `ao_timer_stop()` find the calling object through
  the current thread, so an object can still name only its own timer.
- `ao_timer_start()` stops the timer before it sets the new data, so a
  timer that fires in between cannot carry the new data.
- Stopping an RTOS timer does not take back a timeout that was already
  posted. A count carried in the timeout and checked by a guard is the
  method that works in every case (D8).
- On FreeRTOS, start and stop are commands sent to the timer service task.
  Give that task a higher priority than every object, so that each command
  takes effect before the object's handler goes on. Send the commands with a
  block time of 0. The timer command queue is sized under D6, and a failed
  command is an error under D12.

### Start-up

- If the CPU starts with interrupts enabled, `main()` masks them first.
- Create every queue, timer and thread before any thread runs. On FreeRTOS,
  create them all before `vTaskStartScheduler()`. On Zephyr, create the
  threads with a start delay of `K_FOREVER`, then `k_thread_start()` them
  in the order approved under D2.
- Each thread handles its own start event before receiving. Events posted
  to it earlier wait in its queue.
- Each owner enables its own peripheral interrupts on its start event, after
  its queue exists.

### What a handler must not call

`vTaskDelay`, `k_sleep`, `xSemaphoreTake`, `k_sem_take`, `k_mutex_lock`,
`xQueueReceive` or `k_msgq_get` with a non-zero wait, or any blocking driver
call. In a handler, every RTOS call uses a zero timeout. Under RTOS threads
these calls are easy to reach for, and each one breaks run to completion.

### Shared resources

Nothing is shared by default. The only allowed exception (approved and
recorded) is a short, bounded priority-ceiling section around a resource
several objects must use. Use `vTaskSuspendAll()`/`xTaskResumeAll()` or
`k_sched_lock()`/`k_sched_unlock()`, or raise the holder to the highest
user's priority for the section. Make no RTOS calls inside it. Nobody waits
for it. These locks cover one core only. A blocking mutex between objects
is never allowed.

### Idle

The RTOS idle thread does the idling, including any tickless low-power mode
(D14). No object sleeps the CPU.

## Measuring handler time

D2 needs the worst-case time of each handler. Measure it on the target:
read a cycle counter before and after the handler, or toggle a spare pin
around it and watch it with a logic analyser. Record the worst case seen
under the heaviest load.

## Kernel checklist

- [ ] Only the kernel calls handlers, never one handler twice at once.
- [ ] Every object gets its start event before any other event.
- [ ] Queues are first in, first out, except for recall at the front.
- [ ] `ao_post()` copies, returns at once, never blocks, never calls the
      receiver, works from every posting context and applies D5.
- [ ] Every critical section saves and restores the interrupt state.
- [ ] Recall is protected, checks for room and happens at most once per
      handler call.
- [ ] Timers only post into their own object's queue, and the interface
      cannot name another object's timer. Starting stops first, then sets
      the data.
- [ ] Idle cannot miss an event posted just before it, and something wakes
      the CPU when a timer is due.
- [ ] Kernel structures are protected against every context, and every
      core, that touches them.
- [ ] Interrupts that post run at a level the kernel masks.
- [ ] Nothing in the kernel lets one object reach another's internals.
- [ ] Interrupts start only after every queue exists and, on the cooperative
      kernel, after every start event has run.
