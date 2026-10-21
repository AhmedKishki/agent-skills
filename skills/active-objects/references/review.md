# Review

Read this before finishing any change that touches the pattern, and when
reviewing code. When something fails, name the contract or decision, say
what goes wrong because of it, and propose a fix.

## Warning signs

If you catch yourself thinking one of these, stop.

| Thought | Instead | See |
|---|---|---|
| "I'll pick a sensible option and mention it later." | Put the decision to the user first. | `decisions.md` |
| "Just a small read-only getter." | It skips the queue and ties the reader to the owner's internals. Send an event. | `objects-and-messages.md` |
| "The receiver can read the value when notified." | It would see the value now, not what happened. Put the value in the event. | `objects-and-messages.md` |
| "A common module or a mutex makes sharing safe." | Sharing is the problem. Give the data one owner. | `objects-and-messages.md` |
| "A flag will do." | History that changes reactions is a state. | `state-machines.md` |
| "One more guard." | A growing guard chain is a missing state. | `state-machines.md` |
| "That event can't arrive in this state." | Decide its reaction anyway. | `state-machines.md` |
| "I'll change state in the entry action." | Use two transitions with opposite guards. | `state-machines.md` |
| "A short loop until the flag is set." | Start the timer and return. | `handlers.md` |
| "A quick `vTaskDelay` is harmless here." | It blocks every event behind it. Start the timer and return. | `handlers.md` |
| "This driver call only takes a moment." | If it can wait, it blocks. Use the asynchronous form and post the result. | `handlers.md` |
| "The interrupt has the data; it can do the work." | Capture and post. | `handlers.md` |
| "Calling the handler directly is simpler." | Only the kernel calls handlers. | `kernel.md` |
| "The timeout arrived, so the time is up." | It may be late. Check it as decided in D8. | `timers.md` |
| "The header shows the struct, so I can use it." | Seeing it is not permission to use it. | `objects-and-messages.md` |
| "The kernel could just let objects peek at each other." | The kernel keeps the same contracts as the objects. | `kernel.md` |
| "The existing code already does it." | Existing shortcuts are debt, not a pattern. | — |

## Conformance check

- [ ] Each object's internals are out of reach; peers get only a handle.
- [ ] Every interaction between objects is a posted event with an approved
      agreement.
- [ ] No handler blocks, waits on an RTOS call, saves a position or keeps an
      event pointer.
- [ ] Every state and signal pair has a deliberate reaction, no flag stands
      in for a state, and set-up and clean-up sit in entry and exit actions.
- [ ] Timers are started and stopped only by their own object, and late
      timeouts are recognised as decided in D8.
- [ ] Interrupts and callbacks only capture and post, at a level the kernel
      masks, and posting is safe and non-blocking.
- [ ] Every resource has one owner.
- [ ] Start-up follows `kernel.md`, Start-up and shutdown.
- [ ] Every decision this code relies on is approved and recorded, and every
      exception is approved, recorded and marked in the code.
- [ ] For kernel code, the checklist at the end of `kernel.md` passes.
- [ ] For a state machine, the checklist at the end of `state-machines.md`
      passes.
