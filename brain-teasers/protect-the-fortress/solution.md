---
layout: solution
title: 'Protect the fortress'
category: brain-teaser
tags: solution
---

43.

The main insight here is realizing that you should arrange the numbers in 6 columns, like so:

<div class="table-container" id="numberTable1"></div>

So, we can start by crossing off 6, 9, and 20 since the wall-blasters can clearly destroy wall segments of that length:

<div class="table-container" id="numberTable2"></div>

And now is where our 6 columns pay off. Because your enemies can always add as many 6's as they want, we can also cross off everything under 6, 9, and 20:

<div class="table-container" id="numberTable3"></div>

From here on out, it's just finding the smallest number in each column that you can make with 9 and 20, which appens to be 29, 40, and 49:

<div class="table-container" id="numberTable4"></div>

So the answer is 43.

<style>
  .table-container {
    display: flex;
    justify-content: center;
  }
  table {
    max-width: min(100%, 400px);
    border-collapse: collapse;
    margin: 8px 0px;
  }
  table, th, td {
    border: 1px solid black;
  }
  th, td {
    padding: 4px;
    text-align: center;
    position: relative;
  }
  .marked::after {
    content: 'X';
    color: red;
    font-size: 1.5em;
    opacity: 70%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    pointer-events: none;
  }
</style>

<script>
  function createNumberTable(elementId, markedSet) {
    const container = document.getElementById(elementId);
    const table = document.createElement('table');
    const columns = 6;
    const maxN = 78;
    let number = 1;
    // Loop to create rows
    for (let i = 0; i < Math.ceil(maxN / columns); i++) {
        // Create a new row
        const row = document.createElement('tr');

        // Loop to create columns in the current row
        for (let j = 0; j < columns; j++) {
            // Create a new cell
            const cell = document.createElement('td');
            // Set the cell's text to the current number
            cell.textContent = number;
            if (markedSet.has(number)) cell.classList.add("marked")
            number++;

            // Append the cell to the row
            row.appendChild(cell);
        }

        // Append the row to the table
        table.appendChild(row);
    }

    // Append the table to the container element
    container.appendChild(table);
}

createNumberTable("numberTable1", new Set());
createNumberTable("numberTable2", new Set([6, 9, 20]));
createNumberTable("numberTable3", new Set([6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 20, 26, 32, 38, 44, 50, 56, 62, 68, 74]));
createNumberTable("numberTable4", new Set([6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 9, 15, 21, 27, 33, 39, 45, 51, 57, 63, 69, 75, 20, 26, 32, 38, 44, 50, 56, 62, 68, 74, 29, 35, 41, 47, 53, 59, 65, 71, 77, 40, 46, 52, 58, 64, 70, 76, 49, 55, 61, 67, 73]));


</script>
