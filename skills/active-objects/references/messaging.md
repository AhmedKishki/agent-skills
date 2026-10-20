# Messaging

## Queue-only communication

The implementation must:

- Pass every piece of information between objects as an event, posted into
  the receiver's queue through the framework's one posting operation.
- Make each message complete: its signal and data carry everything the
  receiver needs in order to act.
- Let a receiver keep its own copy of what it received. The producer remains
  the authority for that state.

The implementation must not:

- Add getters or setters between objects. A read-only getter is still a
  bypass.
- Call another object's handler, read its variables, hand out references to
  its state, or alias that state through shared globals.
- Send a notification that sends the receiver back to the producer for the
  data ("the mode changed; go and read it").
- Replace getters with a central shared-state module. It is the same back
  door under another name.
- Expose an object's handler, queue, timers or private state to peers. A
  public handle names a destination and nothing else.
- Start, stop or inspect another object's timers.

Services that are not active objects, such as drivers, the clock or pure
utilities, need an explicit boundary decision. Calling a function a driver or
a utility does not exempt it from these rules.

## State and events

- State is persistent: its owner holds it and keeps applying it until it
  changes. Persistent does not mean stored in non-volatile memory.
- An event is transitory: it is consumed by its designated consumers, not
  necessarily by every object.
- A request is not proof of an applied state. The owner records a state when
  it has actually applied the change, and nothing reports a request as an
  applied result before then.
- A state change becomes an event only where a consumer needs it. Post an
  event only when a consumer acts on it.
- Model the states and events the current work needs, not every physical
  transition. An output's level is state and a change of level is an event;
  the individual pulses are not events when nothing consumes them.
- The signal names the event itself: "door opened" and "door closed" are two
  signals, not one signal with an on/off value. Data accompanies a signal
  only where the receiver needs a quantity, such as a duration or a sample.
- One central list defines every signal with its producers, its consumers and
  the meaning of its data. One event may go to several objects under the same
  signal, and one signal may have several producers.
- Internal events carry no external wire protocol: no protocol framing, byte
  layouts or checksums. The protocol's owner converts at the border and takes
  part through ordinary events, not through a privileged path.

## Message contracts

Agree each message before implementing it:

- **Meaning:** what happened, and which object is the authority for it.
- **Signal and data:** what the receiver needs in order to act, and nothing
  more.
- **Initial state:** how a receiver learns the current state at startup,
  typically because the owner posts it on its start event. A receiver never
  reads the owner's internals to seed itself.
- **Ordering and freshness:** what the receiver does while its retained copy
  lags the producer, and how repeated or late messages are treated.
- **Full queue:** what happens when the receiver's queue cannot take the
  message (next section).

Do not choose a payload layout, retry, acknowledgement or coalescing policy
without agreement.

## Full queues

- Queues are bounded. The framework defines what posting to a full queue
  does, for example that it drops the new event, and the code base documents
  it.
- A silent drop is not an acceptable way to lose state. For each state
  message, show why the receiver's queue cannot be full, or agree a recovery,
  such as the owner republishing its state periodically while receivers treat
  a repeated state as nothing new.
- An argument based on priority order (every receiver ranks above the
  producer, so their queues are empty when it posts) holds only while that
  order stays. Record the dependency next to the order.
- A lost timeout stops an activity that restarts its timer only on its
  timeout. Account for it.
- Coalescing (keeping only the newest) is the receiver's choice, made in its
  own state. It is not a framework feature.
