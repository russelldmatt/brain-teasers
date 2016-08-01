---
layout: solution
title:  "Two envelopes problem revisited"
category: brain-teaser
tags: solution

---

It's so simple (yet incredibly hard).  Pick a number, x, from a distribution that covers all real numbers (e.g. a normal distribution).  If the amount of money in your envelope is less than x, switch.  Otherwise don't switch.

As long as there is some probability that x > "amount in smaller envelope" and x <= "amount in larger envelope" then there is some chance you decide to switch at exactly the right time.  Since the amounts in both envelopes aren't the same, and a normal has positive probability for all x, then sampling from a normal distribution satisfies this constraint.

Slightly more rigorously, consider all cases:

- x <= both envelopes

You don't switch with either envelope.  P(you end up with larger envelope) = P(you were initially handed larger evelope) = 50%.

- x > both envelopes

You switch with either envelope.  P(you end up with larger envelope) = P(you were initially handed smaller evelope) = 50%.

- Else (x > smaller envelope and x <= larger envelope)

You switch only with smaller envelope.  You end up with larger envelope 100% of the time.

So, as long as there is some probability you end up in the third case, the P(ending up with larger envelope) > 50%.

