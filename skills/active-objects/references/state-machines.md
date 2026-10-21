# State machines in C

An object's behaviour is one state machine. The rules below hold in every
project. D9 decides how the machine is coded and D10 settles one detail of
nested transitions (`decisions.md`).

## Rules

A state is a stretch of time in which the object waits and reacts to events
in one particular way. The state records the part of the object's history
that still matters.

- Keep any history that changes how the object reacts as a **state**. A
  `bool` or mode variable that is tested in several places is a state that
  nobody has modelled yet. Keep other values, such as counts, measurements
  and buffers, only where modelling them as states would multiply the
  states, and give each value a reason.
- **Guards** are conditions on a transition. They have no side effects, and
  two guards on the same event in the same state never overlap. When the
  guards on one event in one state keep multiplying, the object is missing a
  state.
- Give every pair of state and signal a chosen reaction: **handle**,
  **ignore**, **defer**, or **pass** to the outer state. A pair that nobody
  has considered is a gap in the design, and the code must not drop such an
  event by default. Give the pair a reaction.
- Set-up and clean-up that belong to a state go in its **entry** and
  **exit** actions. For example, start a timer on entry and stop it on exit.
  Prefer them to actions on single transitions, because they run however
  the state is entered or left.
- After the initial transition, the state changes only in one transition
  function. That function runs the exit actions, then the transition's
  action, then the entry actions.
- Never change state inside an entry or exit action. When the next state
  depends on a condition, write two transitions with opposite guards. Entry
  and exit actions cannot see the event that caused them, so save any value
  they need beforehand.
- The machine and every state that contains other states have an initial
  transition into an inner state. The machine's own initial transition runs
  once, on the start event.
- Nest states where nesting removes repetition. An event that an inner state
  does not handle, or whose guards all fail, goes to the outer state.
- An **internal transition** runs its action and stays in the state. A
  **self-transition** leaves the state and enters it again, so its exit and
  entry actions run. Choose between them by whether the design needs the
  exit and entry actions to run.
- A deferred event waits as a copy in the object's own small store (D6). A
  state that handles deferred events recalls one on entry, and another after
  handling each recalled event, until the store is empty. A recall puts the
  event at the front of the queue, and a handler call recalls at most once.
- States and transitions are fixed in the code. Nothing builds or changes
  them at run time.

## The words

| Word | Meaning |
|---|---|
| state | a stretch of time in which the object waits and reacts in one way |
| transition | the change from one state to another, caused by an event |
| guard | a condition a transition needs, such as `e->data > LIMIT` |
| action | code that runs on a transition |
| entry action | code that runs every time a state is entered |
| exit action | code that runs every time a state is left |
| internal transition | an action that runs inside the state, with no exit or entry action |
| self-transition | leaving a state and entering it again, so both exit and entry actions run |
| initial transition | the step into an inner state when an outer state, or the whole machine, is entered |
| nested state | a state inside another state, where the outer state holds the behaviour they share |
| defer | keep an event for later, because the current state cannot handle it yet |
| pass | let the outer state handle an event that the inner state does not handle |

## Plan with an event table

Before writing code, list every state and every signal the object can
receive, and choose a reaction for each pair:

- **handle**: do something, perhaps change state.
- **ignore**: drop the event knowingly.
- **defer**: keep the event until a state that handles it is entered.
- **pass**: hand the event to the outer state.

One row may cover "any other" signal, as long as every pair ends up with a
reaction. Once the table exists, the code follows it.

The example object reads a button. It senses the button, gives it time to
settle, and tells the lamp only when the level changes. A power manager can
suspend the button object. The object has one timer and recognises late timeouts with a
count carried in the timeout, which is one possible answer to D8
(`timers.md`). The code assumes that D3 chose an integer data type,
`ao_data_t`.

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

Suspending the object while a timeout is already queued produces a late
timeout, which is the case D8 covers. The old timeout still arrives, and its
count shows that it is late.

## A flat machine (D9 default)

The button below uses the default from D9: a switch on a state `enum` with
one transition function.

