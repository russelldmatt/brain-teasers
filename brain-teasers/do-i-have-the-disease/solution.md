---
layout: solution
title:  "Do I have the disease?"
category: brain-teaser
tags: solution

---

<style>
table {
  border-collapse: collapse;
}

table, th, td {
  border: 1px solid;
  padding: 2px;
}
</style>

Classic bayes-rule question.  Instead of using the formula, let's solve it using an example.

Let's start with a population of 1000 people. 2% of people have the disease, so that's 20 people.

|-------------|------------|
| Yes Disease | No Disease |
|-------------|------------|
| 20          | 980        |
|-------------|------------|

If everyone took the test, 95% of the 20 people with the disease would be positive; that's 19 people.  10% of the 980 people without the disease would be positive; that's 98 people.

|---------------|-------------|------------|-------|
|               | Yes Disease | No Disease | Total |
|---------------|-------------|------------|-------|
| Test Positive | 19          | 98         | 117   |
| Test Negative | 1           | 882        | 883   |
|---------------|-------------|------------|-------|
| Total         | 20          | 980        | 1000  |
|---------------|-------------|------------|-------|

You take the test and you're positive.  Given that information, we now only care about the "Test Positive" row.  In that row, 19 out of a total of 117 people have the disease.  So the chance you have it is $$19/117 \approx 0.16%$$.
