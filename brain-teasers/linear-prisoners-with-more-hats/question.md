---
layout: brain-teaser
title:  "Linear prisoners... with more hats"
difficulty: 5
add_date: 2018-07-05
category: brain-teaser
source: mayank mehta (or maybe his brother?)
tags:
- question
- solved

---

<style>
.image-blurred {
    background-image: url('./hats.jpg');
	width: 233px;
    height: 350px;
    /* you need to match the shadow color to your background or image border for the desired effect*/
	background-repeat: no-repeat;
    background-size: 233px 350px;
    box-shadow: 0 0 2px 2px white inset;
	margin: auto;
	margin-bottom: 10px;
}
</style>

<div class="image-blurred" style="display:block;"></div>

This problem is an extension of a previous problem [Linear Prisoners](../linear-prisoners/question.html), so if you want to start with a simpler problem, go there.

A jailer lines up 10 prisoners in a row for a perverse game.  All prisoners are facing forward and can only see the prisoners in front of him.  As such, the prisoner in the back of the line can see all other prisoners and the prisoner at the front of the line can't see anyone.  The jailer then puts a hat on each prisoner's head.  Each hat could be one of $$n$$ colors (the value of $$n$$ is known to the prisoners).  Then the game begins.  Starting from the back of the line, the jailer asks the prisoners, one by one, for the color of his or her hat.  The prisoner lives only if he or she is correct about the color of their own hat.

As usual, the prisoners are told ahead of time that this game will occur and are given time to come up with a strategy.  What's their best strategy and, on average, how many prisoners will survive (as a function of $$n$$)?


