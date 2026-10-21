# State machines in C

Read this before designing, writing or reviewing an object's behaviour.
It lists the contracts, explains the words, shows how to plan a machine
with an event table, and gives C shapes for flat and nested machines and
for deferred events. Everything in the contracts section holds in every
project; the decisions (D-numbers) are in `decisions.md`.

## Contracts

A state is a stretch of time in which the object waits and reacts in one
way. It holds the part of the history that matters.

- History that changes how the object reacts is a **state**, not a flag. A
  `bool` or mode variable tested in several places is a missing state. Keep
  other values (counts, measurements, buffers) only where states would
  multiply, and give each one a reason.
- **Guards** (conditions on a transition) have no side effects. Guards on the
  same event in the same state never overlap. A growing chain of guards is a
  missing state.
- Every state and signal pair has a deliberate reaction: **handle**,
  **ignore**, **defer** or **pass** to the outer state. A pair nobody thought
  about is a gap, not permission to drop the event.
- Set-up and clean-up that belong to a state go in its **entry** and **exit**
  actions: start a timer on entry, stop it on exit.
- After the initial transition, the state changes only through one
  transition function. It runs the exit actions, then the transition's
  action, then the entry actions.
- No state change inside an entry or exit action. If the next state depends
  on a condition, use two transitions with opposite guards. Entry and exit
  actions cannot see the event that caused them; save any value they need
  first.
- The machine, and every state that contains others, has an initial
  transition into an inner state. The machine's first one runs once, on the
  start event.
- Nest states when it removes repetition. An event an inner state does not
  handle, or whose guards all fail, goes to the outer state. How the coding
  works is D9; one detail of nested transitions is D10.
- An **internal transition** runs its action and stays put. A
  **self-transition** leaves and re-enters, running exit and entry actions.
  Choose on purpose.
- A deferred event waits, as a copy, in the object's own small store (D6). A
  state that handles deferred events recalls one on entry, and another
  after handling each recalled event, while the store is not empty. A
  recall puts the event at the front of the queue, at most once per handler
  call.
- States and transitions are fixed in the code, never built at run time.

## The words

| Word | Meaning |
|---|---|
| state | a stretch of time in which the object waits and reacts in one way |
| transition | the change from one state to another, caused by an event |
| guard | a condition a transition needs, such as `e->data > LIMIT` |
| action | code that runs on a transition |
| entry action | code that runs every time a state is entered |
| exit action | code that runs every time a state is left |
| internal transition | an action that runs without leaving the state; no exit or entry |
| self-transition | leaving a state and entering it again; exit and entry both run |
| initial transition | the step into an inner state when an outer state, or the whole machine, is entered |
| nested state | a state inside another; the outer state holds behaviour they share |
| defer | keep an event for later, because the current state cannot handle it yet |
| pass | let the outer state handle an event the inner state does not |

## Plan first: the event table

Before writing code, list every state and every signal the object can
receive, and give each pair a reaction:

- **handle**: do something, perhaps change state;
- **ignore**: drop it on purpose;
- **defer**: keep it until a state that handles it is entered;
- **pass**: hand it to the outer state.

A row may cover "any other" signal, but no pair is left to chance. Write
the table before the code; the code then follows it.

An example: a button that is sensed, given time to settle, and reported to
the lamp only when its level changes. A power manager can suspend it. It
uses one timer, and a count carried in the timeout recognises late ones
(one possible answer to D8, see `timers.md`). It assumes D3 chose an integer
data type, `ao_data_t`.

| State | Signal | Guard | Reaction | Action | Next state |
|---|---|---|---|---|---|
| (start) | `AO_SIG_START` | – | handle | – | Sensing |
| Sensing | entry | – | – | `sense_begin()`; start timer (settle) | – |
| Sensing | `AO_SIG_TIMEOUT` | count matches | handle | read the level; post a change to the lamp | Waiting |
| Sensing | `POWER_SUSPEND` | – | handle | abandon the reading | Suspended |
| Waiting | entry | – | – | start timer (poll − settle) | – |
| Waiting | `AO_SIG_TIMEOUT` | count matches | handle | – | Sensing |
| Waiting | `POWER_SUSPEND` | – | handle | – | Suspended |
| Sensing, Waiting | exit | – | – | stop the timer | – |
| Suspended | `POWER_RESUME` | – | handle | – | Sensing |
| any | `AO_SIG_TIMEOUT` | count does not match | ignore | – | – |
| any | any other | – | ignore | – | – |

