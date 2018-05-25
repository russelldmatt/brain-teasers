---
layout: brain-teaser
title:  "Moser's circle problem"
difficulty: 8
add_date: 2018-05-24
category: brain-teaser
tags:
- question
- solved

---

This is a somewhat famous problem, known as Moser's circle problem:

Here's Wolfram's formulation:
> Determine the number of pieces into which a circle is divided if n
points on its circumference are joined by chords with no three
internally concurrent.

A less jargony version is:

Draw n points on the circumference of a circle.  Connect each pair of
points with a straight line segment.  What is the maximum number of
regions that the circle can be divided into as a function of n?

A few examples:

For n = 2, it has 2 regions,

<svg width="500" height="500"><ellipse cx="250" cy="250" rx="200" ry="200" fill="none" stroke="black"></ellipse>
<line x1="450" y1="250" x2="50" y2="250.00000000000003" stroke="blue" stroke-width="1"></line></svg>

and for n = 3, it has 4 regions.

<svg width="500" height="500"><ellipse cx="250" cy="250" rx="200" ry="200" fill="none" stroke="black"></ellipse>
<line x1="450" y1="250" x2="250" y2="450" stroke="blue" stroke-width="1"></line>
<line x1="450" y1="250" x2="249.99999999999997" y2="50" stroke="blue" stroke-width="1"></line>
<line x1="250" y1="450" x2="249.99999999999997" y2="50" stroke="blue" stroke-width="1"></line></svg>

