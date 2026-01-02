---
layout: brain-teaser
title: 'Piano Test'
difficulty: 5
add_date: 2026-01-02
category: brain-teaser
tags:
  - question
  - solved
source: me
---

A piano student is preparing for an exam. The way the exam works is that the student will record himself playing four songs and submit the video to pass the exam. Here are the rules in order to pass:

- The student may make _at most one mistake_ among all four songs in order to pass.
- The video must be one _continuous_ video with all four songs. So if you play the first three songs perfectly and then make two mistakes on the fourth song, you will need to start over from song #1. You cannot re-use the video from the first 3 songs and just reattempt the fourth.

For the sake of making this problem well defined, let's also stipulate the following:

- You can only decide to stop the video after completing a song (you can't stop in the middle of a song). So, the number of songs the student will play will always be an integer.
- You can decide to stop the video after any song - you do not have to complete all four songs. If you make a mistake on the first and second song, there is no reason to continue. You can start over immediately after the second song.
- On any song, the student has a 1/3 chance of playing it perfectly (0 mistakes) and a 2/3 chance of making exactly 1 mistake.

What is the optimal strategy if your goal is to minimize the total number of songs the student has to play before getting a video that will pass the exam? And how many songs will the student have to play in expectancy?
