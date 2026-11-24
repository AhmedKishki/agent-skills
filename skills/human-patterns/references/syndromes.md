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

1. Find every reference: *it, its, they, them, their, he, she, this, that, these, those*, and *which* after a comma. A *this* or *that* that opens a sentence with no noun after it is a strong signal.
2. List the candidates: every noun phrase in the same sentence and the one before it that agrees with the reference in number, and the referent the writer means.
3. Replace the reference with each candidate. The reference is vague if more than one candidate makes sense, or if the referent the writer means is not a noun in the text.

Replace a vague reference with the noun it means. If the text has no such noun, name the thing.
