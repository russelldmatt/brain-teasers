---
layout: solution
title:  "NBA Finals"
category: brain-teaser
tags: solution

---

Break the problem up into mutually exclusive outcomes:

- Warriors win in 4 games
- Warriors win in 5 games
- Warriors win in 6 games
- Warriors win in 7 games

What's the probability that Warriors win in 4 games?  That's easy, it's just $$0.6^4$$.

What's the probability that Warriors win in 5 games?  Any given 5 game streak, such as WWLWW is equally probable, with $$P = 0.6^4 0.4^1$$.  How many streaks are there?  The one loss can be anywhere in the first 4 games, so 4.  But more generally, $${4 \choose 1} = 4$$.  So the probability that the warriors win in 5 games is $${4 \choose 1} 0.6^4 0.6^1$$.

What's the probability that Warriors win in 6 games?  Similar to above, the two losses can come in any of the first 5 games, and each 6-game winning streak is equally likely: $${5 \choose 2} 0.6^4 0.4^2$$.

You might detect a pattern, but there's only one last case: $${6 \choose 3} 0.6^4 0.6^3$$.

Putting it all together, let's call $$L$$ the number of losses and $$T$$ the total number of games:

$$
T = L + 4 \\
\sum_{L=0}^{3} {T - 1 \choose L} 0.6^4 0.4^L \\
\sum_{L=0}^{3} {L + 3 \choose L} 0.6^4 0.4^L \\
\approx 0.71
$$


