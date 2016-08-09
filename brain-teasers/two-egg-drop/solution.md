---
layout: solution
title:  "Two Egg Drop"
category: brain-teaser
tags: solution

---

Drop the first egg from floor 14.  If it breaks, start from floor 1 with the second and move up by one floor until it breaks.  It if doesn't break:

Drop the first egg from floor 27 = (14 + 13).  If it breaks, start from floor 15 with the second and move up by one floor until it breaks.  It if doesn't break:

Drop the first egg from floor 39 = (14 + 13 + 12).  If it breaks, start from floor 28 with the second and move up by one floor until it breaks.  It if doesn't break:

Drop the first egg from floor 50 = (14 + 13 + 12 + 11).  etc...

In short, go up by (14-#tries-so-far) with the first egg if the first egg doesn't break, and if it does, then start from the last floor that your first egg didn't break from and move up by one with the second egg.

This gives you a 14-drop worst case.
