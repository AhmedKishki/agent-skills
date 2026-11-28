# Syndromes

AI writing is characterised by being both too verbose and yet too vague.

## Placeholder *something*

Example:

> The C++ Core Guidelines use the keyword to tell the reader something: `class` if the type has an invariant

Correction:

> The C++ Core Guidelines use the keyword `class` to tell the reader that the type has an invariant.

If *something* refers to a concrete object, drop *something* and mention the object directly.

## Vague reference

Example:

> A constructor is the only way to make an object, and it runs in a fixed order.

Correction:

> A constructor is the only way to make an object. C++ constructs an object in a fixed order.

A reference (*it, this, they, which* and the like) is vague if more than one noun in the sentence can take its place, or if its referent is not in the sentence. A vague reference must be replaced with the noun it refers to.

## Announced number of things

Example:

> In Python, `x = value` always does one thing: it binds the name `x` to an object.

Correction:

> In Python, `x = value` always binds the name `x` to an object.

If a sentence announces how many things it will give, as *does one thing:* does, and the number is irrelevant, drop the announcement and give the things directly.

## Vague emphasis

Example:

> C++ has two operations that both use `=`, and each runs different code.

Correction:

> C++ has two operations that both use `=`.

If a clause joined by *and* says nothing that the rest of the sentence does not already imply, drop it.

## Forced narration

Example:

> One model is checked against three devices.

Correction:

> The model is yolo11n. The devices are this laptop, the NXP i.MX 8M Plus and a phone NPU.

If a sentence narrates what the text does instead of stating its content, it is vague and uninformative. Drop the narration and state the content directly: which model, which devices.

## Unintroduced reference

Example:

> The other direction fails too. A property of the model does not carry over to a device that has no hardware for it.

Correction:

> A layer with INT8 weights runs no faster than in FP32 on a device without INT8 hardware.

If a sentence refers to something the text has not introduced, as *the other direction* does, the reader cannot tell what it refers to. State directly what fails.

## Overloaded sentence

Example:

> This laptop's caches hold 52 MiB and the largest layer of yolo11n moves 11.5 MB, so the count above overstates the traffic to memory and the CPU verdict holds all the more.

> This laptop's caches hold 52 MiB and the largest layer of yolo11n moves 11.5 MB, so the real traffic to memory is lower than counted, the real I higher, and the CPU stays compute-bound.

Correction:

> The count above assumes that every layer reads its input and weights from memory and writes its output back. This laptop's caches hold 52 MiB, more than the 11.5 MB of yolo11n's largest layer, so a layer's output can stay in the cache for the next layer. Then fewer bytes travel to memory than counted, so yolo11n does more than the counted 37.3 operations per byte. Any model above 15.6 operations per byte is compute-bound on this CPU, so yolo11n stays compute-bound.

If one sentence attempts to say too much, the reader cannot tell what to get out of it, and it reads as a sequence of words that do not mean much. Split it into one step per sentence, and end with what the reader should get out of it.

## Noun/verb mismatch

Example:

> attributes, shapes and the tool's own limits decide

> the nodes' attributes and input shapes also decide

Correction:

> the provider checks the nodes' attributes and input shapes

If the subject cannot perform the verb, as attributes cannot *decide*, name the actor that does and give it a verb it can perform.

## Sequence squeezed into a preposition

Example:

> the network takes 18.9 ms between 1.1 ms of preprocessing and 0.5 ms of postprocessing

Correction:

> preprocessing takes 1.1 ms, the network 18.9 ms and postprocessing 0.5 ms

If a preposition (*between, after, around*) packs a sequence of steps into one phrase, list the steps in order.

## Undefined symbol

Example:

> the real traffic to memory is lower than counted, the real I higher

Correction:

> fewer bytes travel to memory than counted, so yolo11n does more than the counted 37.3 operations per byte

If the text uses a symbol, as *I* here, that the reader cannot resolve where it stands, the reader cannot tell what it is. Write out what the symbol stands for.
