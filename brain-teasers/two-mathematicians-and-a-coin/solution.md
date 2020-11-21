---
layout: solution
title:  "Two Mathematicians and a Coin"
category: brain-teaser
tags: solution

---

<style>
.r { color: green }
.w { color: red }
</style>

This problem was very unintuitive to me!

Here's a strategy that will allow them to live indefinitely.
Mathematician #1 always guesses the same result as the coin flip that
he was shown.  Mathematician #2 guesses the opposite as the result of
the coin of the coin flip that he was shown.

To prove this works, here are the possible outcomes:

<table class="table table-condensed table-striped">
<tbody>
<tr> <td></td><td>M#1 sees H</td><td>M#1 sees T</td> </tr>
<tr> <td>M#2 sees H</td><td>(<span class="r">H</span>, <span class="w">T</span>)</td><td>(<span class="w">T</span>, <span class="r">T</span>)</td> </tr>
<tr> <td>M#2 sees T</td><td>(<span class="w">H</span>, <span class="r">H</span>)</td><td>(<span class="r">T</span>, <span class="w">H</span>)</td> </tr>
</tbody>
</table>

The simple way to state why this works is that M#1 guesses the result
of the coin flips will be the same and M#2 guesses that they will be
different.  One of them has to be right!  Althought that's a very
elegant way of summarizing the solution, I think it's only useful in
understanding the solution after you know it, not in actually
generating the solution.

Here's how I think one could generate the solution.  Let's first focus
on deterministic strategies.  Without loss of generality, we can say
that when M#1 sees H he will guess H (we could have picked T and the
following chain of logic would work just as well).  

<table class="table table-condensed table-striped">
<tbody>
<tr> <td></td><td>M#1 sees H</td><td>M#1 sees T</td> </tr>
<tr> <td>M#2 sees H</td><td>(<span class="r">H</span>, )</td><td>( , )</td> </tr>
<tr> <td>M#2 sees T</td><td>(<span class="w">H</span>, )</td><td>( , )</td> </tr>
</tbody>
</table>

So, still assuming that M#1 saw H, if M#2 sees H, then M#1 will be
correct and they will survive, so it doesn't matter what M#2 does in
that case.  However, if M#2 sees T then M#1 will be wrong and
therefore M#2 needs to be correct in order for them to survive, so M#2
needs to pick H if he sees T.  

<table class="table table-condensed table-striped">
<tbody>
<tr> <td></td><td>M#1 sees H</td><td>M#1 sees T</td> </tr>
<tr> <td>M#2 sees H</td><td>(<span class="r">H</span>, )</td><td>( , )</td> </tr>
<tr> <td>M#2 sees T</td><td>(<span class="w">H</span>, <span class="r">H</span>)</td><td>( , <span class="w">H</span>)</td> </tr>
</tbody>
</table>

So now we see that if M#2 sees T and M#1 sees T, M#2 is going to guess
wrong, so M#1 better guess right (i.e. T).

<table class="table table-condensed table-striped">
<tbody>
<tr> <td></td><td>M#1 sees H</td><td>M#1 sees T</td> </tr>
<tr> <td>M#2 sees H</td><td>(<span class="r">H</span>, )</td><td>(<span class="w">T</span>, )</td> </tr>
<tr> <td>M#2 sees T</td><td>(<span class="w">H</span>, <span class="r">H</span>)</td><td>(<span class="r">T</span>, <span class="w">H</span>)</td> </tr>
</tbody>
</table>

Finally, it's clear the case in which they still have problems is if
M#1 sees T and M#2 sees H.  We haven't determined what M#2 will do in
that case yet, so let's say if M#2 sees H, he guesses T.

<table class="table table-condensed table-striped">
<tbody>
<tr> <td></td><td>M#1 sees H</td><td>M#1 sees T</td> </tr>
<tr> <td>M#2 sees H</td><td>(<span class="r">H</span>, <span class="w">T</span>)</td><td>(<span class="w">T</span>, <span class="r">T</span>)</td> </tr>
<tr> <td>M#2 sees T</td><td>(<span class="w">H</span>, <span class="r">H</span>)</td><td>(<span class="r">T</span>, <span class="w">H</span>)</td> </tr>
</tbody>
</table>

As you can see, from a random first decision (M#1 will guess H if he
sees H), every other decision was forced, and we somehow come to a
solution which never loses.
