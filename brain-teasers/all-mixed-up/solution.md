---
layout: solution
title:  "All Mixed Up"
category: brain-teaser
tags: solution

---

Lots of ways to think about this one.  I'll describe two:

### Recursive: ###

Define $$f(n, k)$$ as the number of ways that exactly $$k$$ elements are in their correct position out of a total of $$n$$ elements.

$$
f(n, k) =
  \begin{cases}
    1 & \text{if $n = k$} \\
    {n \choose k} \big[ (n-k)! - \sum_{i=1}^{n-k} f(n-k, i) \big] & \text{otherwise}
  \end{cases}
$$

In other words, if you want exactly $$k$$ elements in their correct position, there's $${n \choose k}$$ ways to choose the $$k$$ correctly positioned elements.  For each of those choices, you need the $$n-k$$ elements not selected to all be in an incorrect position.  The number of ways that can happen is the total number of ways $$n-k$$ elements can be arranged, $$(n-k)!$$, minus the number of ways that $$n-k$$ can have $$1$$ to $$n-k$$ elements in the correct position, $$\sum_{i=1}^{n-k} f(n-k, i)$$.

### Non-recursive: ###

Define $$z(n)$$ as the number of ways that *zero* elements are in their correct position out of a total of $$n$$ elements.

$$
z(n) = \sum_{i=0}^{n} (-1)^i {n \choose i } (n-i)! \\
f(n, k) = { n \choose k } z(n-k)
$$
