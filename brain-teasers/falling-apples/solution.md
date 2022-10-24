---
layout: solution
title:  "Falling Apples"
category: brain-teaser
tags: solution

---

I *think* the answer is 833.

Assuming I'm right, the main insight is that you want the truck as
full of apples as possible at all times.  No matter how many apples
are in the truck, one will fall out per mile, so by having as many
apples in the truck as possible you have the best ratio of apples
moved to apples wasted.

The way I thought about it was that the truck would always move all
the apples one mile at a time.

To start, we have 3000 apples at mile 0.  The truck would then take 3
trips from mile 0 -> 1 and it would drops 3 apples doing so.

Now we have 997 apples all at mile 1.  The truck again takes 3 trips
from mile 1 -> 2 and drops another 3 apples.

Carry this on until you've moved all the apples to mile 333.  How many
apples will you have left?  Each mile takes 3 trips, so you've dropped
999 apples and you have 2001 left, but consider yourself as having
only 2000 apples because that extra apple is no use.

For the next 500 miles, you only need 2 trips per mile and therefore
you only drop 2 apples per mile.  Now you're at mile 833 and you've
dropped an additional 1000 apples, leaving 1000 apples remaining (all
at mile 833).

From there, you just pack up a full truck and make a run for it.  167
miles left, which means you drop 167 apples and are left with 833
apples by the time you reach Town B.
