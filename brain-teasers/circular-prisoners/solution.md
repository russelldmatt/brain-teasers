---
layout: solution
title:  "Circular Prisoners"
category: brain-teaser
tags: solution

---

Let's consider a sub-strategies of the form:

If person X, sees [ A, B, C ] for the other three hat colors, they will guess Y

where X is 0-3, A, B, C can be either r or b (red or blue), and Y is either r or b.  Also, the other three hat colors [ A, B, C ] are enumerated from lowest numbered person to highest. This allows us to differentiate between all permutations of [ A, B, C ].

The solution strategy will be a list of sub-strategies.  Note, if person X will "pass", i.e. not guess, when they see a particular [ A, B, C ] sequence of hat colors, we will just omit that sub-strategy.

As an example, let's say our strategy is to guess red when you see all blue hats.  In above terminology, we would describe that strategy as this list of sub-strategies:

- When person 0 sees [ r, r, r ] they will guess b
- When person 1 sees [ r, r, r ] they will guess b
- When person 2 sees [ r, r, r ] they will guess b
- When person 3 sees [ r, r, r ] they will guess b

We can analyze how this strategy would do:

<table class="table table-condensed table-striped">
<thead>
<th>Hat colors</th>
<th>Guesses</th>
<th>Outcome</th>
</thead>
<tbody>
<tr><td>(r, r, r, r)</td><td>[b, b, b, b]</td><td>incorrect</td></tr>
<tr><td>(r, r, r, b)</td><td>[None, None, None, b]</td><td>correct</td></tr>
<tr><td>(r, r, b, r)</td><td>[None, None, b, None]</td><td>correct</td></tr>
<tr><td>(r, r, b, b)</td><td>[None, None, None, None]</td><td>no guesses (incorrect)</td></tr>
<tr><td>(r, b, r, r)</td><td>[None, b, None, None]</td><td>correct</td></tr>
<tr><td>(r, b, r, b)</td><td>[None, None, None, None]</td><td>no guesses (incorrect)</td></tr>
<tr><td>(r, b, b, r)</td><td>[None, None, None, None]</td><td>no guesses (incorrect)</td></tr>
<tr><td>(r, b, b, b)</td><td>[None, None, None, None]</td><td>no guesses (incorrect)</td></tr>
<tr><td>(b, r, r, r)</td><td>[b, None, None, None]</td><td>correct</td></tr>
<tr><td>(b, r, r, b)</td><td>[None, None, None, None]</td><td>no guesses (incorrect)</td></tr>
<tr><td>(b, r, b, r)</td><td>[None, None, None, None]</td><td>no guesses (incorrect)</td></tr>
<tr><td>(b, r, b, b)</td><td>[None, None, None, None]</td><td>no guesses (incorrect)</td></tr>
<tr><td>(b, b, r, r)</td><td>[None, None, None, None]</td><td>no guesses (incorrect)</td></tr>
<tr><td>(b, b, r, b)</td><td>[None, None, None, None]</td><td>no guesses (incorrect)</td></tr>
<tr><td>(b, b, b, r)</td><td>[None, None, None, None]</td><td>no guesses (incorrect)</td></tr>
<tr><td>(b, b, b, b)</td><td>[None, None, None, None]</td><td>no guesses (incorrect)</td></tr>
</tbody>
</table>

So, in 4 of the 16 possible hat color permutations, at least one person would guess correctly and no one is wrong, so there is a 1/4 chance they would go free.

The crucial realization is that for every substrategy, there is a 50% chance that the guess is right and a 50% chance that the guess is wrong.  Once you accept that, then the only hope is to make everyone guess wrong at the same time, and guess right at different times, since multiple wrong guesses at the same time is only as bad as a single wrong guess.

So, without actually finding the best strategy, we can put an upper bound on the probability of going free.  If you had exactly one person guess right in 13 of the 16 scenarios, there would be 13 incorrect guesses that would need to happen.  There can be 4 incorrect guesses per scenario, and 3 scenarios left, which only leaves a maximum of 12 incorrect guesses.  Given the fact that there needs to be an incorrect guess for every correct guess, this is impossible.  So going free in 12 of the 16 scenarios is the best case that we can hope for.

Finding that strategy was pretty hard for me, so I used a computer, and my resulting solution was kind of gross.  Emily Berger did not find this so hard, and found a much prettier solution by hand, so I'm going to steal hers - thanks Emily!

1.  Totally ignore person 3
2.  Person 0, 1, and 2 will guess red when they see at least two blues
3.  Person 0, 1, and 2 will guess blue when they see at least two reds

To prove this gets 75% (12/16) of the scenarios right, we can just enumerate them.  Also, let's completely omit person 3 since he never guesses.  Just note that for each of the scenarios below, in the 4 person game there will be two such scenarios - one when person 3 is r and one when person 3 is b.

<table class="table table-condensed table-striped">
<thead>
<th>Hat colors</th>
<th>Guesses</th>
<th>Outcome</th>
</thead>
<tbody>
<tr><td>(r, r, r)</td><td>[b, b, b]</td><td>incorrect</td></tr>
<tr><td>(r, r, b)</td><td>[None, None, b]</td><td>correct</td></tr>
<tr><td>(r, b, r)</td><td>[None, b, None]</td><td>correct</td></tr>
<tr><td>(b, r, r)</td><td>[b, None, None]</td><td>correct</td></tr>
<tr><td>(r, b, b)</td><td>[r, None, None]</td><td>correct</td></tr>
<tr><td>(b, r, b)</td><td>[None, r, None]</td><td>correct</td></tr>
<tr><td>(b, b, r)</td><td>[None, None, r]</td><td>correct</td></tr>
<tr><td>(b, b, b)</td><td>[r, r, r]</td><td>incorrect</td></tr>
</tbody>
</table>

