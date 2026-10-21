# Objects, events and messages

Read this when designing objects, events, signals, the messages between
objects, or who owns which resource. Everything here is a contract unless a
decision (D-number) is named; see `decisions.md`.

## Objects

- One object per responsibility. It owns its state, the values it keeps and
  the resources it drives.
- Its state, kept values and handler are out of reach of every other module
  (D13). Peers get only a handle they can post to.
- It is reached only by posting to its queue. Nothing calls its handler,
  reads its variables or takes a pointer to its data.
- Its behaviour is one state machine (`state-machines.md`).

## Events and signals

- An event is a signal, naming what happened, plus agreed data. Their types
  and size are chosen per project (D3).
- Name the event itself: `DOOR_OPENED` and `DOOR_CLOSED` are two signals,
  not one signal with a 0/1 value. The signal alone tells the receiver what
  the data means.
- One `enum` lists every signal. Beside each, a comment names its senders,
  its receivers and the meaning of its data. The kernel reserves a start
  signal and a timeout signal (one per timer when D7 allows several).
- Signals are too fine if several are always handled alike, and too coarse
  if handlers keep inspecting the data to tell cases apart.
- A posted event is read-only. The receiver may use it only during the
  handler call, and copies what it needs to keep.
- Post an event only when some receiver acts on it. Post a change, not a
  repeat of the same value. A PWM duty cycle is state and changing it is an
  event; the PWM edges are not events, because nothing acts on them.
- A request is not a result. Record a state only once the change has really
  happened, and never report a request as done before then.
- Events inside the program carry no wire format: no protocol tags, byte
  layouts or checksums. A protocol module converts at the edge and joins in
  through ordinary events.
- With pooled events (D3), the sender never touches an event after posting
  it, and gives back any event it took but did not post.

## Messages between objects

- Each message has an agreement, approved before it is built: its meaning,
  its signal and data, how the receiver gets the starting value, how order
  and freshness work, and what a full queue does (D5). Payload layout,
  retries, acknowledgements and keeping only the newest event belong to the
  agreement too.
- The sender is in charge of the value. The receiver keeps its own copy. The
  sender posts the value itself at start-up and after each change a
  receiver needs, never "it changed, go and read it".
- No getters or setters between objects, not even "read-only" ones. No
  shared-state module, and no globals that alias an object's data.
- Never wait for a reply. A request and its reply are two events; the reply
  is handled when it arrives.
- Never start, stop or inspect another object's timer.
- Delivery to a named object or to subscribers is D4.

## Queues, from the objects' side

- Each object has one queue. Anyone may post to it; only the kernel takes
  from it.
- Events come out in the order they went in. The one exception is a
  deferred event put back at the front (`state-machines.md`).
- A queue has a fixed size (D6). What a post to a full queue does is D5.
- Never accept a silent drop for a message that carries state. For each such
  message, show why the queue cannot be full, or agree a policy. An argument
  from priority ("the receiver always runs before the sender posts again")
  holds only while D1 and D2 stay as they are, and must count posts from
  interrupts and several posts in one handler.
- A post never blocks and never calls the receiver. How the kernel keeps
  this is in `kernel.md`.
- Keeping only the newest of several events is the receiver's choice, made
  in its own state. It is not a kernel feature.

## Ownership and sharing

- Each resource (peripheral, pin, register, buffer) and each changing value
  has one owning module. The owner sets it up and drives it; others ask by
  message.
- There is no central GPIO module: only a pin's owner knows what its level
  means. A module that needs another's resource in a certain condition (for
  example, outputs dark during a measurement) asks the owner by signal and
  never writes the resource itself.
- A register holding settings for several peripherals gets one owner as
  soon as a second module needs it.
- When several objects need one resource, one object owns it and serves the
  others' requests as events.
- Objects need no locks between them because they share nothing, not
  because they never run at the same time. On RTOS threads they do overlap,
  so anything two objects both touch breaks this section.
- The kernel's own structures and the boundary modules of D11 are the only
  shared code; each is protected and its protection recorded. Calling a
  module a driver or a helper does not exempt it.
- Under RTOS threads, a resource several objects must use may be guarded by
  a short, bounded priority-ceiling section: a scheduler lock, or raising
  the holder to the highest user's priority, so that no user waits. It makes
  no RTOS calls inside, and it is allowed only as an approved exception. A
  blocking mutex between objects is never allowed.
