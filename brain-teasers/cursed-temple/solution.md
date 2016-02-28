---
layout: solution
title:  "Cursed Temple"
category: brain-teaser
tags: solution

---

You know that you aren't cursed, so you can explore an entire tunnel alone and reliably report whether it leads to the exit.  You also know the tunnel that you just came from, which isn't the exit.  That leaves three more tunnels to explore between your 8 friends, 2 of whom are cursed.

Split them up into groups of 3, 3, 2.

When everyone reports back (assuming you didn't find the exit, in which case you all survive), you can break up the outcomes into three possibilities:

- Nobody disagrees
- One group disagrees
- Two groups disagree

One important fact is that if you can trust all but one group, then you can figure out which tunnel is the exit by process of elimination.

If nobody disagrees, then you know that each of the two groups of three are telling the truth since, at most, only two of them could be lying.  That means you can trust all but one group, the group of two.  Solved.

If one group disagrees, then you can trust all but that group. Solved.

If two groups disagree, then you know that there must be one cursed friend in each group. At least one group will be a group of three, and since there is only one cursed friend in the group, you can trust majority rules.  Therefore, you can trust all but one group.  Solved.
