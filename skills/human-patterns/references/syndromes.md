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
