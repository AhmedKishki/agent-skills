# Syndromes

A syndrome is a wording habit that marks prose as AI-written. Each entry describes the habit, quotes a real case, explains why a human would write it differently, and gives the check and the fix where they are known.

## S1 The placeholder *something*

*Something* fills a subject or object slot, and the sentence then fills the same slot again, after a colon, with what *something* stands for.

> The C++ Core Guidelines use the keyword to tell the reader something: `class` if the type has an invariant, `struct` if "the data members can vary independently" [8, C.2].

**Why it marks AI.** *Something* and the text after the colon are both the object of *tell*. *Something* adds nothing, since *tell* already says that the reader learns a thing. The reader asks what that thing is, so a human writer names it at once.

**Likely cause.** The writer does not see that a phrase can itself be the subject or object of a verb, so it puts a noun in the slot and attaches the phrase after a colon.

**Check.** Does *something* refer to a concrete thing that the sentence names after it?

**Fix.** Drop *something* and put that thing in its slot.

> The C++ Core Guidelines use the keyword to tell the reader `class` if the type has an invariant, `struct` if "the data members can vary independently" [8, C.2].
