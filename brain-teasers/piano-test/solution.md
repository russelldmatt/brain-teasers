---
layout: solution
title: 'Piano Test'
category: brain-teaser
tags: solution
---

<style>
  img {
    max-width: min(500px, 100vw);
  }

  div.image {
    display: flex;
    justify-content: center;
  }
</style>

The optimal solution is to stop early if the first song contains a mistake, but otherwise never stop early. In expectancy, the total number of songs the student will need to play is 21 3/7.

Here's my work:

The expected number of songs if you stop early after a mistake on the first, second, or third song is 40:

<img src="IMG_2925.jpeg" width="100%" display="max-width: 800px;">

The expected number of songs if you stop early after a mistake on the first or second song is 25 1/5:

<img src="IMG_2926.jpeg" width="100%" display="max-width: 800px;">

The expected number of songs if you stop early after a mistake on the first song is 21 3/7:

<img src="IMG_2927.jpeg" width="100%" display="max-width: 800px;">

The expected number of songs if you never stop early is 25 1/3:

<img src="IMG_2928.jpeg" width="100%" display="max-width: 800px;">
