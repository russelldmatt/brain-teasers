---
layout: solution
title:  "Minimum number of weights"
category: brain-teaser
tags: solution

---

Only 7 weights!

$$
w_0 = 1 \\
w_n = 2 \sum_{x=0}^{n-1} w_x + 1
$$

If you proceed in this way, you'll be able to make every weight up to the sum of all weights you've taken so far.

Starting with only 1, the highest weight you can make is 1, so you should take 3 next (1 * 2 + 1).

As the problem stated, with 1 and 3, you and make 1 to 4.  Using my formula, the next weight to take is 9 (2 * 4 + 1).

Without using the 9, you can already make 1 to 4.  That means you can subtract any of 1-4 from 9, and therefore will be able to make 5-8.  You can also add 1-4 to 9, and now will be able to make 10-13.  Now that you can make up to 13, you should take 27 (2 * 13 + 1).

Using the same logic as before, you can now make any weight up to 40.  So take 81.

And so on...

- 1 --> gets you up to 1
- 3 --> gets you up to 4
- 9 --> gets you up to 13
- 27 --> gets you up to 40
- 81 --> gets you up to 121
- 243 --> gets you up to 364
- 729 --> gets you up to 1093

Cool - powers of three.  My recursive formula just boils down to $$w_n = 3^n$$.


