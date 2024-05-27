---
layout: solution
title: 'Infinite Gold'
category: brain-teaser
tags: solution
---

<style>
  img {
    max-width: min(500px, 100vw);
    max-height: 300px;
  }

  div.image {
    display: flex;
    justify-content: center;
  }
</style>

22

The way I solved it was by creating a spreadsheet and incrementally filling it out.

My sheet has 3 columns, one for the starting number of coins, one for what that becomes after applying the magic 1x, and one for what that becomes after applying the magic 2x.

It starts out looking like this:

<div class="image">
<img src="./pic0.png">
</div>

Based on the rules, we know the bag always increases the number of coins, so, we can fill this one.

<div class="image">
<img src="./pic1.png">
</div>

Which means we can fill in this one:

<div class="image">
<img src="./pic2.png">
</div>

And so on:

<div class="image">
<img src="./pic3.png">
</div>

Now it's not super obvious what to do, but notice that 4 and 5 must produce more coins than 3 and less than 6. 3 produces 6 and 6 produces 9, leaving only 7 and 8 as possibilities. Again, using the rule that more input coins produce more output coins, we can fill in 7 and 8 for 4 and 5, respectively.

<div class="image">
<img src="./pic4.png">
</div>

And then we can follow the implications of those:

<div class="image">
<img src="./pic5.png">
</div>

Just like before, 12 -> 21 and 15 -> 24. There are only 22 and 23 available and we have 2 spots, so we can fill them in:

<div class="image">
<img src="./pic6.png">
</div>

And we have our answer! If you put 13 in, you get 22 out!
