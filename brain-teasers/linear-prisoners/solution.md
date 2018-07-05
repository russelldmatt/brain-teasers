---
layout: solution
title:  "Linear Prisoners"
category: brain-teaser
tags: solution

---

Surprisingly, 9.5 of them, on average, can survive, and 9 will
*definitely* survive.

The prisoner in the back of the line, who has to guess the color of
his hat first, can't do better than random.  There's no information
available to him, so any guess is as good as any other.  Given that,
his only goal is to transfer as much information possible to the rest
of the prisoners with his guess.

What he can do is guess white if the number of white hats that he sees
(i.e. all hats except his own) is even and guess black if the number
of white hats that he sees is odd.  

Then, we come to the next prisoner in line.  He can see whether the
number of white hats in front of him is even or odd.  He also knows
whether the number of white hats in front of him plus his own hat (if
white) is even or odd from the last prisoner's guess.  From that, he
can deduce with certainty whether or not his hat is white.  

Moving on to the next prisoner, the logic is exactly the same.

So, all every prisoner can correctly the color of their own hat except
for the prisoner in the back of the line whose chance of being right
is random (50%).  That comes to 9.5 out of 10 prisoners, on average.




