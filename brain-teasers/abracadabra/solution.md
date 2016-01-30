---
layout: solution
title:  "abracadabra"
category: brain-teaser
tags: solution

---

The standard way to solve this problem is probably with a finite state machine.  However, here is a different, elegant, way to do it.

Imagine that you're a betting man, and you want to bet that George will type abracadabra.  You place the following bet before *every* letter than george types:

- You bet $1 that he will type an "a", with 26 to 1 odds.
- If successful, you bet your $26 that he will type a "b", with 26 to 1 odds.
- If successful, you bet your $26^2 that he will type a "r", with 26 to 1 odds.
- If successful, you bet your $26^3 that he will type a "a", with 26 to 1 odds.
- ... you get the drill

In this way, you place a new $1 bet (the first "a" bet) before each letter that George types, and you only stop and cash out once he has typed abracadabra.  What will your winnings be at that point?

- You just won a string of 11 bets (#letters in "abracadabra"), that were each 26 to 1, so that pays $26^11
- You also won a string of 4 bets (#letters in "abra") that is now paying out $26^4.
- You also won your last bet (string of 1 bet - #letters in "a") that is now paying out $26.

So, you walk away with 26^11 + 26^4 + 26 dollars.  But what does that say about how long it took?

Well, each turn, you placed a *fair* bet of $1 (fair meaning that the expected value was 0).  Since every individual bet was fair, you should have had to place, on average, 26^11 + 26^4 + 26 bets in order win 26^11 + 26^4 + 26 dollars.

So how many letters did George type on average? 26^11 + 26^4 + 26!

He types at a rate of 1 letter/second.  He is 2yrs old when he starts.  So he should be (about) 116,385,862 when he finishes.  Good luck!
