---
layout: solution
title:  "Bracketology 101"
category: brain-teaser
tags: solution

---

The most straightforward way to solve this puzzle was to compute the probability distributions of the winners of each match recursively, given each swap. The most advantageous swap for the 2-seed is to swap seeds 3 and 16, which increases the 2-seed’s probability of winning by 6.55795%.

<a href="bracketology.py">download code</a>

```python
# each pdf is going to be a dict from player number (int) -> probability of winning
def play(pdf1, pdf2):
    d = dict()
    for (p1, prob1) in pdf1.items():
        if p1 not in d: d[p1] = 0
        for (p2, prob2) in pdf2.items():
            if p2 not in d: d[p2] = 0
            d[p1] += prob1 * prob2 * p2 / (p1 + p2)
            d[p2] += prob1 * prob2 * p1 / (p1 + p2)
    return d

# this crazy one-liner just groups a list into pairs of elements
# i.e. match([1,2,3,4]) = [(1,2), (3,4)]
def match(pdfs):
    return list(zip(*(iter(pdfs),) * 2))

# generate the final win pdf for a given player order
def sim(players):
    pdfs = [ {p: 1} for p in players ]
    while True:
        # each loop is one round
        matchups = match(pdfs)
        pdfs = [ play(x,y) for (x, y) in matchups ]
        if len(pdfs) == 1:
            return pdfs[0]

players = [
    1,
    16,
    8,
    9,
    5,
    12,
    4,
    13,
    6,
    11,
    3,
    14,
    7,
    10,
    2,
    15
]

pdf = sim(players)
starting_win_probability = pdf[2]

def swap(i, j):
    players[i], players[j] = players[j], players[i]
    
best = starting_win_probability
# test all possible swaps of (i, j)
for i in range(16):
    for j in range(16):
        if i == j: continue
        swap(i, j)
        pdf = sim(players)
        swap(i, j)
        if pdf[2] > best:
            print("new best:")
            print ("  swap:", (players[i], players[j])),
            print ("  probability increase:", pdf[2], pdf[2] - starting_win_probability)
            best = pdf[2]
```
