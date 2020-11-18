---
layout: solution
title:  "Working Together"
category: brain-teaser
tags: solution

---

The trick here is to understand that completion times do not add, but
rates do.  For example:

If Alice finishes a job in 2 hours and Bob finishes it in 3 hours,
when working together they *do not* finish it in 5 hours (2+3).  But
if Alice finishes 1/2 the job per hour and Bob finishes 1/3 of it per
hour, when working together they *do* finish 5/6 of it per hour (1/2 +
1/3)..

So now we can set up equations.  Let's call $$A$$ Alice's per hour
rate, $$B$$ Bob's per hour rate, and $$C$$ Charlie's per hour rate.

$$
\begin{align*}
A + B &= \frac{1}{2} \\
A + C &= \frac{1}{3} \\
B + C &= \frac{1}{4} \\
\end{align*}
$$

What is $$A + B + C$$?

Now it seems pretty simple, you add all three equations and divide by two:

$$
\begin{align*}
2A + 2B + 2C &= \frac{1}{2} + \frac{1}{3} + \frac{1}{4} \\
A + B + C &= \frac{13}{24} \\
\end{align*}
$$

So, when all three work together, their per hour rate ($$A + B + C$$) is $$\frac{13}{24}$$, so the time it takes them to complete the job is just 1 over the rate, so $$\frac{24}{13}$$ hours.

