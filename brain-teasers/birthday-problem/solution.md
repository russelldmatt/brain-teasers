---
layout: solution
title:  "Birthday Problem"
category: brain-teaser
tags: solution

---

More on this <a href=https://en.wikipedia.org/wiki/Birthday_problem>here</a>.

Let's build up incrementally.  The first person has a birthday on some random day.  What's the chance that the second person has the same birthday as the first?

$$1 / 365$$

Let's say he doesn't share the same birthday as the first ($$P = 1-1/365$$), what's chance that the third person shares a birthday with one of the first two people?

$$2/365$$

To generalize, the chance that the (n+1)th person shares a birthday with first n people, assuming the first n people all have different birthdays, is

$$n/365$$

Now to flip it around, the probability that no one shares a birthday out of n people:

$$
(1-1/365) (1-2/365) (1-3/365)...(1-(n-1)/365) \\
\prod_{i=1}^{n-1} 1-i/365
$$

So the probability that at least one two people share a birthday out of n people:

$$ P = 1 - \prod_{i=1}^{n-1} 1-i/365 $$

Now, just find the smallest $$n$$ s.t. $$P > 0.5$$.  For this, I just use a computer and find that when $$n = 23$$, $$P \approx 0.507$$.





