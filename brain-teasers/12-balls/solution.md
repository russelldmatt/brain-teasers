---
layout: solution
title:  "12 balls"
category: brain-teaser
tags: solution

---

<!-- Add Link to better site about this puzzle -->
Number the 12 balls from 0 to 11.

<pre>
Weigh: left = [0, 1, 2, 3] vs. right = [4, 5, 6, 7]
If Left_heavy:
  Weigh: left = [0, 1, 2, 4] vs. right = [3, 8, 9, 10]
  If Left_heavy:
    Weigh: left = [0] vs. right = [1]
    If Left_heavy: Solved -> Ball 0 is heavy
    If Left_light: Solved -> Ball 1 is heavy
    If Even      : Solved -> Ball 2 is heavy
  If Left_light:
    Weigh: left = [4] vs. right = [11]
    If Left_heavy: Impossible -> Impossible, all balls are equal
    If Left_light: Solved -> Ball 4 is light
    If Even      : Solved -> Ball 3 is heavy
  If Even:
    Weigh: left = [5] vs. right = [6]
    If Left_heavy: Solved -> Ball 6 is light
    If Left_light: Solved -> Ball 5 is light
    If Even      : Solved -> Ball 7 is light
If Left_light:
  Weigh: left = [0, 1, 2, 4] vs. right = [3, 8, 9, 10]
  If Left_heavy:
    Weigh: left = [4] vs. right = [11]
    If Left_heavy: Solved -> Ball 4 is heavy
    If Left_light: Impossible -> Impossible, all balls are equal
    If Even      : Solved -> Ball 3 is light
  If Left_light:
   Weigh: left = [0] vs. right = [1]
    If Left_heavy: Solved -> Ball 1 is light
    If Left_light: Solved -> Ball 0 is light
    If Even      : Solved -> Ball 2 is light
  If Even:
    Weigh: left = [5] vs. right = [6]
    If Left_heavy: Solved -> Ball 5 is heavy
    If Left_light: Solved -> Ball 6 is heavy
    If Even      : Solved -> Ball 7 is heavy
If Even:
  Weigh: left = [0, 1, 2] vs. right = [8, 9, 10]
  If Left_heavy:
    Weigh: left = [8] vs. right = [9]
    If Left_heavy: Solved -> Ball 9 is light
    If Left_light: Solved -> Ball 8 is light
    If Even      : Solved -> Ball 10 is light
  If Left_light:
    Weigh: left = [8] vs. right = [9]
    If Left_heavy: Solved -> Ball 8 is heavy
    If Left_light: Solved -> Ball 9 is heavy
    If Even      : Solved -> Ball 10 is heavy
  If Even:
    Weigh: left = [11] vs. right = [0]
    If Left_heavy: Solved -> Ball 11 is heavy
    If Left_light: Solved -> Ball 11 is light
    If Even      : Impossible -> Impossible, all balls are equal
</pre>
