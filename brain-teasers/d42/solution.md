---
layout: solution
title:  "d42"
category: brain-teaser
tags: solution

---

I really like this problem because it's possible to make a lot of incremental progress without necessarily finding the optimal solution.  As opposed to just stating the optimal solution up front, let's follow one possible path of insights that will lead to the final solution.

One thing to realize is that when you roll two dice, one with $$x$$ sides and one with $$y$$ sides, there are $$x \cdot y$$ possible outcomes and they are all equally likely.  So, if we could find two dice that multiply to 42, that would solve our problem in 2 rolls.

Of course we won't be able to find that because 42's prime factorization is 2 * 3 * 7, so there are no two primes that multiply to 42.  However, there are three (2, 3, and 7), and we can extend our logic about two dice to 3 in the obvious way.  So, by rolling a d2, a d3, and a d7, we have 2 * 3 * 7 = 42 possible outcomes that are all equally likely.  This solved the problem is 3 rolls... but can we do better?

Another insight is to realize that the two die rolls don't need to multiply to exactly 42.  If their product is larger than 42, you can adopt the strategy: "If the product is <= 42, keep the result, otherwise try again".

In this vein, we want to find 2 primes that multiply to something larger than, but close to 42.  How about 2 and 23.  We can roll a 2 and a 23, which gives us 46 possible outcomes.  If we get any of the first 42, that will be our d42 die roll, otherwise we try again.  The expected number of die rolls for this strategy is $$\frac{2}{42/64}$$ which is actually slightly *over* 3.  So a bit worse than our previous try.

However, with a tweak it can become much better.  Ideally we would love to roll a d21 and a d2 to get exactly 42 outcomes.  But we're forced to use a d23 and a d2 instead.  However, we can partition the 23 outcome in a d23 into 21 outcomes and 2 outcomes, giving us something very close to a d21 and a d2.  We roll a d23.  If the result is <= 21, then we roll a d2 to get 42 possible outcomes.  If the d23 roll is either a 22 or a 23, *we treat that as a d2*.  Now we need a d21, which we don't have exactly, but we can simulate by rolling a d23 repeatedly until the result is <= 21.  The expected number of outcomes in this strategy is

$$
x = \frac{21}{23} (2) + \frac{2}{23} (\frac{2}{21/23}) \\
x \approx 2.01
$$

However, with a tweak it can become much better.  The product of our two dice doesn't have to be slightly greater than 42, it can be slightly greater than any multiple of 42.  If we roll two d41, there are 1681 possible outcomes.  1680 is divisible by 42 (40 * 42), so we can break it up into 42 equal sections (e.g. 1-40 maps to 1, 41-80 maps to 2, etc.).  The only time that we will need to repeat our strategy is if we roll a 41 and a 41 (outcome number 1681).  The expected number of rolls for this strategy takes is

$$
x = 2 + \frac{1}{1681} x \\
x \approx 2.001
$$

But can we do even better?

Actually yes.  The last insight is that we can roll a die and partition the outcomes into $$n$$ groups, of different sizes.  If, for each group of size $$n_i$$, we can find a corresponding prime that multiplies with $$n_i$$ to equal 42, we can simulate the d42 in exactly 2 rolls.

You can't find a prime die that can be split into 2 groups that has this property, but a d41 has this property when split into 3 groups of size 6, 14, and 21.  So, the optimal strategy is as follows:

- Roll a d41.
- If the outcome is between 1-6, roll a d7, giving 42 possible outcomes.
- If the outcome is between 7-20 (14 possibilities), roll a d3, giving 42 possible outcomes.
- If the outcome is between 21-41 (21 possibilities), roll a d2, giving 42 possible outcomes.

By splitting a d42 in this way, you can *always* construct 42 equally probably outcomes, which simulates a d42 in **exactly 2 rolls**.


