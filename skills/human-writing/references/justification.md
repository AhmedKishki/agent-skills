# Justification, worked through

## A weak part

Part: why dashboard prices are stale. Purpose: give the cause.

> Caching is an important part of modern systems. The cache keeps each price for 60 seconds, and the dashboard is built with React. This is not a pricing bug. It is also a caching issue. Understanding this is key to fixing the problem.

```
Part: Stale prices: give the cause of the stale prices
S1 "Caching is an important..."
  does: nothing for the part. It makes a general claim about systems.
  back: opens the part, which asks about these prices.
  next: S2 does not use it.
  verdict: cut
S2 "The cache keeps each price..."
  does: premise for the cause, but no sentence draws the cause from it.
  back: nothing once S1 is cut.
  next: S3 ignores the 60 seconds.
  joins: "and" only sets the framework beside the cache time. The framework has nothing to do with the age of a price.
  verdict: split. Cut the React claim. Repair the cache claim: add how often prices change and the consequence.
S3 "This is not a pricing bug."
  does: rejects a cause nobody proposed.
  confusable: nothing in the part points to the pricing service.
  verdict: repair: name what makes the pricing service look guilty, or cut.
S4 "It is also a caching issue."
  does: puts a label on S2.
  back: "also" adds without relating. S3 named no cause, so there is nothing to add to.
  verdict: cut. The repaired S2 carries the cause.
S5 "Understanding this is key..."
  does: announces importance.
  next: closes the part and adds nothing.
  verdict: cut
```

## The revision

> The wrong prices look like a pricing-service bug, since they arrive through its API, but they come from the cache in front of it. The cache keeps each price for 60 seconds while prices change every 10 seconds, so a price on the dashboard can be 50 seconds old.

```
Part: Stale prices: give the cause of the stale prices
S1 "The wrong prices look like..."
  does: names the cause and clears the obvious suspect.
  back: opens the part with the symptom the reader has seen.
  next: S2 shows how the cache produces the symptom.
  joins: "since" gives the reason the pricing service looks guilty. "But" sets the real cause against it.
  confusable: both causes deliver wrong values through the same API.
  verdict: keep
S2 "The cache keeps each price..."
  does: gives the mechanism and the size of the delay.
  back: explains S1's claim that the cache is the source.
  next: closes the part. A following part can take up the fix.
  joins: "while" sets the two rates against each other. "So" draws the age of the price from them.
  verdict: keep
```

## A negation in argument

"Profit is not theft" passes rule 5 only in a part where a reader could take profit for theft. The confusable feature is that both leave workers with less than they produced. The next sentence must then give the difference: the capitalist pays labour-power at its value and still gains, because labour produces more value than labour-power costs. Without that sentence the negation does no work and is cut.
