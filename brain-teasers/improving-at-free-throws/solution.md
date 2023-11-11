---
layout: solution
title: 'Improving at Free Throws'
category: brain-teaser
tags: solution
---

<style>
table {
  margin-bottom: 15px;
}

table td {
    padding: 4px;
    border: 1px solid black;
}  
</style>

Surprisingly, the answer is yes.

Before I explain why, here's an interesting follow-up question: What percentages will have a yes answer to this question and what percentages will have a no answer?

Before attacking this problem systematically, let's just work though one concrete example.

| Made | Total | Percentage |
| 0 | 1 | 0% |
| 0 | 2 | 0% |
| 1 | 3 | 33% |
| 2 | 4 | 50% |
| 3 | 5 | 60% |
| 4 | 6 | 66% |
| 5 | 7 | 71% |
| 6 | 8 | 75% |

Interesting - so in that example he did hit exactly 75%. Was it a fluke? What if he had missed the 8th shot instead of making it but then made all the shots after that until he got over 75%?

| Made | Total | Percentage |
| 5 | 8 | 62.5% |
| 6 | 9 | 66% |
| 7 | 10 | 70% |
| 8 | 11 | 72% |
| 9 | 12 | 75% |

Huh! Exactly 75% again.

Now that we have a sense for the problem, let's attack it my systematically. Let's write down all the scenarios where Jeff's free throw percentage is exactly 75%:

| Made | Total | Percentage |
| 3 | 4 | 75% |
| 6 | 8 | 75% |
| 9 | 12 | 75% |
| 12 | 16 | 75% |
| 15 | 20 | 75% |
| 18 | 24 | 75% |
| 21 | 28 | 75% |
| 24 | 32 | 75% |

(and so on...)

Let's write the same table, but add "number of missed shots":

| Made | Total | Number of missed shots |
| 3 | 4 | 1 |
| 6 | 8 | 2 |
| 9 | 12 | 3 |
| 12 | 16 | 4 |
| 15 | 20 | 5 |
| 18 | 24 | 6 |
| 21 | 28 | 7 |
| 24 | 32 | 8 |

Notice that for any number of missed shots, you can come up with a 75% free throw percentage that has exactly that number of missed shots.

Now, let's say you've already missed three shots and you're below 75%. Maybe you're 5 / 8. We want you to get above 75%. Let's assume for a second that you aren't going to miss any more shots before your free throw percentage goes above 75%. That means your trajectory will look like:

| Made | Total | Percentage |
| 5 | 8 | 62.5% |
| 6 | 9 | 66% |
| 7 | 10 | 70% |
| 8 | 11 | 72% |
| 9 | 12 | 75% |

Given that I stipulated that you weren't going to miss any more shots before your free throw percentage went above 75%, you were bound to hit 9 / 12, since that has 3 missed shots.

If you're already missed four shots and you're below 75% (and we assume you aren't going to miss any more shots), you're bound to hit 12 / 16 before getting your free throw percentage above 75%.

Put another way, let's stipulate that when your free throw percentage first crosses 75%, you will have missed 4 shots. Then you will first hit 12 / 16 before your free throw percentage is above 75%.

If we instead stipulate that when your free throw percentage first crosses 75%, you will have missed 7 shots, then you're bound to hit 21 / 28 first.

For any $$X$$, if we assume you will have missed $$X$$ shots when your free throw percentage first crosses 75%, there is some combination of missed and total shots that has a 75% free throw percentage and has exactly $$X$$ missed shots. You will first hit that combination before your free throw percentage goes above 75%.

## Follow up

For what percentages is the answer to this question yes vs. no?

The key is that 75 = 3 / 4 and 4 - 3 = 1.

If you pick a different percentage, say 60%, which is 3 / 5. Since 5 - 3 is 2, there will be a way to go above 60% without ever hitting it. For example:

| Made | Total | Percentage |
| 0 | 1 | 0% |
| 1 | 2 | 50% |
| 2 | 3 | 66% |

But if you pick a percentage for which the numerator and denominator have a difference of exactly 1, say 66% = 2/3, then you will necessarily hit exactly 66% before your free throw percentage goes above it.
