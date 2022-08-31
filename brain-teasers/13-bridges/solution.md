---
layout: solution
title:  "13 Bridges"
category: brain-teaser
tags: solution

---

Although this solution is really beautiful, it's a classic "aha
moment" problem, by which I mean that it relies on a single "aha moment".
If you don't manage to see this one trick, the problem is basically
impossible.  If you do manage to see it, it's trivial.

Imagine that instead of bridges, each line was a water dam (which prevents water from flowing across it).  Notice that "crossing from the north to the south bank" is now exactly symmetric to the question "can water flow from the left to the right".

<pre>

             North Bank
     ###########################
        |         |         |
        O---------O---------O
        |         |         |
        O---------O---------O
        |         |         |
     ###########################
             South Bank
</pre>

If water can flow from the left to the right, then there is no path that allows us to cross from the top to the bottom.  Similarly, if there is a path that allows us to cross from the top to the bottom, then water cannot flow from left to right.

Since water flowing from the left to the right and us crossing from the top to the bottom are both completely symmetric, then it must be true that each one has a 50% chance.  QED.

If the claim "water cannot flow from left to right => there is a path from top to bottom" is not intuitive to you, consider this: Dye the water on the left red.  The rightmost fridge of red squares draws a path from top to bottom.
