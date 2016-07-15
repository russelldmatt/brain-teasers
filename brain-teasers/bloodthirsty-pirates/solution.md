---
layout: solution
title:  "Bloodthirsty Pirates"
category: brain-teaser
tags: solution

---

Work backwards:

If only Pirate 1 is left, he will get all 1000 coins.
<pre>
Pirate 1 -> 1000
Pirate 2 -> X
Pirate 3 -> X
Pirate 4 -> X
Pirate 5 -> X
</pre>

If Pirates 1 and 2 left, Pirate 1 will not accept any proposal because he he knows that if he rejects Pirate 2's proposal, Pirate 2 will be thrown overboard and Pirate 1 will get all 1000 coins.  Pirate 2 is doomed to get nothing.
<pre>
Pirate 1 -> 1000
Pirate 2 -> X
Pirate 3 -> X
Pirate 4 -> X
Pirate 5 -> X
</pre>

If Pirates 1, 2, and 3 are left, Pirate 3 will offer Pirate 2 one coin and give himself the rest.  Pirate 2 will accept knowing that if he rejects then he will get nothing.  Pirate 3 will also accept, so it will be accepted by a majority.
<pre>
Pirate 1 -> 0
Pirate 2 -> 1
Pirate 3 -> 999
Pirate 4 -> X
Pirate 5 -> X
</pre>

If Pirates 1, 2, 3, and 4 are left, Pirate 4 will offer Pirate 1 1, Pirate 2 2, and give himself the rest.
<pre>
Pirate 1 -> 1
Pirate 2 -> 2
Pirate 3 -> 0
Pirate 4 -> 997
Pirate 5 -> X
</pre>

If Pirates 1, 2, 3, 4, and 5 are left, Pirate 5 will offer:
<pre>
Pirate 1 -> 2
Pirate 2 -> 0
Pirate 3 -> 1
Pirate 4 -> 0
Pirate 5 -> 997
</pre>




