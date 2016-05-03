---
layout: solution
title:  "How many teams"
category: brain-teaser
tags: solution

---

I found this to be a surpisingly tricky counting problem.  The key is to figure out how to partition the space such that you don't overcount.

Here is one way:

Let's define $$f(N, k)$$ as the number of ways to break $$N$$ kids into *exactly* $$k$$ teams.

Total number of ways to break N kids into teams is:

$$
f(N, 1) + f(N, 2) + f(N, 3) + ... + f(N, N)
$$

In english, all I'm saying is the total number of ways to break N kids up into teams is the number of ways to break them up into exactly 1 team, plus the number of ways I can break them up into exactly 2 teams, and so on.  This seems fairly tri
vial but it allows you to separate the space of teams rather nicely.

$$f(N, 1) = 1$$, which seems fairly obvious.  But what is $$f(N, 2)$$?

Well, let's first answer an easier question.  Call $$g(N, k)$$ the number of ways you can break up N kids into k *named* groups.  So, in this problem, putting all kids in group #1 is considered different from putting all the kids in group #2.  This question has a pretty answer: since you can have $$k$$ choices as to where to each of $$N$$ kids, it's $$g(N, k) = k^N$$.

How can we relate $$g(N, 2)$$ to $$f(N, 2)$$?  $$g(N, 2)$$ contains groups of 2 and groups of 1.  How many groups of 1?  Well, there's one option where all $$N$$ kids are put into group #1 and there's one option where all $$N$$ kids are put into group #2.  More generally, there's $$f(N, 1)$$ ways to put $$N$$ kids into exactly one group, but if there are two possible groups, which one group should we put them in - there's $${N \choose 1}$$ choices for that.

$$
f(N, 2) = \frac{g(N, 2) - {N \choose 1} f(N, 1)}{2!} \\
f(N, 2) = \frac{2^N - {N \choose 1} f(N, 1)}{2!}
$$

Why do we need to divide by $$2!$$ at the end?  Since the teams are named in $$g$$, but not in $$f$$, we will overcount groups of $$2$$ by a factor of $$2!$$.

So, let's try to compute $$f(N, 3)$$ manually before generalizing to $$f(N, k)$$.

$$
f(N, 3) = \frac{3^N - {N \choose 2} f(N, 2) 2! - {N \choose 1} f(N, 1)}{3!} \\
f(N, k) = \frac{k^N - \sum_{i=1}^{k-1}{N \choose i} f(N, i) i!}{k!}
$$

$${N \choose i} * i!$$ is actually just $$N$$ permute $$i$$, which we will call $$P(N, i)$$.  So a more succint solution is

$$
f(N, k) = \frac{k^N - \sum_{i=1}^{k-1}P(N, i) f(N, i)}{k!}
$$

Finally, the question asked how many ways can you make teams out of N kids, regardless of group size, which is just:

$$
\sum_{k=1}^{N} f(N, k)
$$

To double check that this looks reasonable for small N:

| N        | #ways |
| ------------- |:-------------:| -----:|
| 1 | 1 |
| 2 | 2 |
| 3 | 5 |
| 4 | 15 |
| 5 | 52 |
| 6 | 203 |
| 7 | 877 |
| 8 | 4140 |
| 9 | 21147 |
| 10 | 115975 |





