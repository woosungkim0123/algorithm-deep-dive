const n = 5;
const k = 3;
const array = [
  [1, 2, 5, 4, 3],
  [5, 5, 6, 6, 5],
];
array[0].sort();
array[1].sort();

for (let i = 0; i < k; i++) {
  if (array[0][i] < array[1][n - 1 - i]) {
    array[0][i] = array[1][n - 1 - i];
  } else {
    break;
  }
}

const result = array[0].reduce((sum, current) => {
  return sum + current;
});
console.log(result);
