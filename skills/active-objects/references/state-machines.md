# State machines in C

An object's behaviour is one state machine. The rules below hold in every project. D9 decides how the machine is coded and D10 settles one detail of nested transitions (`decisions.md`).

## Rules

A state is a stretch of time in which the object waits and reacts to events in one particular way. The state records the part of the object's history that still matters.

- Keep any history that changes how the object reacts as a **state**. A `bool` or mode variable that is tested in several places is a state that nobody has modelled yet. Keep other values, such as counts, measurements and buffers, only where modelling them as states would multiply the states, and give each value a reason.
- **Guards** are conditions on a transition. They have no side effects, and two guards on the same event in the same state never overlap. When the guards on one event in one state keep multiplying, the object is missing a state.
- Give every pair of state and signal a chosen reaction: **handle**, **ignore**, **defer**, or **pass** to the outer state. A pair that nobody has considered is a gap in the design, and the code must not drop such an event by default. Give the pair a reaction.
- Set-up and clean-up that belong to a state go in its **entry** and **exit** actions. For example, start a timer on entry and stop it on exit. Prefer them to actions on single transitions, because they run however the state is entered or left.
- After the initial transition, the state changes in one place only: the transition function, or the event processor. A transition runs its action first, then the exit actions, then the entry actions. The action comes first because it belongs to the source state, like the guard: run after the exit actions, it would find taken down what it may still need, such as a sensor the exit action switched off.
- Never change state inside an entry or exit action. When the next state depends on a condition, write two transitions with opposite guards. Entry and exit actions cannot see the event that caused them, so save any value they need beforehand.
- The machine and every state that contains other states have an initial transition into an inner state. An initial transition has no guard, and its target lies inside the state that owns it. The machine's own initial transition runs once, on the start event.
- Nest states where nesting removes repetition. An event that an inner state does not handle, or whose guards all fail, goes to the outer state.
- An **internal transition** runs its action and stays in the state. A **self-transition** leaves the state and enters it again, so its exit and entry actions run. Choose between them by whether the design needs the exit and entry actions to run.
- States and transitions are fixed in the code. Nothing builds or changes them at run time.

## Plan with an event table

Before writing code, list every state and every signal the object can receive, and choose a reaction for each pair:

- **handle**: do something, perhaps change state.
- **ignore**: drop the event knowingly.
- **defer**: keep the event until a state that handles it is entered.
- **pass**: hand the event to the outer state.

One row may cover "any other" signal, as long as every pair ends up with a reaction. Once the table exists, the code follows it. The object's statechart (`diagrams.md`) draws the same machine: the table shows that every pair has a reaction, and the statechart shows the machine's shape.

The example object reads a button. It senses the button, gives it time to settle, and tells the lamp only when the level changes. A power manager can suspend the button object. The object has one timer and recognises late timeouts with a count carried in the timeout, which is one possible answer to D8 (`timers.md`). The code assumes that D3 chose an integer data type, `ao_data_t`.

| State | Signal | Guard | Reaction | Action | Next state |
|---|---|---|---|---|---|
| (start) | `AO_SIG_START` | – | handle | – | Sensing |
| Sensing | entry | – | – | `sense_begin()`, then start the timer (settle) | – |
| Sensing | `AO_SIG_TIMEOUT` | count matches | handle | read the level and post any change to the lamp | Waiting |
| Sensing | `POWER_SUSPEND` | – | handle | abandon the reading | Suspended |
| Waiting | entry | – | – | start the timer (poll − settle) | – |
| Waiting | `AO_SIG_TIMEOUT` | count matches | handle | – | Sensing |
| Waiting | `POWER_SUSPEND` | – | handle | – | Suspended |
| Sensing, Waiting | exit | – | – | stop the timer | – |
| Suspended | `POWER_RESUME` | – | handle | – | Sensing |
| any | `AO_SIG_TIMEOUT` | count does not match | ignore | – | – |
| any | any other | – | ignore | – | – |

## State-handler functions (D9 default)

Each state is one function. It receives every event that arrives while the object is in that state, and the reserved signals `AO_SIG_ENTRY` and `AO_SIG_EXIT` when the state is entered and left. Its entry and exit actions therefore sit in the same `switch` as its reactions. The current state is a pointer to that function, and a small event processor, `dispatch()`, is the only code that calls it.

