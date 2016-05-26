---
layout: solution
title:  "Elevator Buttons"
category: brain-teaser
tags: solution

---

Although I did solve this, my solution was much worse than the one posted on the riddler's website, so I'm going to use <a href="http://fivethirtyeight.com/features/can-you-solve-the-puzzle-of-the-overflowing-martini-glass/">that one</a>:

> Given N people equally likely to press any one of M elevator buttons, you can expect M-M(1-1/M)^N of the buttons to be lit up when the elevator begins its ascent. Here’s one way to get there: First, consider the probability that a given button is not pushed by anyone. The probability that any one rider doesn’t select a given floor is (M-1)/M, so the probability that a given floor is selected by no one is ((M-1)/M)^N. Put another way, the probability that any given floor is pressed by someone is 1-((M-1)/M)^N. This is true for all the buttons, independently of one another, so the expected number of pressed buttons is M multiplied by that probability, or M-M((M-1)/M)^N. A little rearranging for simplicity’s sake and we arrive at our answer: M-M(1-1/M)^N.
