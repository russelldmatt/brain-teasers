---
layout: solution
title:  "Survival of the species"
category: brain-teaser
tags: solution

---

Let $$e$$ be the probability that the species goes extinct.  This is also the probability that one microorganism's family line goes extinct.

$$
e = (1-p) + pe^2
$$

There's a $$1-p$$ chance that the first organism does not multiply, in which case the species is extinct.  With probability $$p$$, the organism multiplies and there are now two microorganisms.  The probability that they both go extinct is simply $$e^2$$.

Solving for $$e$$ gives two solutions:

$$
e =
  \begin{cases}
    1 \\
    \frac{1 - p}{p}
  \end{cases}
$$

If $$p <= \frac{1}{2}$$, both solutions are $$>= 1$$, meaning that the species will definitely go extinct.  If $$p > \frac{1}{2}$$, the solution $$\frac{1 - p}{p}$$ gives values for $$e$$ that are $$< 1$$, meaning the species has a chance.

For a better explanation of how to know which solution for $$e$$ to choose based on the value of $$p$$, look [here](http://www.laurentlessard.com/bookproofs/microorganism-multiplication/).
