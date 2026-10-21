# Review

Before finishing a change, check it against the red flags and the
conformance check. When a check fails, name the contract or decision involved, say what goes wrong
because of it, and propose a fix.

## Red flags

If you catch yourself thinking one of these, stop. Each one means the work
is about to break a contract or skip a decision.

| Thought | Reality | Module |
|---|---|---|
| "I'll pick a sensible option and mention it later." | The user makes project decisions. Ask before writing the code. | `decisions.md` |
| "Just a small read-only getter." | A getter ties the reader to the owner's internals and timing, and bypasses the queue's ordering. Send an event. | `objects-and-messages.md` |
| "The receiver can read the value when it is notified." | The receiver would read the value as it is now, which may differ from the value that changed. Put the value in the event. | `objects-and-messages.md` |
| "A common module or a mutex will make sharing safe." | Sharing is the problem, and both keep the data shared. Give the data one owner. | `objects-and-messages.md` |
| "A flag will do." | History that changes how the object reacts belongs in a state. | `state-machines.md` |
| "One more guard on this transition." | When the guards on one event in one state keep multiplying, the object is missing a state. | `state-machines.md` |
| "That event can't arrive in this state." | Choose its reaction anyway. | `state-machines.md` |
| "I'll change state in the entry action." | Entry actions never change state. Write two transitions with opposite guards. | `state-machines.md` |
| "A short loop until the flag is set." | The loop blocks the handler. Start the timer and return. | `handlers.md` |
| "A quick `vTaskDelay` is harmless here." | The delay holds up every event queued behind the handler. Start the timer and return. | `handlers.md` |
| "This driver call only takes a moment." | A call that can wait blocks the handler. Use the asynchronous form and post the result. | `handlers.md` |
| "The interrupt already has the data, so it can do the work." | Work in an interrupt lengthens interrupt latency and breaks run-to-completion reasoning. Capture the data and post. | `handlers.md` |
| "Calling the handler directly is simpler." | A handler called from another handler runs inside it, and a call from anywhere else breaks one-at-a-time delivery. Only the kernel calls handlers. | `kernel.md` |
| "The timeout arrived, so the time is up." | The timeout may be late. Check it as decided in D8. | `timers.md` |
| "The header shows the struct, so I can use its fields." | If C allows an access, that does not make it permitted. | `objects-and-messages.md` |
| "The kernel could let objects peek at each other." | The kernel follows the same contracts as the objects. | `kernel.md` |
| "The existing code already does it." | Existing breaks are debt to pay off. Never copy them. | every module |

## Conformance check

- [ ] Each object's internals are out of reach, and peers get only a handle.
- [ ] Every interaction between objects is a posted event with an approved
      agreement.
- [ ] No handler blocks, waits on an RTOS call, saves a position or keeps a
      pointer to an event.
- [ ] Every pair of state and signal has a chosen reaction, no flag stands in
      for a state, and set-up and clean-up sit in entry and exit actions.
- [ ] Timers are started and stopped only by their own object, and late
      timeouts are recognised as decided in D8.
- [ ] Interrupts and callbacks only capture data and post, at a level the
      kernel masks, and posting is safe and never blocks.
- [ ] Every resource has one owner.
- [ ] Start-up follows `kernel.md`, section Start-up and shutdown.
- [ ] Every decision the code relies on is approved and recorded, and every
      exception is approved, recorded and marked in the code.
- [ ] Kernel code passes the checklist at the end of `kernel.md`.
- [ ] Each state machine passes the checklist at the end of
      `state-machines.md`.
