---
layout: solution
title: 'Logicians Numbers'
category: brain-teaser
tags: solution
---

We will display A's numbers on the left and B's numbers on the right, like this:

<div id="0"></div>

- A: “Is your number double mine?”
- B: “I don’t know."

Now we know that B's number is even. If it was odd, he would say no.

<div id="1"></div>

- B: "Is your number double mine?”
- A: “I don’t know."

Now we know that A's number is even. If it was odd, he would say no.

Even more than that, we know that A's number is a multiple of 4. It it was not, then A would know his number is not double an even number (and B's number is even).

<div id="2"></div>

- A: "Is your number half mine?”
- B: “I don’t know."

That rules out all the even numbers from 16 - 30 for B. He is left with 2, 4, 6, 8, 10, 12, 14.

<div id="3"></div>

- B: "Is your number half mine?”
- A: “I don’t know.”

That rules out all numbers above 7 since B's highest possible number left is 14.

<div id="4"></div>

The only multiple of 4 less than 7 is 4. A's number is 4.

- B: “I know your number.”

<style>
  .both {
    display: flex;
    gap: 30px;
    margin: 20px 0px;
  }

  .board {
    display: grid;
    gap: 4px;
    grid-template-columns: repeat(10, min-content);
  }

  .number {
    width: 25px;
    aspect-ratio: 1 / 1;
    border: 1px solid black;
    display: grid;
    place-items: center;
  }

.disabled::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  border-bottom: 3px solid red; /* Adjust the color and style as needed */
  transform: rotate(-45deg);
  transform-origin: center;
}

  .disabled {
    position: relative;
    opacity: 0.3;
  }
</style>

<script>
  function addNumbers(parent, object) {
    for (let n in object) {
      console.log("hi")
      let num = document.createElement("div")
      num.innerHTML = n
      num.classList.add("number")
      if (!object[n]) {
        num.classList.add("disabled")
      }
      parent.appendChild(num)
    }
  }

  function genBoard(as, bs, id) {
    let board = document.getElementById(id);
    board.classList.add("both")
    let a = document.createElement("div");
    a.classList.add("board")
    a.classList.add("a")
    let b = document.createElement("div");
    b.classList.add("board")
    b.classList.add("b")
    board.appendChild(a)
    board.appendChild(b)
    addNumbers(a, as)
    addNumbers(b, bs)
  }

  function init() {
    var o = {};

    for (var i = 1; i <= 30; i++) {
      o[i] = true;
    }

    return o
  }

  let as = init()
  let bs = init()
  genBoard(as, bs, "0")

  for (let key in bs) {
    if (parseInt(key) % 2 == 1) {
      bs[key] = false
    }
  }
  genBoard(as, bs, "1")

  for (let key in as) {
    if (parseInt(key) % 4 !== 0) {
      as[key] = false
    }
  }
  genBoard(as, bs, "2")

  for (let key in bs) {
    if (parseInt(key) >= 16) {
      bs[key] = false
    }
  }
  genBoard(as, bs, "3")

  for (let key in as) {
    if (parseInt(key) > 7) {
      as[key] = false
    }
  }
  genBoard(as, bs, "4")

</script>
