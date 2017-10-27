---
layout: solution
title:  "Prison with Levers"
category: brain-teaser
tags: solution

---

Warning: This is not complete!

The strategy:

We designate one prisoner (prisoner #1) to be the only person allowed to pull the second lever down (i.e. from up to down).  Everyone else is only allowed to push the second level up, and they can only do so exactly once.

If we could assume that the second lever starts in a down state, then prisoner #1 will announce that every prisoner has been to the room when he pulls the lever down the 100th time.

{% highlight python %}
In [1]: sum([ 100 + 100 / float(i) for i in range(1,100) ]) + 100
Out[1]: 10517.737751763965
{% endhighlight %}

