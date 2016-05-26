---
layout: solution
title:  "Reverse Birthday Problem"
category: brain-teaser
tags: solution

---

Let $$g(n,k)$$ be the number of ways you can put n people into k buckets:

$$g(n,k) = k^n$$

Let $$f(n,k)$$ be the number of ways you can put n people into k buckets, *using all k buckets*.

$$f(n,k) = g(n,k) - \sum_{i=1}^{k-1}{ k \choose i }f(n,i)$$

In words, the number of ways you can put n people into k buckets *using all k buckets*, is the number of ways you can put n people into k buckets, minus the number of ways you can put n people into exactly 1 bucket (times the number of ways you can choose that one bucket out of k buckets), minus the number of ways you can put n people into exactly 2 buckets (times the number of ways you can choose those two buckets out of k buckets), etc...

Now that we have $$g$$ and $$f$$, the original problem just becomes:

Find the smallest $$N$$, s.t. $$f(N, 365) > g(N, 365) / 2$$.

Using a computer, I found the smallest $$N$$ to be $$2287$$.