```c
/* button.c */
#include <stdbool.h>
#include "ao_object.h"
#include "button.h"
#include "lamp.h"                /* extern ao_t *const lamp; */
#include "signals.h"             /* the project's one signal enum */

/* +1 because a timer starts partway through a tick (timers.md) */
#define SETTLE_TICKS (5u + 1u)           /* at least 5 ticks */
#define WAIT_TICKS   ((20u - 5u) + 1u)   /* at least 15 ticks */

typedef enum { RET_HANDLED, RET_IGNORED, RET_TRAN } ret_t;
typedef ret_t (*state_t)(const ao_event_t *e);

static ret_t sensing(const ao_event_t *e);
static ret_t waiting(const ao_event_t *e);
static ret_t suspended(const ao_event_t *e);

static state_t    state;         /* the current state's function */
static ao_data_t  timer_count;   /* recognises late timeouts (D8) */
static bool       pressed;       /* last level reported; as states it would
                                    double the machine */

static const ao_event_t entry_event = { AO_SIG_ENTRY, 0 };
static const ao_event_t exit_event  = { AO_SIG_EXIT, 0 };

static void sense_begin(void);
static bool sense_end(void);     /* the debounced level */

static void timer_start(ao_tick_t ticks)
{
    ao_timer_start(ticks, ++timer_count);
}

/* A state returns tran(target) to take a transition, after its action. */
static ret_t tran(state_t target)
{
    state = target;
    return RET_TRAN;
}

/* The event processor: after start-up, the only caller of the states.
 * The source state has already run the transition's action; the
 * processor exits the source, then enters the target. */
static void dispatch(const ao_event_t *e)
{
    state_t source = state;

    if (source(e) == RET_TRAN) {
        (void)source(&exit_event);
        (void)state(&entry_event);
    }
}

static void report_change(void)
{
    bool now = sense_end();
    if (now != pressed) {        /* post only when the level changed */
        pressed = now;
        ao_post(lamp, now ? BUTTON_PRESSED : BUTTON_RELEASED, 0);
    }
}

static ret_t sensing(const ao_event_t *e)
{
    switch (e->sig) {
    case AO_SIG_ENTRY:
        sense_begin();
        timer_start(SETTLE_TICKS);
        return RET_HANDLED;
    case AO_SIG_EXIT:
        ao_timer_stop();
        return RET_HANDLED;
    case AO_SIG_TIMEOUT:
        if (e->data == timer_count) {    /* guard: not a late timeout (D8) */
            report_change();
            return tran(waiting);
        }
        return RET_IGNORED;
    case POWER_SUSPEND:
        (void)sense_end();               /* abandon the reading */
        return tran(suspended);
    }
    return RET_IGNORED;                  /* any other signal */
}

static ret_t waiting(const ao_event_t *e)
{
    switch (e->sig) {
    case AO_SIG_ENTRY:
        timer_start(WAIT_TICKS);
        return RET_HANDLED;
    case AO_SIG_EXIT:
        ao_timer_stop();
        return RET_HANDLED;
    case AO_SIG_TIMEOUT:
        if (e->data == timer_count) {
            return tran(sensing);
        }
        return RET_IGNORED;
    case POWER_SUSPEND:
        return tran(suspended);
    }
    return RET_IGNORED;
}

static ret_t suspended(const ao_event_t *e)
{
    switch (e->sig) {
    case POWER_RESUME:
        return tran(sensing);
    }
    return RET_IGNORED;                  /* a late timeout lands here */
}

static void handler(const ao_event_t *e)
{
    if (e->sig == AO_SIG_START) {        /* the initial transition */
        state = sensing;
        (void)state(&entry_event);
        return;
    }
    dispatch(e);
}
```

In this code:

- Each state's function holds all of that state: its entry and exit actions, its guards and every reaction. Reading one function is enough to draw the state.
- `state` points at the current state's function. Apart from the initial transition, only `tran()` changes it, and only `dispatch()` calls the states, so every transition runs its action, then exit, then entry.
- An internal transition does its work and returns `RET_HANDLED`. A self-transition returns `tran()` with its own state, so its exit and entry actions run.
- A guard is an `if` inside its `case`. When the guard fails, the state returns `RET_IGNORED`, as the event table's "ignore" row says.
- A state function works only inside its `switch`, because the processor also calls it for entry and exit. Code before the `switch` would run on those calls too.

## Nested states

Nest states where several states share behaviour, such as a reset that works in all of them. The state functions keep the shape above and change in three ways:

- An event that a state does not handle, or whose guards all fail, goes to its outer state: the function ends with `return super(outer);` in place of `return RET_IGNORED;`. The outermost states name `top`, which ignores everything and is never the target of a transition.
- A state that contains other states answers `AO_SIG_INIT` with `tran()` to one of its inner states.
- `tran()` and `super()` leave their answer in `temp`, because the processor needs the current state and the target at the same time.

