---
layout: solution
title:  "Five Card Magic Trick"
category: brain-teaser
tags: solution

---

Top answer on [puzzling.stackexchange.com](http://puzzling.stackexchange.com/questions/6569/a-five-card-trick-how-does-it-work#answer-6571):

I'm going to assume Alice looked at the cards and chose which one to
give back to you. The key to the puzzle is then to encode a single
card's suit and value in 4 cards without the luxury of choosing those
4 cards arbitrarily from the whole deck.

The suit is easy. In 5 cards there must be a double of at least one
suit. So the first (or last, but I'll choose arbitrarily) card in the
bunch she passes is the same suit as yours. Now there are three cards
left to encode a number from 1 to 13. However Alice chose which card
of your suit to pass to Bob and which to return to you. She can choose
according to a rule that gets the number of possible cards down
significantly.

The three passed cards can be designated small medium and large
according to their number, and then breaking ties by suit order (clubs
smallest, diamonds, hearts, spades as in bridge.) This gives six
possible numbers to be represented by the 3 passed cards based on
their order: SML, SLM, MLS, MSL, LSM, LMS.

So how does she choose which of the suit cards to pass and which to
return? Bob will add the encoded number to the passed card (going
around K-A-2 if need be) to get the returned card. Alice passes
whichever card is within an add of 6.

