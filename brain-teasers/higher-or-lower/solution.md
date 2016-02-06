---
layout: solution
title:  "Higher or Lower"
category: brain-teaser
tags: solution

---

To start, it seems intuitively clear that if the current number is > 0.5, then you should guess "lower", and otherwise guess "higher".  Let's just agree that's optimal.

Let's call $$z(x)$$ the value of the game if the "current number" (i.e. the last number generated) is $$x$$.  Given our symmetric strategy around 0.5, it's also clear that $$z(\frac{1}{2}+x) = z(\frac{1}{2}-x)$$.  So, to simplify our equations, let's define $$f(x)$$ as the value of the game if the current number is $$x$$ away from $$\frac{1}{2}$$.  In other words, $$z(x) = f(\vert x - \frac{1}{2}\vert)$$. So, if the current number is 1, then the value of this game is $$z(1) = f(\frac{1}{2})$$.

This equation accurately describes the value of the game, for any $$x$$:

$$
f(x) = \int_{0}^{\frac{1}{2}} (1 + f(y)) dy + \int_{0}^{x} (1 + f(y)) dy \\
f(x) = \int_{0}^{\frac{1}{2}} f(y) dy + \int_{0}^{x} f(y) dy + \frac{1}{2} + x 
$$

But how to solve that... ugh.

Let's define $$f'(x) = g(x)$$, i.e. $$f(x)$$ is the first derivative of $$g(x)$$.  Now we can rewrite our equations:

$$
g'(x) = g(y) \bigg|_0^{\frac{1}{2}} + g(y) \bigg|_0^x + \frac{1}{2} + x \\
g'(x) = g(\frac{1}{2}) - g(0) + g(x) - g(0) + \frac{1}{2} + x \\
g'(x) = g(x) + x + g(\frac{1}{2}) - 2g(0) + \frac{1}{2}
$$

Not gonna lie, had to watch some khan academy videos to refresh myself on how to solve linear differential equations.  You basically assume the equation is linear, $$g(x) = mx + b$$, and then solve for $$m$$ and $$b$$.

$$
g(x) = mx + b \\
g'(x) = m = g(x) + x + g(\frac{1}{2}) - 2g(0) + \frac{1}{2} \\
m = g(x) + x + g(\frac{1}{2}) - 2g(0) + \frac{1}{2} \\
m = mx + b + x + g(\frac{1}{2}) - 2g(0) + \frac{1}{2} \\
0 = x(m+1) + b - m + g(\frac{1}{2}) - 2g(0) + \frac{1}{2}
$$

And since $$0$$ is a constant, it can't depend on $$x$$, meaning that $$m+1 = 0$$ and $$m = -1$$.  $$b$$ doesn't actually matter since I'm only interested in $$f(x)$$, which depends on differences of $$g(x)$$, meaning that the constant part of $$g(x)$$ will always cancel out.

So we now have this equation:

$$
g(x) = -x + c_1 \\
g'(x) = -1
$$

We can plug this into our original equation for $$g(x)$$ to check that it works:

$$
g'(x) = g(x) + x + c_2 \\
-1 = -x + c_1 + x + c_2 \\
-1 = c_1 + c_2
$$

Constants aside, it looks good.  But wait, there's one more thing.  These linear solutions actually aren't the only solutions that work.  You can add $$c e^{x}$$ and the differential equation for $$g'(x)$$ will still hold as follows:

$$
g(x) = c_0 e^x - x + c_1 \\
g'(x) = c_0 e^x - 1 \\
g'(x) = g(x) + x + c_2 
$$

So let's incorporate an additional $$c_0 e^x$$ into our solution for $$g(x)$$.

$$
g(x) = c_0 e^x + -x + c_1 \\
f(x) = c_0 e^x - 1 
$$

So, I don't care about $$c_1$$ because the function I really want is $$f(x) = g'(x)$$ and $$c_1$$ won't affect $$f(x)$$.  But $$c_0$$ will affect $$f(x)$$ so we need to figure that one out.

In order to solve for $$c_0$$ we can use the fact that $$f(\frac{1}{2}) = 2f(0)$$.  This is from intuition.  If the current number if 0.5, and you guess lower, and you're right, then - on average - you're in the same situation as if the current number is 1 and you guess lower.  The only difference is that in the 0.5 case, you're wrong half the time.  So $$f(\frac{1}{2}) = 2f(0)$$.

$$
f(x) = c_0 e^x - 1 \\
f(\frac{1}{2}) = 2f(0) \\
c_0 e^{\frac{1}{2}} - 1 = 2(c_0 - 1) \\
c_0 = \frac{-1}{e^{\frac{1}{2}}-2}
$$

Great, we have $$c_0$$, so let's finally solve for $$f(x)$$.

$$
f(x) = c_0 e^x - 1 \\
f(x) = \frac{-1}{e^{\frac{1}{2}}-2} e^x - 1
$$

Let's use one last thing from intuition.  $$f(0.5)$$ is one more than the value of the game.  You can think of it as "you get one freeby, then we're going to play the game that I originally described".  Knowing this - the value of the game is:

$$
game = f(0.5) - 1 \\
game = \frac{-1}{e^{\frac{1}{2}}-2} e^{\frac{1}{2}} - 2 \approx 2.7
$$


