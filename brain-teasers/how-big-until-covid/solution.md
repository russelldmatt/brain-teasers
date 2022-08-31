---
layout: solution
title:  "How big until covid?"
category: brain-teaser
tags: solution

---

Let's assume that each person has a 2% chance of having COVID and each
person's probability is independent of one another's.

We can set up an equation.  If the number of people attending the party is $$N$$, then the probability that none of them have COVID is $$0.98^N$$.  So the probability that someone *does* have COVID is $$1 - 0.98^N$$.  

$$
\begin{align*}
1 - 0.98 ^ N &= 0.5 \\
0.5 &= 0.98 ^ N \\
\frac{log(0.5)}{log(0.98)} &= N \\
34.3 &\approx N
\end{align*}
$$

So, you can invite 34 people to your party and still have less than a 50% chance that COVID is also attending!
