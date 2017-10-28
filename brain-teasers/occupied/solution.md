---
layout: solution
title:  "Occupied"
category: brain-teaser
tags: solution

---

This is a fairly straightforward application of bayes theorom.  To make things easier, let's define a few symbols:

$$o$$ = bathroom is occupied <br>
$$v$$ = bathroom is vacant <br>
$$\bar{o}$$ = bathroom sign says occupied <br>
$$\bar{v}$$ = bathroom sign says vacant <br>

With this new terminology, let's go through the question again:

Assume that 1/3 of bathroom users don’t notice the sign upon entering or exiting. Therefore, whatever the sign reads before their visit, it still reads the same thing during and after their visit. Another 1/3 of the users notice the sign upon entering and make sure that it says “Occupied” as they enter. However, they forget to slide it to “Vacant” when they exit. The remaining 1/3 of the users are very conscientious: They make sure the sign reads “Occupied” when they enter, and then they slide it to “Vacant” when they exit.

$$
P[\bar{o}|o] = \frac{1}{3}P[\bar{o}|v] + \frac{2}{3}(1) \\
P[\bar{o}|v] = \frac{1}{3}P[\bar{o}|v] + \frac{1}{3}(1) + \frac{1}{3}(0) \\
\frac{2}{3}P[\bar{o}|v] = \frac{1}{3} \\
P[\bar{o}|v] = \frac{1}{2} \\
\therefore P[\bar{v}|v] = \frac{1}{2} \\
\therefore P[\bar{o}|o] = \frac{1}{3}\frac{1}{2} + \frac{2}{3}(1) = \frac{5}{6} \\
$$


Finally, assume that the bathroom is occupied exactly half of the time, all day, every day.

$$
P[o] = 1/2 \\
P[v] = 1/2 \\
$$

Two questions about this workplace situation:

If you go to the bathroom and see that the sign on the door reads “Occupied,” what is the probability that the bathroom is actually occupied?

$$
P[o|\bar{o}]?
$$

Apply bayes theorem:

$$
P[o|\bar{o}] = \frac{P[\bar{o}|o] P[o]}{P[\bar{o}]}
$$

We know everything except $$P[\bar{o}]$$ but that's easy to solve for:

$$
P[\bar{o}] = P[\bar{o}|o]P[o] + P[\bar{o}|v]P[v]  = \frac{5}{6}\frac{1}{2} + \frac{1}{2}\frac{1}{2} = \frac{2}{3}
$$

So, plugging everything in:

$$
P[o|\bar{o}] = \frac{P[\bar{o}|o] P[o]}{P[\bar{o}]} \\
P[o|\bar{o}] = \frac{\frac{5}{6} \frac{1}{2}}{\frac{2}{3}} = \frac{5}{8}\\
$$

If the sign reads “Vacant,” what is the probability that the bathroom actually is vacant?

$$
P[v|\bar{v}] = \frac{P[\bar{v}|v]P[v]}{P[\bar{v}]} \\
P[\bar{v}] = \frac{1}{2}\frac{1}{2} + \frac{1}{6}\frac{1}{2} = \frac{1}{3} \\
P[v|\bar{v}] = \frac{\frac{1}{2}\frac{1}{2}}{\frac{1}{3}} = \frac{3}{4} \\
$$
