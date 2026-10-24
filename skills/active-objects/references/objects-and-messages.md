# Objects, events and messages

## Objects

- Give each responsibility its own object. The object owns its state, the values it keeps and the resources it drives.
- No other module can reach the object's state, kept values or handler (D13, see `decisions.md`). Peers get a handle they can post to and nothing more.

## Events and signals

- An event is a signal, which names what happened, plus agreed data. The project chooses their types and size (D3).
- Name the event itself. `DOOR_OPENED` and `DOOR_CLOSED` are two signals. A single signal with a 0 or 1 value would make the receiver decode which event happened. The signal alone tells the receiver what the data means.
- One `enum` lists every signal. A comment beside each signal names its senders, its receivers and the meaning of its data.
- Signals are too fine when several of them are always handled alike. They are too coarse when handlers keep inspecting the data to tell cases apart.
- A posted event is read-only. The receiver may use it only during the handler call, and copies whatever it needs to keep.
- Post an event only when some receiver acts on it. When a value has not changed, do not post it again. A PWM duty cycle is state, and a change of duty cycle is an event. The PWM edges are not events, because nothing acts on them.
- Record a state only once the change has really happened. Until then, a request must never be reported as done.
- Events inside the program carry no wire format, so they have no protocol tags, byte layouts or checksums. A protocol module converts at the edge of the system and takes part through ordinary events.
- With pooled events (D3), the sender never touches an event after posting it. The sender gives back any event it took from the pool and never posted.

## Messages between objects

- Every message has an agreement, approved by the user before the message is built. The agreement covers the meaning, the signal and data, how the receiver gets the starting value, how order and freshness work, and how many of its events can wait in the receiver's queue (D6). Payload layout, retries, acknowledgements and keeping only the newest event also belong to the agreement.
- The sender is in charge of the value, and the receiver keeps its own copy. The sender posts the value itself at start-up and after each change that a receiver needs. Never send only "it changed, go and read it", because that sends the receiver back into the sender's data.
- Add no getters or setters between objects, including read-only ones. Add no shared-state module and no globals that alias an object's data.
- Never wait for a reply. A request and its reply are two events, and the reply is handled when it arrives.

## Queues as the objects see them

- Each object has one queue. Anyone may post to it, and only the kernel takes events out.
- Events leave the queue in the order they arrived. The one exception is a deferred event put back at the front (`state-machines.md`).
- Each queue has its own fixed size (D6), large enough that it never fills. A full queue is a bug, like a stack overflow, and the post reports it (`kernel.md`, D12).
- Size a queue from its producers: the most events they can post to it while its object waits to run. An argument from priority, such as "the receiver always runs before the sender posts again", holds only while D1 and D2 stay as they are. It must also count posts from interrupts and several posts within one handler.
- Keeping only the newest of several events is a choice the receiver makes in its own state. The kernel offers no such feature.

## Ownership and sharing

- Each resource (peripheral, pin, register, buffer) and each changing value has one owning module. The owner sets the resource up and drives it. Other modules ask the owner by message.
- The project has no central GPIO module, because only a pin's owner knows what its level means. A module that needs another owner's resource in a certain condition, such as outputs dark during a measurement, asks the owner with a signal. It never writes the resource itself.
- A register that holds settings for several peripherals gets one owner as soon as a second module needs it.
- When several objects need one resource, one object owns it and serves the others' requests as events.
- Objects need no locks between them because they share nothing, and that reason holds on every kernel. On RTOS threads, one object's handler can preempt another's, so anything two objects both touch breaks this section.
- The kernel's own structures and the boundary modules of D11 are the only shared code. Each of them is protected, and the protection is recorded. Calling a module a driver or a helper gives it no exemption.
- Under RTOS threads, a resource that several objects must use may be guarded by a short, bounded priority-ceiling section. The section either locks the scheduler or raises the holder to the highest priority among the users, so no user ever waits for it. The section makes no RTOS calls and needs an approved exception. A blocking mutex between objects is never allowed.
