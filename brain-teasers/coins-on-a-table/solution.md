---
layout: solution
title: 'Coins on a table'
category: brain-teaser
tags: solution
---

This is one of those puzzles that seems impossible. But it's not! If you're looking at the solution because you think there is some trick answer, go back and keep trying. There is a perfectly normal solution.

If you're wondering whether you have to use all the coins, you do.

SPOILER BELOW

<hr />
<br />

Take 10 coins away from the 100 and put them in their own pile. Then flip those 10 coins. You're done. Both piles have an equal number of heads.

There are two key insights.

- One is that you are allowed to flip coins. So you can, for example, flip all the coins to get 90 heads and 10 tails if you wanted.
- The second is figuring out how many coins to take away from the first pile. (10 is the key number)

Picking the right number of coins for the new pile is key. Say you started by splitting the coins into two equal piles of 50. There are some number of heads in the left pile (let's call it $$x$$) and $$10-x$$ heads in the right pile. You can flip all the coins in the left pile and you'll now have $$50-x$$ heads in the left pile. Unfortunately, that doesn't help you.

The way I got to the solution is to imagine that there were 50 heads and 50 tails originally. In that case, splitting the coins into two equal piles of 50 coins gives you $$x$$ heads in the left pile and $$50-x$$ heads in the right pile. Then, by flipping all the coins in the left pile you end up with $$50-x$$ heads in the left pile, which is an equal number of heads as the right pile.

Then I struggled for _quite a while_ before figuring out how to apply that insight to the actual problem (where there are only 10 heads originally). But finally I realized that by only pulling 10 coins into the new pile and flipping those, I get $$10-x$$ heads in each pile.
