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
| "A quick delay call is harmless here." | The delay holds up every event queued behind the handler. Start the timer and return. | `handlers.md` |
| "This driver call only takes a moment." | A call that can wait blocks the handler. Use the asynchronous form and post the result. | `handlers.md` |
| "The interrupt already has the data, so it can do all the work." | Long work in an interrupt delays every handler and every lower interrupt. Do the short part on the interrupt's own data, post, and leave the rest to the handler. | `handlers.md` |
| "If the queue is full, the event is just dropped." | A full queue is a bug, like a stack overflow. Size the queue so it never fills. | `objects-and-messages.md` |
| "Calling the handler directly is simpler." | A handler called from another handler runs inside it, and a call from anywhere else breaks one-at-a-time delivery. Only the kernel calls handlers. | `kernel.md` |
| "I'll update the diagram once the code settles." | A diagram that lags the code describes software that does not exist. Change it in the same change. | `diagrams.md` |
| "The timeout arrived, so the time is up." | The timeout may be late. Check it as decided in D8. | `timers.md` |
| "The header shows the struct, so I can use its fields." | If C allows an access, that does not make it permitted. | `objects-and-messages.md` |
| "The kernel could let objects peek at each other." | The kernel follows the same contracts as the objects. | `kernel.md` |
| "The existing code already does it." | Existing breaks are debt to pay off. Never copy them. | every module |

## Conformance check

- [ ] The change keeps every rule of each module it touches, and every item
      of the "Never" list in `SKILL.md`.
- [ ] Every decision the code relies on is approved and recorded, and every
      exception is approved, recorded and marked in the code.
