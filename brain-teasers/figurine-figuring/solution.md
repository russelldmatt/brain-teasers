---
layout: solution
title:  "Figurine Figuring"
category: brain-teaser
tags: solution

---

6.859787

The main difficulty with this problem is finding a way to keep it
computationally tractable.  I found a pretty bad way to do this, where
the problem was *just barely* tractable but a friend suggested a much
better way, which I'll describe here:

There are 12 classes of figurines, the partridge, of which there's
only one, up to the 12 drummers.  Let's label these ornaments using a
subscript that describes how many of that type of ornament there are.
So $$o_{12}$$ would be a drummer (since there are 12), and $$o_{11}$$
would be a piper (since there are 11), and so on until $$o_2$$.  We
won't label the partridge this way since it's special.

- Start with just the partridge figurine.
- Next add both of the $$o_2$$ ornaments.
- Next add all three $$o_3$$ ornaments.
- And so on.

At each step, we will update a 13 x 78 matrix that represents the
combination of the maximum number of any ornament type to the left of
the partridge (13 possibilities) as well as the current position of
the partridge (78 possibilities).  In each cell, we will keep track of
the number of ways that combination can happen.

Here's the code:

```python
#!/usr/bin/env python
import numpy as np
import math 

# num_ways[max_figurine_of_one_type_before_partridge, partridge_position] = num_ways given those two facts
num_figurine_types = 12
num_ways = np.zeros([num_figurine_types + 1, 1], dtype=np.float64)
num_ways[0][0] = 1

# [add] adds "one type" of figurine.
# [N] is how many of that figurine type there are
# [num_ways] is described above and represents the state before adding this figurine type
def add(N, num_ways):
    (rows, cols) = num_ways.shape
    num_ways_ = np.zeros([rows, cols + N])
    for num_before in range(N+1):
        num_after = N - num_before
        n = math.comb(N, num_before)
        for prev_num_before in range(rows):
            prev_num_ways = num_ways[prev_num_before]
            max_num_before = max(num_before, prev_num_before)
            new_num_ways = np.pad(n * prev_num_ways, (num_before, num_after))
            num_ways_[max_num_before] += new_num_ways
    return num_ways_ 

for N in range(2, num_figurine_types + 1):
    num_ways = add(N, num_ways)

# the partridge is equally likely to land in each position, so
# normalize so that each position (column) has the same weight.  Now
# each column is a probability distribution function of the max number
# of any one type of figurine to the left of the partridge given the
# partidge is in that positon
num_ways_by_position = np.sum(num_ways, axis = 0)
pdfs = num_ways / num_ways_by_position

sum_over_positions = np.sum(pdfs, axis = 1)
# pdf[i] is probability that max_figurine_of_one_type_before_partridge = i
pdf = sum_over_positions / np.sum(sum_over_positions)
print("pdf:", pdf)

# compute the expected value by multiplying prob[i] * i
ev = sum([ i * pdf[i] for i in range(len(pdf)) ])
print("ev:", ev)
```

And here's the output of said code:

```bash
pdf: [0.01282051 0.04771169 0.06485704 0.07376005 0.0795385  0.08382464 0.0873028  0.09031402 0.09304028 0.09553442 0.09752237 0.09685061 0.07692308]
ev: 6.859787373340944
```
