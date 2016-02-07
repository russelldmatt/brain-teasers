---
layout: solution
title:  "Traffic Jams"
category: brain-teaser
tags: solution

---

$$f(N)$$ is the number of groups for $$N$$ cars.

$$
f(0) = 0 \\
f(N) = 1 + \frac{1}{N} \sum_{i=0}^{N-1} f(i)
$$

<img src="graph.png" width="300px" align="center">
