# Decisions

## Putting a decision to the user

- A few plain sentences are enough for each option. Silence or a follow-up
  question leaves the decision open, and each approved decision is recorded
  with its reason.
- When a later change needs a different answer, put the new question to the
  user in the same way.
- The agreement for each message is also a decision
  (`objects-and-messages.md`), and so is every exception to a contract.

## The decisions

| # | Decision | Options | Default | Module |
|---|---|---|---|---|
| D1 | Kernel | A cooperative kernel written for the project, where one loop runs the handlers and no handler interrupts another. Or RTOS threads, one FreeRTOS or Zephyr thread per object, where a higher priority preempts a lower one. | Cooperative kernel. | `kernel.md` |
| D2 | Priorities, deadlines and start order | The order of the objects (cooperative) or their thread priorities (RTOS). Each object's deadline. How the worst-case handler time is measured. How equal priorities are treated. The order in which the objects start. | Order by deadline and measure on the target. | `kernel.md` |
| D3 | Event types and memory | The signal type. The data type and size, either one value or a fixed payload. Whether events are copied into the queue or taken read-only from a pool with a use count. | Copied into the queue. No default for the types or the size. | `objects-and-messages.md`, `kernel.md` |
| D4 | Delivery | Post to a named object, publish to subscribers, or both. | Named object. | `objects-and-messages.md` |
| D6 | Sizes | Every queue, deferral store and event pool, each sized on its own. Under RTOS threads, also each thread stack and the RTOS timer command queue. | Start generous, record the lowest free count under the heaviest load, then shrink and keep a recorded margin. | `objects-and-messages.md` |
| D7 | Timers per object | One one-shot timer, several timers with a signal each, or periodic timers. | One one-shot timer. | `timers.md` |
| D8 | Late timeouts | Carry a count in the timeout and check it with a guard. Use a stop that reports whether the timeout was already posted. Or let the kernel remove the queued timeout on stop. | None. | `timers.md` |
| D9 | State-machine coding | State-handler functions: one function per state, holding its entry and exit actions as reserved signals beside its reactions; the same shape nests. A switch on a state `enum`, where a state's entry and exit actions sit apart from its reactions. A state table, where every new state needs an entry for every signal. | State-handler functions. | `state-machines.md` |
| D10 | Nested transitions | For a transition between an outer state and one of its own inner states, either leave and re-enter the outer state (external) or stay in it (local). | Local, so a move inside an outer state never runs that state's exit and entry actions. | `state-machines.md` |
| D11 | Boundary modules | Which modules are not objects (drivers, the clock, pure helpers, protocol converters). What each one may do. How a module used by several objects is protected. | No module is exempt until this is decided. | `objects-and-messages.md` |
| D12 | Errors | What `AO_ERROR()` does on a bug: a broken contract, an impossible event, or a queue, store or pool that fills. In development it always stops where the bug happened. In production, either it records the fault where it survives a restart, puts the outputs in a safe state and restarts; or it records the fault and returns, so that the fallback written after the call runs and the product keeps working. Rare but legitimate situations are not errors: they become states and events (`handlers.md`). | Record, make safe and restart. | `handlers.md`, `kernel.md` |
| D13 | Objects and hiding | One object per `.c` file with `static` state, or an object type with several instances whose handler receives a `self` pointer. Also how the internals are kept out of reach. | One object per `.c` file. Peers see only an incomplete type. | `objects-and-messages.md`, `kernel.md` |
| D14 | Ticks and sleep | The tick period and tick type. How deeply idle sleeps. What wakes it, either a periodic tick or a hardware timer set for the next due timer. | None. Ask with the power budget at hand. | `timers.md`, `kernel.md` |
| D15 | Interrupt levels | The kernel's critical sections mask every interrupt, or only those up to a set level. Faster interrupts above that level keep running and must not post. | Mask every interrupt. | `handlers.md`, `kernel.md` |
| D16 | Diagrams | Where the PlantUML files live. Whether the project's documents also keep ASCII diagrams, each with a PlantUML counterpart that changes with it; a diagram there is a picture of boxes, arrows, states or timelines, not a formula or a list. | A `uml/` folder beside the sources, without ASCII copies. | `diagrams.md` |

D5 is not a decision: a full queue, store or pool is a bug, like a stack
overflow (`kernel.md`). D6 sizes each one so that it never fills, and D12
sets what happens if one fills anyway.
