---
layout: solution
title:  "Coin Towers"
category: brain-teaser
tags: solution

---

[OEIS](https://oeis.org/A281701) for this sequence.  See the formula section for the exact answer.

I thought it was really interesting/counterintuitive that adding operations of the second type made such a massive difference to the number of coins you could make.  I didn't find the exact optimal answer (or a formula for it), but I found a way to make enough coins such that even if the coins were pennies, I'd have all the money in the world.  Figured that was enough to stop.

This problem is related to the 5th problem on [the 51st IMO](http://yisun.io/papers/imo2010.pdf) (see problem 5), which Terrence Tao blogged about [here](https://polymathprojects.org/2010/07/08/minipolymath2-project-imo-2010-q5/).

There's also a great video about this problem by Po-Shen Loh [here](https://www.youtube.com/watch?v=YdpFPHFE60w&t=4167s).

To give you a sense of the answer, I think it's something like $$2^{2\uparrow\uparrow2\uparrow\uparrow2^{14}}$$, where $$\uparrow$$ is Knuth's [up-arrow notation](https://en.wikipedia.org/wiki/Knuth%27s_up-arrow_notation).  It's a... big number.
