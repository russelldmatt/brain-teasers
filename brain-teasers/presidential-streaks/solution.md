---
layout: solution
title:  "Presidential Streaks"
category: brain-teaser
tags: solution

---

Disclaimer, I'm going to refer to Republicans and Democrats as heads and tails, respectively.  

Can we just try all sequences?  The number of sequences of 22 heads and 16 tails is $${38 \choose 16} = 22,239,974,430$$.  Probably not.

Definitions:

- $$total(h, t)$$: the total number of sequences with $$h$$ heads and $$t$$ tails
- $$lt(k, h, t)$$: number of sequences with $$h$$ heads and $$t$$ tails that have a longest streak < $$k$$.
- $$lte(k, h, t)$$: number of sequences with $$h$$ heads and $$t$$ tails that have a longest streak <= $$k$$.
- $$lt\_cond\_right\_is\_tails(k, h, t)$$: number of sequences with $$h$$ heads and $$t$$ tails that have a longest streak < $$k$$ and the rightmost coin flip is tails.
- $$lt\_cond\_right\_is\_heads(k, h, t)$$: number of sequences with $$h$$ heads and $$t$$ tails that have a longest streak < $$k$$ and the rightmost coin flip is heads.
- $$eq\_cond\_right\_k\_tails(k, h, t)$$: number of sequences with $$h$$ heads and $$t$$ tails that have a longest streak = $$k$$ and the rightmost $$k$$ coin flips are tails.
- $$eq\_cond\_right\_k\_heads(k, h, t)$$: number of sequences with $$h$$ heads and $$t$$ tails that have a longest streak = $$k$$ and the rightmost $$k$$ coin flips are heads.
- $$ge(k, h, t)$$: number of sequences with $$h$$ heads and $$t$$ tails that have a longest streak >= $$k$$.
- $$prob\_lte(k, h, t)$$: probability that a sequence with h heads and t tails has a longest streak <= k.  **The answer to our question is $$prob\_lte(5, 22, 16)$$.**

Implementations:
{% highlight python %}
#####################################
# purely for performance
import functools
def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer
#####################################
from math import factorial

@memoize
def choose(n, k): 
    if k < 0: return 0
    else: return factorial(n)/factorial(k)/factorial(n-k)

# the total number of sequences with h heads and t tails
@memoize
def total(h, t): return choose(h+t, h)

# number of sequences with h heads and t tails that have a longest
# streak < k
@memoize
def lt(k, h, t): return total(h, t) - ge(k, h, t)

# number of sequences with h heads and t tails that have a longest
# streak <= k.
@memoize
def lte(k, h, t): return lt(k+1, h, t)

# number of sequences with h heads and t tails that have a longest
# streak < k and the rightmost coin flip is tails.
@memoize
def lt_cond_right_is_tails(k, h, t): 
    return lt_cond_right_is_heads(k, t, h)

# number of sequences with h heads and t tails that have a longest
# streak < k and the rightmost coin flip is heads.
@memoize
def lt_cond_right_is_heads(k, h, t): 
    return lt(k, h-1, t) - eq_cond_right_k_heads(k-1, h-1, t)

# number of sequences with h heads and t tails that have a longest
# streak = k and the rightmost k coin flips are tails.
@memoize
def eq_cond_right_k_tails(k, h, t): 
    return eq_cond_right_k_heads(k, t, h)

# number of sequences with h heads and t tails that have a longest
# streak = k and the rightmost k coin flips are heads.
@memoize
def eq_cond_right_k_heads(k, h, t):
    if h < 0 or t < 0: return 0
    elif h < k and t < k: return 0
    else:
        return lt(k+1, h-k, t) - lt_cond_right_is_heads(k+1, h-k, t)

# number of sequences with h heads and t tails that have a longest
# streak >= k.
@memoize
def ge(k, h, t):
    if h < 0 or t < 0: return 0
    elif h < k and t < k: return 0
    elif k == 0: return total(h, t)
    else:
        return 0 \
            + ge(k, h-1, t) \
            + eq_cond_right_k_heads(k-1, h-1, t) \
            + ge(k, h, t-1) \
            + eq_cond_right_k_tails(k-1, h, t-1)

# probability that a sequence with h heads and t tails has a longest
# streak <= k
@memoize
def prob_lte(k, h, t):
    return float(lte(k, h, t)) / total(h, t)

print prob_lte(5, 22, 16)
{% endhighlight %}

$$prob\_lte(5, 22, 16) \approx 0.55$$, meaning that if there was absolutly no connection between one election and the next, the probability that the longest consecutive sequence of wins by either political party would be 5 terms or less is about 55%.  Null hypothesis not rejected...
