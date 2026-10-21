# Handlers, interrupts and other contexts

## Handlers run to completion

A handler that waits holds up every event queued behind it, and anything it
read before waiting may be out of date when it resumes.

- Handle one event and return. To wait, start the object's timer, or return
  and handle the next event when it arrives.
- Never block. Every RTOS call in a handler uses a zero timeout (`0` or
  `K_NO_WAIT`). That rules out `vTaskDelay`, `k_sleep`, `xSemaphoreTake`,
  `k_mutex_lock` and any receive that waits. A loop that waits for a flag or
  a register blocks too.
- Many driver and stack calls block, for example Zephyr's `i2c_transfer`,
  `spi_transceive` and `adc_read`. Use their asynchronous or callback forms,
  and post the completion as an event.
- A short busy-wait with a fixed bound, such as one ADC conversion, is
  allowed only if it is shorter than every deadline, including its failure
  path. Record it with the decisions.
- Never save a position inside the function. Protothreads, `switch`-based
  coroutine macros, `setjmp`/`longjmp` and private stacks all do this. The
  object's state records its progress.
- Keep values that later events need in the object's state. Use local
  variables only within the current call.
- Never keep a pointer to the event. To keep an event for later, defer it
  (`state-machines.md`).
- Never call a handler directly, including the object's own. Only the kernel
  calls handlers. To continue later, post to the object's own queue or start
  its timer.
- Keep handlers short. The longest handler sets how fast the system can
  respond, and its worst-case time is measured under D2 (`decisions.md`).
- Check before changing anything, so that a handler never leaves its object
  half-changed. Expected problems become states or events. Real errors are
  handled as decided in D12.

## Interrupts, callbacks and other threads

These rules apply to every context outside an object's handler: interrupt
handlers, RTOS timer callbacks, library callbacks such as a BLE stack's, and
any other thread.

- Code in these contexts only captures data and posts an event. It stores
  the captured data in memory that the receiving object owns, and the
  handler does the work.
- Every exception needs approval and a recorded reason. For example, a
  waveform interrupt may set its own output pins, because the waveform
  cannot wait for a handler.
- Posting must be safe from every context that posts. Code that disables
  interrupts saves the interrupt state first and restores it afterwards. It
  never simply re-enables interrupts, because the caller may have had them
  disabled. On an RTOS, interrupts use the queue calls made for interrupts
  (`kernel.md`, Mapping).
- An interrupt that posts runs at a level that the kernel's critical
  sections mask (D15). On FreeRTOS, that level is at or below
  `configMAX_SYSCALL_INTERRUPT_PRIORITY`. On Zephyr, a zero-latency
  interrupt must not post.
- Posting never blocks the poster. A failed post is handled as decided in
  D5.
- Data shared between an interrupt and its own object's handler is
  `volatile`, and the handler accesses it with interrupts disabled. Between
  threads, pass data by posting. Where posting is impossible, use C11 atomics
  or an approved priority-ceiling section (`objects-and-messages.md`,
  Ownership). A blocking mutex is never allowed. `volatile` on its own does
  not synchronise threads.
- When an object's handler and its own interrupt both touch a hardware
  register, change the register in one of two ways: with one write that
  affects only the intended bits, as a set/clear register allows, or with a
  read-modify-write done with interrupts disabled. An interrupt must never be
  able to split the change.
