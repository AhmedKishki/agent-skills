# Handlers, interrupts and other contexts

Read this when writing a handler, or any code that runs in an interrupt, a
callback or another thread. Everything here is a contract unless a decision
(D-number) is named; see `decisions.md`.

## Handlers run to completion

A handler that waits holds up every event behind it, and the world changes
while it is not looking.

- Handle one event and return. To wait, start the object's timer, or return
  and handle the next event when it comes.
- Never block. In a handler, every RTOS call uses a zero timeout (`0` or
  `K_NO_WAIT`): no `vTaskDelay`, `k_sleep`, `xSemaphoreTake`,
  `k_mutex_lock`, or waiting receive. No loop that waits for a flag or a
  register.
- Many driver and stack calls block, for example Zephyr's `i2c_transfer`,
  `spi_transceive` and `adc_read`. Use their asynchronous or callback forms,
  and post the completion as an event.
- A short, bounded busy-wait (such as one ADC conversion) is allowed only if
  it is shorter than every deadline, failure path included. Record it with
  the decisions.
- Never save a position inside the function: no protothreads, `switch`-based
  coroutine macros, `setjmp`/`longjmp` or private stacks. Progress lives in
  the state.
- Keep values needed later in the object's state. Use local variables only
  within the current call.
- Never keep a pointer to the event. To keep an event for later, defer it
  (`state-machines.md`).
- Never call a handler directly, not even the object's own. Only the kernel
  calls handlers. To continue later, post to your own queue or start your
  timer.
- Keep handlers short. The longest one limits how fast the system responds;
  its worst-case time is measured under D2.
- Never leave the object half-changed. Check before changing anything.
  Expected problems become states or events; real errors go to D12.

## Interrupts, callbacks and other threads

This covers every context that is not an object's handler: interrupt
handlers, RTOS timer callbacks, library callbacks such as a BLE stack's,
and any other thread.

- Only capture data and post an event there. Captured data goes into
  storage the receiving object owns. The handler does the work.
- Any exception is approved and recorded with its reason. For example, a
  waveform interrupt may set its own output pins because the waveform cannot
  wait for a handler.
- Posting is safe from every context that posts. Code that disables
  interrupts saves their state first and restores it afterwards. It never
  simply re-enables them, because the caller may have had them off. On an
  RTOS, interrupts use the queue calls made for them (`kernel.md`, Mapping).
- An interrupt that posts runs at a level the kernel's critical sections
  mask (D15). On FreeRTOS that is at or below
  `configMAX_SYSCALL_INTERRUPT_PRIORITY`; on Zephyr, not a zero-latency
  interrupt.
- Posting never blocks the poster. A failed post is handled as decided in
  D5.
- Data shared between an interrupt and its own object's handler is
  `volatile` and accessed with interrupts disabled. Between threads, pass
  data by posting. Where that is impossible, use C11 atomics or an approved
  priority-ceiling section (`objects-and-messages.md`, Ownership), never a
  blocking mutex. `volatile` alone does not synchronise threads.
- A hardware register that an object's handler and its own interrupt both
  touch is changed with one write that touches only the intended bits (a
  set/clear register), or with a read-modify-write done with interrupts
  disabled. It is never changed in a way an interrupt can split.