```c
/* button.c */
#include <stdbool.h>
#include <stddef.h>
#include "ao_object.h"
#include "button.h"
#include "lamp.h"                /* extern ao_t *const lamp; */
#include "signals.h"             /* the project's one signal enum */

/* +1 because a timer starts partway through a tick (timers.md) */
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
    if (now != pressed) {        /* post only when the level changed */
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

In this code:

- The state is a `static enum`. `pressed` is a kept value, and its comment
  gives the reason it is not a state.
- Apart from the initial transition, only `tran()` assigns `state`. The exit
  and entry actions therefore always run, in the right order.
- An internal transition calls its action without calling `tran()`. A
  self-transition is `tran(state, action, e)`.
- The handler's `switch` follows the event table. A `break` with no match is
  an "ignore" row. Give it a comment wherever that is not obvious.
- The transition's action receives the event. Entry and exit actions do not,
  because they run however the state is entered or left.

## Nested machines (D9 alternative)

Nest states when several states share behaviour, such as a reset that works
in all of them. Each state is then a constant record naming its outer state,
its initial inner state, its entry and exit actions and its reaction to
events:

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

To dispatch an event:

1. Start at the current innermost state and call `react`. While the result
   is `PASS`, move to the parent and try again. If the outermost state
   passes as well, the event is ignored, and the design must intend that.
2. On `TRAN`, the state that returned it is the source. Find the nearest
   state that contains both the source and the target. When one of the two
   contains the other, D10 decides whether that outer state counts as
   containing them (local) or not (external).
3. Run the exit actions from the current innermost state outwards, stopping
   just below that common state.
4. Run the transition's action.
5. Run the entry actions from just below the common state inwards, down to
   the target.
6. While the target has an initial inner state, enter it and run its entry
   action. The last state reached becomes the current state.

A self-transition, where the target is the source, always leaves the source
and enters it again. D10 covers the two other cases: from an outer state to
one of its own inner states, and from an inner state out to its outer state.
Record the project's choice and apply it everywhere.

The states, their parents and their initial states are `const` and fixed
when the code is built. Nothing creates or changes them at run time.

## Deferring events

An event arrives too early when the current state cannot handle it yet, for
example a send request while the radio is still connecting. The object then
defers it:

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

- Mark the deferring states with "defer" in the event table.
- Where possible, defer in an outer state, so that the rule appears once.
- Recall the oldest event first. One recall per handler call keeps the
  deferred events in order and leaves room in the queue for events posted
  in the meantime.

## Late timeouts

Any state that stops or restarts a timer can receive a late timeout. D8
decides how the object recognises one, and `timers.md` lists the options.

## Common shapes

- One outermost state holds the behaviour that every state shares, such as a
  reset or a fault, so that behaviour is written once.
- An object posts to itself to split long work into short handler calls, or
  uses its timer to drive regular polling.
- To resume an outer state where it left off, keep the last inner state in a
  variable that the inner states' entry actions set. Enter that state in
  place of the usual initial state.
- Independent parts of one object's behaviour can live in sub-machines. A
  sub-machine belongs to its object and has no queue of its own. The object
  calls the sub-machine directly with the current event and starts the
  sub-machine's initial transition. The sub-machine reports back by posting
  to its owner's queue. No code may depend on the order in which
  sub-machines are called.

## State machine checklist

- [ ] Every pair of state and signal has a chosen reaction.
- [ ] No flag or mode variable stands in for a state, and each kept value
      has a reason for not being a state.
- [ ] Guards have no side effects and never overlap.
- [ ] After start-up, the state changes only in the transition function, in
      the order exit, action, entry.
- [ ] No transition happens inside an entry or exit action.
- [ ] Entry and exit actions do not read the event.
- [ ] Every timer is started in a state's entry action and stopped in its
      exit action, and late timeouts are recognised as decided in D8.
- [ ] Every state that contains other states has an initial transition.
- [ ] Deferred events are kept as copies in a store sized under D6, and are
      recalled oldest first, at most one per handler call.
- [ ] D10 is decided wherever a transition runs between an outer state and
      one of its own inner states.
