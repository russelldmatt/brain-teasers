---
layout: default
title:  "Crossing Ladders"
category: brain-teaser
tags: solution

---

## {{ page.title }} (Solution) ##

~1.23 feet

Let's call the width of the alley $$w$$.  Cut $$w$$ into two pieces at
the horizontal point at which ladders A and B meet.  Call the section
on the left, $$w_1$$ and the section on the right $$w_2$$.

Using similar triangles, we can set up the following equations:

$$
w_1 + w_2 = w \\
\frac{w}{\sqrt{4 - w^2}} = \frac{w_2}{1} \\
\frac{w}{\sqrt{9 - w^2}} = \frac{w_1}{1} \\
$$

So, we have 3 equations and 3 unknowns.  Should be able to solve it:

$$
\frac{w}{\sqrt{9 - w^2}} = w - w_2 \\
\frac{w}{\sqrt{9 - w^2}} = w - \frac{w}{\sqrt{4 - w^2}} \\
\frac{w}{\sqrt{9 - w^2}} + \frac{w}{\sqrt{4 - w^2}} = w \\
\frac{1}{\sqrt{9 - w^2}} + \frac{1}{\sqrt{4 - w^2}} = 1 \\
$$

I don't know how to actually finish the solution all in closed form, but using a computer, ~1.23 is a solution.