Suspending while a timeout is already queued is exactly the case D8 is
about. The old timeout still arrives, and the count shows it is late.

## A flat machine (D9 default)

A switch on a state `enum`, with one transition function. This is the
button above.

```c
/* button.c */
#include <stdbool.h>
#include <stddef.h>
#include "ao_object.h"
#include "button.h"
#include "lamp.h"                /* extern ao_t *const lamp; */
#include "signals.h"             /* the project's one signal enum */

/* +1 because a timer starts partway through a tick (references/kernel.md) */
#define SETTLE_TICKS (5u + 1u)           /* at least 5 ticks */
#define WAIT_TICKS   ((20u - 5u) + 1u)   /* at least 15 ticks */

enum state { SENSING, WAITING, SUSPENDED };

static enum state state;
static ao_data_t  timer_count;   /* recognises late timeouts (D8) */
static bool       pressed;       /* last level reported; as states it would
                                    double the machine */

static void sense_begin(void);
static bool sense_end(void);     /* the debounced level */

static void timer_start(ao_tick_t ticks)
{
    ao_timer_start(ticks, ++timer_count);
}

static bool is_current_timeout(const ao_event_t *e)
{
    return e->sig == AO_SIG_TIMEOUT && e->data == timer_count;
}

static void entry(enum state s)
{
    switch (s) {
    case SENSING:   sense_begin(); timer_start(SETTLE_TICKS); break;
    case WAITING:   timer_start(WAIT_TICKS);                  break;
    case SUSPENDED:                                           break;
    }
}

static void exit_action(enum state s)
{
    switch (s) {
    case SENSING:
    case WAITING:   ao_timer_stop(); break;   /* each stops its own timer */
    case SUSPENDED:                  break;
    }
}

typedef void (*action_t)(const ao_event_t *e);

/* After start-up, the only place the state changes:
 * exit, then the action, then entry. */
static void tran(enum state next, action_t action, const ao_event_t *e)
{
    exit_action(state);
    if (action != NULL) {
        action(e);
    }
    state = next;
    entry(next);
}

static void report_change(const ao_event_t *e)
{
    (void)e;
    bool now = sense_end();
    if (now != pressed) {        /* post a change, not a repeat */
        pressed = now;
        ao_post(lamp, now ? BUTTON_PRESSED : BUTTON_RELEASED, 0);
    }
}

static void abandon_reading(const ao_event_t *e)
{
    (void)e;
    (void)sense_end();
}

static void handler(const ao_event_t *e)
{
    if (e->sig == AO_SIG_START) {        /* the initial transition */
        state = SENSING;
        entry(SENSING);
        return;
    }
    switch (state) {
    case SENSING:
        if (is_current_timeout(e)) {
            tran(WAITING, report_change, e);
        } else if (e->sig == POWER_SUSPEND) {
            tran(SUSPENDED, abandon_reading, e);
        }
        break;                           /* anything else: ignore */
    case WAITING:
        if (is_current_timeout(e)) {
            tran(SENSING, NULL, e);
        } else if (e->sig == POWER_SUSPEND) {
            tran(SUSPENDED, NULL, e);
        }
        break;
    case SUSPENDED:
        if (e->sig == POWER_RESUME) {
            tran(SENSING, NULL, e);
        }
        break;                           /* a late timeout lands here */
    }
}
```

What the shape shows:

- The state is a `static enum`, never a set of flags. `pressed` is a kept
  value with a stated reason.
- Apart from the initial transition, `tran()` is the only place `state` is
  assigned, so exit and entry actions always run, in the right order.
- An internal transition is just the action, with no call to `tran()`. A
  self-transition is `tran(state, action, e)`.
- The handler's `switch` mirrors the event table. Each `break` without a
  match is an "ignore" row; write a comment where that is not obvious.
