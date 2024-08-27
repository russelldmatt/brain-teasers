const gridContainer = document.querySelector('.grid-container');
const waysDisplay = document.getElementById('ways-display');

// Example data: You can expand this with more squares and their ways
const waysToReach = paths;

for (let row = 1; row <= 96; row++) {
  for (let col = 1; col <= 4; col++) {
    const square = document.createElement('div');
    const squareId = `${row}_${col}`;
    const ways = waysToReach[squareId];
    square.classList.add('grid-square');
    if (!ways) square.classList.add('disabled');
    square.textContent = squareId;
    square.dataset.id = squareId;

    square.addEventListener('click', () => {
      highlightSquare(squareId);
      displayWays(squareId);
    });

    gridContainer.appendChild(square);
  }
}

function displayWays(squareId) {
  const ways = waysToReach[squareId];
  if (ways) {
    waysDisplay.innerHTML = ways.map((way) => makeClickable(way)).join('<br>');
  } else {
    waysDisplay.textContent = 'No ways available for this square.';
  }
}

function makeClickable(text) {
  return text.replace(
    /(\d+_\d+)/g,
    '<span class="clickable-square" data-id="$1">$1</span>'
  );
}

waysDisplay.addEventListener('click', function (e) {
  if (e.target.classList.contains('clickable-square')) {
    const squareId = e.target.dataset.id;
    highlightSquare(squareId);
    displayWays(squareId);
  }
});

function highlightSquare(squareId) {
  // Remove active class from all squares
  document
    .querySelectorAll('.grid-square')
    .forEach((square) => square.classList.remove('active'));

  // Add active class to the clicked square
  const square = document.querySelector(`.grid-square[data-id="${squareId}"]`);
  if (square) {
    square.classList.add('active');
  }
}
