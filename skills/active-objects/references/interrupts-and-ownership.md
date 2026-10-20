# Interrupts and ownership

## Interrupts

The implementation must:

- In an interrupt, only capture data, set flags or post events. A handler
  does the work.
- Record any exception explicitly, with its reason. For example, an
  interrupt that generates a waveform may drive its output directly, because
  the waveform must not depend on how long a handler runs.
- Let interrupts and handlers post alike. Posting protects the queue against
  interrupts and afterwards restores the interrupt state it found, so the
  same operation is safe in both contexts.
- Access data shared with an interrupt so that the compiler keeps every
  access and an interrupt never sees a half-made change: change it in one
  indivisible step or with interrupts held off.
- Change a hardware register shared between owners with a single write that
  affects only the intended bits, never with a read-modify-write that an
  interrupt can split.

The implementation must not:

- Put application decisions or state transitions in an interrupt.
- Re-enable interrupts unconditionally after protecting a shared change.
  Restore the state that was found instead.

Handlers never overlap, but interrupts can still preempt them. Data shared
with an interrupt needs protection even though handlers need none between
themselves. Calling into the framework from an interrupt costs time on every
occurrence; measure it against the interrupt's timing budget.

## Ownership

- Every peripheral, pin, register and mutable variable has one owning
  object. The owner configures and drives it; others ask through messages.
- Hardware stays with its owner. There is no central module that drives
  every pin, because only a pin's owner knows what its level means.
- An object that needs another owner's hardware in a certain state, such as
  outputs dark during a measurement, synchronises with that owner through a
  signal. It never writes that hardware itself.
- A register that holds settings of several owners gets one explicit owner
  as soon as a second object needs it.
- Only the dispatcher puts the processor to sleep, and it owns the sleep
  control.
