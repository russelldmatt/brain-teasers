---
layout: brain-teaser
title:  "All Tails"
difficulty: 5
add_date: 2020-12-27
category: brain-teaser
tags:
- question
- solved
source: mtong

---

You have n coins in a row in some beginning state of heads/tails. Define a process as follows:

If you have k>0 heads, flip over the coin in the kth position from the left.
If you have k=0 heads, stop. Otherwise repeat.

For example, for THT, the process goes
THT -> HHT -> HTT -> TTT

For fixed n, calculate the average number of steps it takes to
terminate over all 2^n possible beginning states.
