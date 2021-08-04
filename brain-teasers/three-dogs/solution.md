---
layout: solution
title:  "Three Dogs"
category: brain-teaser
tags: solution

---

The answer is 2/3.

The first step is to realize that all we're doing is computing the
probability that the first dog's bite is not in the middle of the
other two.

### The Elegant Approach

So what's the probability that the first dog's bite is in the middle?
Each dog bites randomly and so they all have an equal probability of
being the "middle bite".  There are three dogs, so the first dog has a
1/3 probability of being the middle bite.

That means there's a 2/3 chance that the first dog is not the middle
bite.  QED.

### The Integral Approach

Let's assume each dog's bite is uniformly randomly distributed.  We
can just integrate over all possibilities for where the first dog's
bite could be and then compute, for each of those possibilities, the
probability that the other two dog's bites are on the same side.

Let's say the first dog's bite was at 40% from bottom of the stick.
What's the chance that both other dogs bite below that?  $$0.4^2$$.
What's the chance that both other dogs bite above that?  $$0.6^2$$.

In general, if the first dog bits at position $$x$$, then the
probability that both other dogs bite below $$x$$ is $$x^2$$ and the
probability that both other dogs bite above $$x$$ is $$(1-x)^2$$.

Now we integrate:

$$
\int_0^1 x^2 + (1-x)^2 = \frac{2}{3}
$$
