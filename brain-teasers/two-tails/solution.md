---
layout: solution
title:  "Two Tails"
category: brain-teaser
tags: solution

---

There's a really neat trick to solve this kind of problem.

On each coin flip, you make a *fair* bet of $1 that the next flip is
going to be tails.

- If it's T, you lose your $1.  You bet $1 again on the next flip that it will be T.  Repeat.
- If it's T, you do 2 things:
  - You double down on this bet.  You take your now $2 (since you won your last bet) and bet that the next flip is going to be T.  If you win, the game will be over and you'll have $4 from this bet.
  - You also start the process over again, by which I mean you make a brand new $1 bet that the next flip is T.

So here's the trick.  When you finally get TT, you know how much money you're going to win.
- 2 flips ago, you'll have started a betting streak of TT that will have just paid off $4
- 1 flip ago, you'll have started a betting stream of T that will have also just won, so that's $2 extra dollars.

So when you get TT, you know you'll have just won $6.  Notice that on
every single coin flip, you placed a new $1 fair bet.  So if you win
$6 at the end, and all your bets were fair, you should have placed (on
average) 6 bets of $1, meaning that on average this process should
take 6 flips!

If you want to try to make sure you understand this procedure, try to
figure out how many flips you'd expect until you see HHHH.  It should
be 30.

