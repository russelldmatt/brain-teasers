---
layout: solution
title:  "How many ways"
category: brain-teaser
tags: solution

---

20 ways.

Here are two good ways to solve it.

### Label each vertex ###

The only way to get to a vertex is from below or from the left.  If there are $$b$$ ways to get to the vertex below and $$l$$ ways to get to the vertex to the left, then there must be $$(b + l)$$ ways to get to this vertex.

To start, there's only one way to get to the bottom left vertex.  Work from there.

### Combinatorics ###

If each move is a move one up or one to the right, then you will need to take exactly 6 moves to get from the bottom left to the top right.  3 of those moves, need to be moves up.  The only thing left is to decide which 3 moves (out of your 6 moves) will be up moves.  That's $${6 \choose 3} = 20$$ 