- The action gets the event; entry and exit actions do not, because they
  run however the state is entered or left.

## Nested machines (D9 alternative)

Use nesting when several states share behaviour, such as a "reset" that
works in all of them. Each state is a constant record that names its outer
state, its initial inner state, its entry and exit actions and its reaction
to events:

```c
typedef enum { HANDLED, IGNORED, PASS, TRAN } ao_result_t;

typedef struct state state_t;

typedef struct {
    ao_result_t    result;
    const state_t *target;                       /* when result is TRAN */
    void         (*action)(const ao_event_t *e); /* when TRAN; may be NULL */
} reaction_t;

struct state {
    const state_t *parent;       /* NULL for the outermost state */
    const state_t *initial;      /* inner state to enter, or NULL */
    void         (*entry)(void);
    void         (*exit)(void);
    reaction_t   (*react)(const ao_event_t *e);
};
```

Dispatching an event:

1. Start at the current innermost state and call `react`. While the result
   is `PASS`, move to the parent and try again. If the outermost state
   passes too, the event is ignored; make sure that is deliberate.
2. On `TRAN`, the state that returned it is the source. Find the nearest
   state that contains both the source and the target. When one of them
   contains the other, D10 decides whether that outer state counts as
   "containing" (local) or not (external).
3. Run exit actions from the current innermost state outwards, stopping
   just below that common state.
4. Run the transition's action.
5. Run entry actions from just below the common state inwards, down to the
   target.
6. While the target has an initial inner state, enter it and run its entry
   action. The last one reached is the new current state.

A self-transition (the target is the source) always leaves and re-enters
the source. D10 covers the other two cases, from an outer state to one of
its own inner states and back out. Record which one the project uses, and
keep it the same everywhere.

The states, their parents and their initial states are `const` and fixed at
build time. Nothing creates or changes them while the program runs.

## Deferring events

Defer when an event arrives too early: for example, a "send" request while
the radio is still connecting.

```c
#define DEFER_LEN 2u             /* D6 */

static ao_event_t deferred[DEFER_LEN];
static uint8_t    deferred_count;

static void defer(const ao_event_t *e)
{
    if (deferred_count < DEFER_LEN) {
        deferred[deferred_count++] = *e;   /* a copy: *e is gone after the call */
    } else {
        /* a full store is handled as decided in D5 */
    }
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

- Mark the deferring states in the event table with "defer".
- Defer in an outer state where possible, so that the rule is written once.
- Recall the oldest first. Recalling one event per handler call keeps them
  in order and leaves room for events posted meanwhile.

## Late timeouts

Any state that stops or restarts a timer can receive a late timeout. How to
recognise it is D8; the options are in `timers.md`.

## Useful shapes

- **One outermost state** for behaviour every state shares, such as reset or
  a fault, written once.
- **Posting to yourself** to split long work into short handler calls, or to
  drive regular polling with the timer.
- **Remembering the last inner state**, so that re-entering an outer state
  resumes where it left off. Keep the last inner state in a variable set by
  the inner states' entry actions, and enter it instead of the usual initial
  state.
- **Sub-machines** for independent parts of one object's behaviour. A
  sub-machine is part of its object, not an object: the object calls it
  directly with the current event and starts its initial transition itself.
  It reports back by posting to the owner's queue. Never depend on the order
  in which sub-machines are called.

## State machine checklist

- [ ] Every state and signal pair has a deliberate reaction.
- [ ] No flag or mode variable stands in for a state. Each kept value has a
      reason not to be a state.
- [ ] Guards have no side effects and never overlap.
- [ ] After start-up, the state changes only in the transition function, in
      the order exit, action, entry.
- [ ] No transition happens inside an entry or exit action.
- [ ] Entry and exit actions do not read the event.
- [ ] Every timer is started in a state's entry and stopped in its exit,
      and late timeouts are recognised as decided in D8.
- [ ] Every state that contains others has an initial transition.
- [ ] Deferred events are kept as copies, in a store sized under D6, and
      recalled oldest first, at most one per handler call.
- [ ] D10 is decided wherever a transition goes between an outer state and
      one of its own inner states.
