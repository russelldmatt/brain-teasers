---
layout: solution
title:  "How many songs can you make?"
category: brain-teaser
tags: solution

---

4,251,528 songs.

For the first beat, you have 8 choices (you can play any of the 8 notes).  For the next beat, you actually have 9 choices: you can play any of the 8 notes *or* you can hold the note you're already playing for another beat.  The same goes for the third beat, and so on.

So, the number of different songs you can make is:

$$
8 \cdot 9^6 = 4251528
$$

More generally, if you have $$m$$ notes to choose from and your song can be $$n$$ beats long, the answer is:

$$
m \cdot (m+1)^{n-1}
$$

---------------------
<br />

I originally solved this problem in the following (worse) way, but it's kind of interesting to see that this solution simplifies to the one above:

Let $$f(n)$$ be the number of tunes you can play in $$n$$ beats.  You can compute $$f(n)$$ in the following way:

Take any tune that you can play in fewer beats than $$n$$.  You can add any of the 8 notes to that song, and hold it for however long you need to get to $$n$$ beats.

$$
f(n) = 8 \sum_{i=0}^{n-1} f(i)
$$

and $$f(0) = 1$$

