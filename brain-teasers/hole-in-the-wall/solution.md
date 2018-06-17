---
layout: solution
title:  "Hole in the Wall"
category: brain-teaser
tags: solution

---

Part 1: 

The right strategy is just to go all the way in one direction, and if
you don't find the hole by the end, turn around and walk all the way
in the other direction.

Let's say the length of the wall is 2 (i.e. it goes 1 in either
direction from the middle).  The expected distance you will travel is:

$$ 
0.5 * 0.5 + 0.5 * (2 + 0.5)  \\
0.25 + 1.25 \\
1.5 
$$

Part 2:

Again, I'm going to assume that the wall extends a distance of 1 in
either direction (for a total distance of 2).  I'm also going to
assume that the strategy is of the form, walk right up to a maximum
distance of $$y$$, if you haven't found the hole by then, turn around
walk back the distance of $$y$$ and walk left as far as you can go
($$1$$).  If you *still* haven't found the hole, turn around, walk all
the way back (the $$1$$ that gets you back to the middle and then the
$$y$$ that gets you back to where you turned around) and walk the rest
of the way to the right.

$$
f(y) = \int_0^y x (1-x) \, dx + \int_0^1 (2y + x) (1-x) \, dx + \int_y^1 (2y+2+x)(1-x) \, dx
$$

The first term is the case where you find the hole before turning
around (at a distance of $$y$$).  The second term is the case where
you find the hold somewhere in the left.  The third term is the case
where you also don't find the hold on the left and you have to go all
the way back to the right in order to find the hole.

After a lot of simplifying:

$$
f(y) = \frac{4}{3} - y^2 + y^3
$$

To find the optimal y, take the derivative:

$$
f'(y) = -2y + 3y^2 \\
f'(y) = y(-2 + 3y)
$$

So the function $$f$$ is maximized or minimized when $$y = 0$$ or
$$3y-2 = 0, y = \frac{2}{3}$$.  

$$f(0) = \frac{4}{3}$$ maximizes the function and $$f(\frac{2}{3})
\approx 1.185$$.
