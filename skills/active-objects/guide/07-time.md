# 7. Time

A traditional RTOS manages time by blocking: a task sleeps for a while or waits on a semaphore with a timeout. [Active objects](glossary.md#active-object) never block, so the book turns time into events (section 6.6). ‘Instead, to be compatible with the active object computing model, time management must be based on the event-driven paradigm in which every interesting occurrence manifests itself as an event instance.’

## Time events

A framework manages time through *[time events](glossary.md#time-event)*, often called timers (section 6.6.1). An [active object](glossary.md#active-object) owns its time events and *arms* one when it needs a timeout. When the time comes, the framework posts the time event straight into the object's own queue, and the object handles it like any other event.

Samek's framework offers two ways of arming. `postIn()` arms a one-shot timeout, and `postEvery()` arms a periodic one. An armed time event can be *disarmed* at any time, and a one-shot event disarms itself when it fires. `rearm()` changes the number of ticks of an armed time event, which turns a one-shot time event into a watchdog that is rearmed before it can expire, or adjusts the phase of a periodic one. Each time event receives its signal once, at construction, so its signal cannot change while an earlier posting still waits in a queue (section 7.7.1).

The usual place to arm a time event is a state's [entry action](glossary.md#entry-action), and the usual place to disarm it is the same state's [exit action](glossary.md#exit-action). The philosophers of chapter 9 arm their timer on entry to *thinking* and to *eating*, and the toaster of chapter 2 arms its toasting timer on entry to *toasting* (sections 2.3.6 and 9.2.2).

UML has its own time event, written with the keyword *after* and measured from the entry into the state. Samek's time events must be armed and disarmed explicitly, which the *after* notation does not express (section 2.3.10).

## The system clock tick

[Time events](glossary.md#time-event) are driven by the *[system clock tick](glossary.md#system-clock-tick)*, a periodic interrupt, usually between 10 Hz and 100 Hz, that calls the framework's tick function (sections 6.6.2 and 7.7.2). The tick function decrements the counter of every armed time event and posts those that expire. The tick function must never execute in two contexts at once. When called from a task, one task only should call it, ideally the highest-priority one.

### Jitter

Time events are delivered late by varying amounts (section 6.6.2). The tick interrupt, every higher-priority object and the queue in front of the receiver all delay them, and ‘The jitter gets worse as the priority of the recipient [active object](glossary.md#active-object) gets lower.’ The tick is also asynchronous to the objects, so a time event armed for one tick can expire almost at once. ‘To guarantee at least one tick timeout, you need to arm a time event for two clock ticks.’ In return, time events are not lost through queuing, unlike the clock ticks of a traditional RTOS under heavy load.

## A timeout that was already posted

A timeout and another event can race (section 7.7.3). Suppose a state arms a timer on entry, and a button press leads to another state just as the timer expires. The timeout may already wait in the queue when the [exit action](glossary.md#exit-action) disarms the timer, and it then reaches the next state, which may use the same timer for a different purpose.

Samek's disarm operation reports what happened. It returns 1 if the [time event](glossary.md#time-event) was still armed, which guarantees that the timeout has not been posted and never will be. It returns 0 if the time event had already fired and posted itself. The book's figure 7.8 shows the use. The exit action of the first state stores the result in an [extended state variable](glossary.md#extended-state-variable), and the next state [guards](glossary.md#guard) its timeout transition with that variable. A timeout that arrives while the variable shows the stale posting only resets the variable, and the next timeout is the real one.

## One timer per object in small systems

QP-nano, the book's version for the smallest microcontrollers, keeps ‘a single private [time event](glossary.md#time-event) (timer) for each [active object](glossary.md#active-object) in the system’ (section 12.2.5). Each timer is a down-counter of typically two bytes, supports only one-shot timeouts, because a period would double the RAM, and posts the reserved `Q_TIMEOUT` signal. A periodic timeout comes from rearming the one-shot timer each time it fires. Disarming usually happens in a state's [exit action](glossary.md#exit-action).

## In the skill

`references/timers.md` holds the timer rules: a timer only posts into its own object's queue, an object touches only its own timers, waits of at least N ticks need N + 1 ticks, and each timer belongs to one state and is stopped when that state is left. Decision D7 chooses how many timers an object has, with QP-nano's single one-shot timer as the default. Decision D8 chooses how a late timeout is recognised: a count carried in the timeout, a stop that reports as in section 7.7.3, or a kernel that removes the queued timeout.

In the button example of `references/state-machines.md`, suspending the object while a timeout is already queued produces a late timeout, which is the case D8 covers. The old timeout still arrives, and its count shows that it is late.
