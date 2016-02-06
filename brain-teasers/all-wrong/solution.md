---
layout: solution
title:  "All wrong"
category: brain-teaser
tags: solution

---

Total number of ways to arrange 8 balls?  $$8!$$

Total number of ways that I can arrange the balls s.t. ball #1 is in box #1? $$7!$$

Total number of ways that I can arrange the balls s.t. ball #2 is in box #2? $$7!$$

Etc..

So the total number of ways we can arrange balls s.t. no ball is in the correct box?

$$
8! - 8 \cdot 7!
$$

But wait, what about any ordering where both ball #1 and ball #2 are in the correct place.  We over substracted those orderings, once for when ball #1 is in the right spot and once for when ball #2 was in the right spot.  So, for any pair of balls, let's add back the number of ways that pair of balls can both be in the right spot:

$$
8! - 8 \cdot 7! + {8 \choose 2} 6!
$$

But wait, what about any ordering where balls #1, #2, and #3 are the the correct place?  First, I subtracted them 3 times, then I added them back $${3 \choose 2} = 3$$ times, so we have to subtrace one again.  And we have to do that for every triple of balls.

$$
8! - 8 \cdot 7! + {8 \choose 2} 6! - {8 \choose 3} 5! 
$$

You can see where this is going.  Number of ways we can arrange the balls s.t. no ball is in the correct place:

$$
\sum_{x=0}^8 (-1)^x {8 \choose x} (8-x)!
$$

So the probability I randomly arrange the balls s.t. no ball is in the same numbered box?

$$
\frac{\sum_{x=0}^8 (-1)^x {8 \choose x} (8-x)!}{8!}
$$





