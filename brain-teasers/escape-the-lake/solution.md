---
layout: solution
title:  "Escape the Lake"
category: brain-teaser
tags: solution

---

<style>
button {
  margin: 0px auto;
  font-size: small;
}
canvas {
	box-shadow: 5px 5px 5px grey;
	border: 1px solid grey;
	width: 500px; 
    max-width: 100%;
	height: 500px; 
	display: block; 
	margin: 30px auto 10px;
}
</style>

The first thing to realize is that you can't just swim directly away
from the monster.  To make things easier on ourselves, let's assume
the lake has a radius of 1 and we swim at a rate of 1 per minute (so
the monster runs at a rate of 4 per minute).  If we swim directly away
from the monster, it takes us 1 minute to reach the shore.  The
monster needs to run half the circumference of the circle, which is
pi.  Since the monster can run 4 in 1 minute and pi is less than 4,
the monster will easily outrun us and be waiting at the shore to eat
us when we arrive.  Like so:

<div id="naive"></div>
<div style="display:flex; justify-content:center">
	<button onclick="naive_sketch.restart()">restart sketch</button>
</div>

So what can we do?  At first it seems impossible, but the solution is
quite cute.  The critical realization is that if we swim in a circle
of radius 1/4, we can complete one full rotation in exactly the same
time as the monster can run around the lake.

So if we swim in a circle of radius *barely* less than 1/4, then the
monster will not be able to keep up with us.  If we do this for long
enough, eventually the monster will be on the opposite side of the
circle as us.  In other words, we will already be 1/4 of the way
towards the opposite edge of the lake.  Can we make a dash for it?

We will have to swim 3/4 to reach the other side and the monster needs
to run halfway around the circle.  The monster can run 3 in the time
it takes us to run 3/4, but half the circle is more than that!  So,
indeed, this strategy works.

If it doesn't make sense, watch this:

<div id="sketch1"></div>
<div style="display:flex; justify-content:center">
	<button onclick="sketch1.restart()">restart sketch</button>
</div>

Can we do better?  Is there a better strategy than dashing in a
straight line directly away from the monster?  It turns out yes.  For
a complete full derivation of the solution, I will refer you to [this
post](https://datagenetics.com/blog/october12013/index.html), but I'll
tell you that the best strategy as follows:

Assume you swim at a speed of 1 and the monster runs at a speed of v.

1. Do the same circling procedure described above (at a radius of
   slightly less than 1/v) to get as far as possible away from the
   monster.
2. When you're at your farthest point, instead of running straight
   away from the monster towards the shore, run at a right angle to
   that path.  This causes the monster's path to be the longest in
   order to reach you.
   
Take a look:

<div id="sketch2"></div>
<div style="display:flex; justify-content:center">
	<button onclick="sketch2.restart()">restart sketch</button>
</div>

As you can see from the top right, in this simulation the monster's
speed is 4.55.  At the limit, you can actually escape any speed lower
than about 4.603338848.  I set the speed somewhat lower to A) make the
optimal strategy take less time and B) because there are only so many
pixels on the screen and rounding means we can't reach the theoretical
limit.

<script src="https://cdn.jsdelivr.net/npm/p5@1.4.0/lib/p5.js"></script>
<script src="/brain-teasers/escape-the-lake/sketch.js"></script>

<script>
let naive_sketch = new p5(naive, 'naive');
let sketch1 = new p5(four, 'sketch1');
let sketch2 = new p5(optimal, 'sketch2');
</script>