```c
typedef enum { RET_HANDLED, RET_IGNORED, RET_TRAN, RET_SUPER } ret_t;
typedef ret_t (*state_t)(const ao_event_t *e);

static state_t state;            /* the current innermost state */
static state_t temp;             /* RET_TRAN: the target; RET_SUPER: the outer state */

static ret_t tran(state_t target) { temp = target; return RET_TRAN; }
static ret_t super(state_t outer) { temp = outer;  return RET_SUPER; }

static ret_t top(const ao_event_t *e)
{
    (void)e;
    return RET_IGNORED;          /* the end of every chain of outer states */
}

static ret_t on(const ao_event_t *e)
{
    switch (e->sig) {
    case AO_SIG_ENTRY: lamp_power(true);  return RET_HANDLED;
    case AO_SIG_EXIT:  lamp_power(false); return RET_HANDLED;
    case AO_SIG_INIT:  return tran(dim);  /* initial transition */
    case RESET:        return tran(on);   /* works in every inner state */
    }
    return super(top);
}

static ret_t dim(const ao_event_t *e)
{
    switch (e->sig) {
    case BRIGHTER: return tran(bright);
    }
    return super(on);            /* everything else goes to on */
}
```

`bright` has the same shape as `dim`.

To dispatch an event, the processor:

1. Calls the current state with the event. While the answer is `RET_SUPER`, it calls the outer state named in `temp`. When the chain reaches `top`, the event is ignored, and the design must intend that.
2. On `RET_TRAN`, the transition's action has already run inside the state that answered, which is the source. The processor finds the nearest state that contains both the source and the target. It learns each state's outer state by calling the state with `AO_SIG_EMPTY`, which no state handles. When one of the two contains the other, D10 decides whether that outer state counts as containing them (local) or not (external).
3. Runs the exit actions from the current innermost state outwards, stopping just below that common state.
4. Runs the entry actions from just below the common state inwards, down to the target.
5. While the state just entered answers `AO_SIG_INIT` with `RET_TRAN`, enters that inner state as well. The last state entered becomes the current state.

On `AO_SIG_START`, the handler enters the target of the machine's initial transition, outermost state first, and then follows the `AO_SIG_INIT` answers as in step 5.

A self-transition, where the target is the source, always leaves the source and enters it again. D10 covers the two other cases: from an outer state to one of its own inner states, and from an inner state out to its outer state. Record the project's choice and apply it everywhere.

The nesting and the transitions are written into the state functions, so they are fixed when the code is built. Nothing creates or changes them at run time.

## Deferring events

An event arrives too early when the current state cannot handle it yet, for example a send request while the radio is still connecting. The object then defers it:

```c
#define DEFER_LEN 2u             /* D6 */

static ao_event_t deferred[DEFER_LEN];
static uint8_t    deferred_count;

static void defer(const ao_event_t *e)
{
    if (deferred_count >= DEFER_LEN) {     /* a bug: the store is too small (D6) */
        AO_ERROR();                        /* D12; if it returns, e is dropped */
        return;
    }
    deferred[deferred_count++] = *e;       /* a copy: *e is gone after the call */
}

/* Call on entry to a state that handles deferred events, and again after
 * handling each recalled event. At most once per handler call. */
static void recall_one(void)
{
    if (deferred_count > 0u) {
        ao_recall(&deferred[0]);           /* copied to the front: next */
        for (uint8_t i = 1u; i < deferred_count; i++) {
            deferred[i - 1u] = deferred[i];
        }
        deferred_count--;
    }
}
```

- Mark the deferring states with "defer" in the event table.
- Where possible, defer in an outer state, so that the rule appears once.
- A state that handles deferred events recalls one on entry, and another after handling each recalled event, until the store is empty. Recall the oldest first: one recall per handler call keeps the deferred events in order and leaves room in the queue for events posted in the meantime.

## Common shapes

- One outermost state holds the behaviour that every state shares, such as a reset or a fault, so that behaviour is written once.
- An object posts to itself to split long work into short handler calls, or uses its timer to drive regular polling.
- To resume an outer state where it left off, keep the last inner state in a variable that the inner states' entry actions set. Enter that state in place of the usual initial state.
- Independent parts of one object's behaviour can live in sub-machines. A sub-machine belongs to its object and has no queue of its own. The object calls the sub-machine directly with the current event and starts the sub-machine's initial transition. The sub-machine reports back by posting to its owner's queue. No code may depend on the order in which sub-machines are called.
