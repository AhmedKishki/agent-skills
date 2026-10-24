# 7. Time

A traditional RTOS manages time by blocking: a task sleeps for a while or waits on a semaphore with a timeout. [Active objects](glossary.md#active-object) never block, so time has to reach them as events, like every other occurrence that matters.

## Time events

A framework manages time through *[time events](glossary.md#time-event)*, often called timers. An [active object](glossary.md#active-object) owns its time events and *arms* one when it needs a timeout. When the time comes, the framework posts the time event straight into the object's own queue, and the object handles it like any other event.[^1]

The QF framework arms a time event in two ways: `postIn()` for a one-shot timeout and `postEvery()` for a periodic one. An armed time event can be *disarmed* at any time, and a one-shot event disarms itself when it fires. `rearm()` changes the number of ticks of an armed time event, which turns a one-shot time event into a watchdog that is rearmed before it can expire, or adjusts the phase of a periodic one.[^2] Each time event receives its signal once, at construction, so its signal cannot change while an earlier posting still waits in a queue.

The usual place to arm a time event is a state's [entry action](glossary.md#entry-action), and the usual place to disarm it is the same state's [exit action](glossary.md#exit-action). A toaster arms its toasting timer on entry to *toasting* and disarms it on exit, and a philosopher arms its timer on entry to *thinking* and to *eating*.

UML has its own time event, written with the keyword *after* and measured from the entry into the state. Time events that must be armed and disarmed explicitly do not fit that notation.

## The system clock tick

[Time events](glossary.md#time-event) are driven by the *[system clock tick](glossary.md#system-clock-tick)*, a periodic interrupt, typically between 10 Hz and 100 Hz, that calls the framework's tick function.[^3] The tick function decrements the counter of every armed time event and posts those that expire. It must never run in two contexts at once. When a task calls it, one task only should do so, ideally the highest-priority one.

### Jitter

Time events arrive late by varying amounts. The tick interrupt, every higher-priority object and the queue in front of the receiver all delay them, and the lower the priority of the receiving object, the worse the jitter. The tick is asynchronous to the objects, so a time event armed for one tick can expire almost at once, and at least one full tick needs a time event armed for two. Time events are not lost through queuing, unlike the clock ticks of a traditional RTOS under heavy load.[^4]

## A timeout that was already posted

A timeout and another event can race. A state arms a timer on entry, and a button press leads to another state just as the timer expires. The timeout may already wait in the queue when the [exit action](glossary.md#exit-action) disarms the timer, and it then reaches the next state, which may use the same timer for a different purpose.

The QF disarm operation reports what happened. It returns 1 if the [time event](glossary.md#time-event) was still armed, which guarantees that the timeout has not been posted and never will be. It returns 0 if the time event had already fired and posted itself.[^5] The exit action of the first state stores the result in an [extended state variable](glossary.md#extended-state-variable), and the next state [guards](glossary.md#guard) its timeout transition with that variable. A timeout that arrives while the variable marks the stale posting only resets the variable, and the next timeout is the real one.[^6]

## One timer per object in small systems

On the smallest microcontrollers, each [active object](glossary.md#active-object) can have a single private [time event](glossary.md#time-event).[^7] Each timer is a down-counter of typically two bytes and supports only one-shot timeouts, because a period would double the RAM. It posts a reserved timeout signal. A periodic timeout comes from rearming the one-shot timer each time it fires, and disarming usually happens in a state's [exit action](glossary.md#exit-action).

## In the skill

`references/timers.md` holds the timer rules: a timer only posts into its own object's queue, an object touches only its own timers, waits of at least N ticks need N + 1 ticks, and each timer belongs to one state and is stopped when that state is left. Decision D7 chooses how many timers an object has, with a single one-shot timer as the default. Decision D8 chooses how a late timeout is recognised: a count carried in the timeout, a stop that reports, or a kernel that removes the queued timeout.

In the button example of `references/state-machines.md`, suspending the object while a timeout is already queued produces a late timeout, which is the case D8 covers. The old timeout still arrives, and its count shows that it is late.

[^1]: Miro Samek, *Practical UML Statecharts in C/C++: Event-Driven Programming for Embedded Systems*, 2nd ed. (Newnes, 2009), §6.6.1, p. 291.
[^2]: Ibid., §6.6.1, p. 292.
[^3]: Ibid., §6.6.2, p. 293.
[^4]: Ibid.
[^5]: Ibid., §7.7.3, p. 358.
[^6]: Ibid., §7.7.3, p. 359.
[^7]: Ibid., §12.2.5, p. 626.
