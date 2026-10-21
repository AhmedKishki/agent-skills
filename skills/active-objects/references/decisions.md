# Decisions

These are the parts of the design that change from project to project.
None of them may be chosen for the user.

## How to put a decision to the user

1. Before code relies on a decision, ask about it. Don't wait until the code
   is written.
2. In a few plain sentences, give the question, the options, what each one
   costs or gains, and the default where there is one.
3. Wait for a clear yes. Silence or a question is not a yes.
4. Ask where approved decisions are recorded, and record each one there
   with its reason.
5. If a later change needs a different answer, put the change to the user in
   the same way.

Each message's agreement is a decision in the same way
(`objects-and-messages.md`). So is every exception to a contract.

## The decisions

| # | Decision | Options | Default | Details in |
|---|---|---|---|---|
| D1 | Kernel | a cooperative kernel written for the project: one loop, handlers never interrupt each other; RTOS threads: one FreeRTOS or Zephyr thread per object, higher priority preempts lower | cooperative kernel | `kernel.md` |
| D2 | Priorities, deadlines and start order | the order of objects (cooperative) or thread priorities (RTOS); each object's deadline; how worst-case handler time is measured; how equal priorities are handled; the order in which objects start | ordered by deadline, measured on the target | `kernel.md` |
| D3 | Event types and memory | the signal type; the data type and size (a single value, or a fixed payload); events copied into the queue, or read-only events from a pool with a use count | copied into the queue; no default for the types or size | `objects-and-messages.md`, `kernel.md` |
| D4 | Delivery | posted to a named object; published to subscribers; both | named object | `objects-and-messages.md` |
| D5 | Full queue, store or pool | drop the new event, only where you can show for that message that it never happens; treat it as a bug and stop with an assertion; keep spare room for key messages | none | `objects-and-messages.md`, `kernel.md` |
| D6 | Sizes | each queue, deferral store and event pool; under RTOS threads, each thread stack and the RTOS timer command queue | start generous, record the lowest free count under the heaviest load, shrink with a recorded margin | `objects-and-messages.md` |
| D7 | Timers per object | one one-shot timer; several, each with its own signal; periodic timers | one one-shot timer | `timers.md` |
| D8 | Late timeouts | a count carried in the timeout and checked by a guard; a stop that reports "already posted"; a kernel that removes it from the queue on stop | none | `timers.md` |
| D9 | State-machine coding | a switch on a state `enum` with one transition function; state-handler functions with nesting; a state table | a switch for flat machines; propose an approach when nesting is needed | `state-machines.md` |
| D10 | Nested transitions | whether a transition between an outer state and one of its own inner states leaves and re-enters the outer state (external) or not (local) | none; ask when nesting is used | `state-machines.md` |
| D11 | Boundary modules | which modules are not objects (drivers, clock, pure helpers, protocol converters), what each may do, how one used by several objects is protected | nothing exempt until decided | `objects-and-messages.md` |
| D12 | Errors | the response to a broken contract, an impossible event, or an overflow that must not happen; for example, an assertion kept on in production with a handler that stops, records and restarts | none | `handlers.md` |
| D13 | Objects and hiding | one object per `.c` file with `static` state; or an object type with several instances, whose handler gets a `self` pointer; how internals are kept out of reach | one object per `.c` file; peers see only an incomplete type | `objects-and-messages.md`, `kernel.md` |
| D14 | Ticks and sleep | the tick period and tick type; how deep idle sleeps; what wakes it (a periodic tick, or a hardware timer set for the next due timer) | none; ask with the power budget in hand | `timers.md`, `kernel.md` |
| D15 | Interrupt levels | the kernel's critical sections mask all interrupts; or only those up to a set level, so that faster interrupts above it keep running but may never post | mask all interrupts | `handlers.md`, `kernel.md` |
