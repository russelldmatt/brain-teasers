---
layout: solution
title:  "Neurotic Basketball Player"
category: brain-teaser
tags: solution

---

2/3

## Using Simulation ##
{% highlight python %}
import numpy as np

def one(num_shots):
    import random
    count = 2
    num_baskets = 1
    while count < (num_shots - 1):
        made_shot = random.random() < (num_baskets / float(count))
        if made_shot:
            num_baskets += 1
        count += 1
    # last shot
    made_last_shot = random.random() < (num_baskets / float(count))
    if made_last_shot:
        num_baskets += 1
        return num_baskets
    else:
        # re-run the sim because in reality he did make last (99th) shot
        return one(num_shots)

def simulate(num_shots, num_sims):
    buckets = np.zeros(num_shots + 1)
    for i in range(num_sims):
        buckets[one(num_shots)] += 1
    return buckets / num_sims

def prob_makes_it(ps):
    count = len(ps) - 1
    xs = np.array([x for (x, y) in enumerate(ps)])
    prob_makes_it = xs / float(count)
    return sum(ps * prob_makes_it)

ps = simulate(99, 100000)
print ps
print prob_makes_it(ps)
{% endhighlight %}

## Using PDF w/Computer ##
{% highlight python %}
import numpy as np

def step(ps, xs, count):
    prob_makes_it = xs / float(count)
    new_ps = np.append(ps * (1 - prob_makes_it), 0) + np.append([0], ps * prob_makes_it)
    new_xs = np.append(xs, count + 1)
    return (new_ps, new_xs, count + 1)

def makes_it(ps, xs, count):
    new_ps = np.append(0, ps)
    new_xs = np.append(xs, count + 1)
    return (new_ps, new_xs, count + 1)

def adjust_because_he_made_it(ps, xs, count):
    prob_makes_it = xs / float(count)
    ps = (prob_makes_it * ps) / 0.5
    return ps

def prob_makes_it(ps, xs, count):
    prob_makes_it = xs / float(count)
    return sum(ps * prob_makes_it)

def pretty_print(ps, xs, count):
    def print_array(a):
        for x in a: print "{:0.2f}\t".format(x),
        print ""
    print "after {} shots prob makes it {}:".format(count, prob_makes_it(ps, xs, count))
    print_array(xs)
    print_array(ps)

ps = np.array([0., 1., 0.])
xs = np.array([0, 1, 2])
count = 2

pretty_print(ps, xs, count)
(ps, xs, count) = step(ps, xs, count)
pretty_print(ps, xs, count)
(ps, xs, count) = step(ps, xs, count)
pretty_print(ps, xs, count)

while count < 98:
    (ps, xs, count) = step(ps, xs, count)

ps = adjust_because_he_made_it(ps, xs, count)
(ps, xs, count) = makes_it(ps, xs, count)
pretty_print(ps, xs, count)
{% endhighlight %}

## Using intuition ##

The probability of making a shot doesn't change from one shot to the next.  Let's say he's currently made n out of t shots.

$$
p_{make it} = \frac{n}{t} 
$$

At the next step

$$
p_{make it} = \frac{n}{t} \frac{n+1}{t+1} + \frac{t - n}{t} \frac{n}{t+1} \\
p_{make it} = \frac{n(n+1+t-n)}{t(t+1)} \\
p_{make it} = \frac{n(1+t)}{t(t+1)} \\
p_{make it} = \frac{n}{t} \\
$$

Also, it doesn't feel like the order of the baskets should matter.  If we obsever the 99th shot, is that any different than if we observed the 3rd shot?  Let's guess no.

Well, if we observed the third shot, we *know* that he would be 2/3 to make the next shot (since we observed him making 2 of 3 baskets so far).  And if that was the case, and we observed nothing until the 100th shot, we would guess that he's 2/3 to make it as well.  So, assuming that nothing is different about observing the 99th shot vs. the 3rd shot, he should be 2/3 to make the 100th shot.
