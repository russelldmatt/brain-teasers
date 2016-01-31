---
layout: solution
title:  "The Cliff"
category: brain-teaser
tags: solution

---

Let's call $$X$$ the probability that he dies (when one foot from the edge).  The crucial realization is that the probability he dies when he is two feet from the edge is $$X^2$$. This is because we can restate $$X$$ as the probability that he ever gets one foot closer to the edge of the cliff (than where he is now).  In order to die from two feet away, you have to get one foot closer to the edge, twice.

With that, we can solve this with one equation:

$$
X = \frac{1 + X^3}{2} \\
X^3 - 2X + 1 = 0 \\
X = \frac{\sqrt{5} - 1}{2} \approx 0.62
$$
