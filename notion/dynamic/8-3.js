const x = 26;

const array = new Array(30001).fill(0);

for (let i = 2; i < x + 1; i++) {
  array[i] = array[i - 1] + 1;
  if (i % 2 === 0) {
    array[i] = Math.min(array[i], array[parseInt(i / 2)] + 1);
  }
  if (i % 3 === 0) {
    array[i] = Math.min(array[i], array[parseInt(i / 3)] + 1);
  }
  if (i % 5 === 0) {
    array[i] = Math.min(array[i], array[parseInt(i / 5)] + 1);
  }
}

console.log(array[x]);
