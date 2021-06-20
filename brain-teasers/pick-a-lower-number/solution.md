---
layout: solution
title:  "Pick a lower number"
category: brain-teaser
tags: solution

---

We can answer this question in two ways, first as a math problem (ignoring any real world considerations) and then as a real world question (i.e. how much would you *really* pay)?

### As a math question

We don't know what distribution we're working with.  This is actually a huge hint, in the sense that we know we'll get the same answer for any distribution (otherwise, this question wouldn't have a single answer).  So an effective approach would be to just pick some distribution that makes the math easy and assume it will give the right answer, but we'll try to be more rigorous here.  So we will consider discrete and continuous distributions separately.

The discrete distribution is actually pretty easy.  There is some lowest number in the distribution, and there is some non-zero chance you pick it.  If you do, then I can *never* pick a lower number, meaning it will take me infinity picks and I will pay you infinity dollars.  Any non-zero probability of winning infinity dollars is still worth inifinity dollars.  So this is worth infinity in the discrete case.

The continuous case has the same answer, but it's less obvious.  The major insight is that we don't care what the probability distribution is, we only care about the CDF (cumulative distribution function).  A cumulative distribution function ranges from 0 to 1 and tells you the probability that you pick a number <= x.  As an example, $$cdf(7) = 0.25$$ means there is a 25% chance you pick a number less than 7.  Another property of the $$cdf$$ is that it produces a number *uniformly* between 0 and 1.

Let's say you pick a number $$x$$ and $$cdf(x) = 0.2$$.  How many tries, on average, will it take for me to pick a number lower than it?  If each pick I have a 20% chance of getting a number lower (by the definition of cdf), then it will take 5 tries, on average.  In general, if $$cdf(x) = y$$ it will take me $$1/y$$ tries to pick a lower number.

Now we just integrate.  I'm going to integrate over $$y$$ (the $$cdf(x)$$), not $$x$$ because I know that $$y$$ is uniformly distributed between 0 and 1, regardless of the distribution of $$x$$.

$$
\int_{0}^{1} \frac{1}{y} dy = \infty
$$

Infinity dollars!  How could it be?  It really seems like this game is not worth infinity dollars.

Here's a rough intuition why this integral does not converge.

- There is a 10% chance that the $$cdf(x)$$ is <= 0.1.  And if it is, the expected payout of the game is $10.  0.1 * $10 = 1.
- There is a 1% chance that the $$cdf(x)$$ is <= 0.01, and if it is, the expected payout of the game is $100.  0.01 * $100 = 1.
- There is a 0.1% chance that the $$cdf(x)$$ is <= 0.001, and if it is, the expected payout of the game is $1000.  0.001 * $1000 = 1.
- etc. 

So, because the payout increases as fast as the probability of that payout decreases, each term of this integral is a constant.  Taking the integral is like summing up a constant infinity times.  This is like a continuous analogue to the [St. Petersburg Paradox](https://en.wikipedia.org/wiki/St._Petersburg_paradox)

### How much would you really pay, though?

There are many ways to take realistic considerations into account, but I'll pick a very simple one.

Assume that if the payout is more than $100,000 I won't be able to pay you.  I'll just pay you the minimum of $100,000 and whatever the number of rolls really was.  In that case:

$$
\int_{0}^{1} \min(100000, \frac{1}{y}) dy \approx 12.5
$$

So, $12.5 is a much more realistic price for this game.  Other real world considerations would probably take the price down even further.


