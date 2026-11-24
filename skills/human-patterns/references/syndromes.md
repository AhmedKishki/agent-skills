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

A reference (*it, this, they, which* and the like) is vague if more than one noun in its sentence or the one before makes sense in its place, or if what it stands for is not a noun in the text.

Replace a vague reference with the noun it means. If the text has no such noun, name the thing.
