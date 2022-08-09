const x = 4;
const array = [1, 3, 1, 5];

const d = new Array(100).fill(0);

d[0] = array[0];
d[1] = Math.max(array[0], array[1]);

for (let i = 2; i < x; i++) {
  d[i] = Math.max(d[i - 1], d[i - 2] + array[i]);
}

console.log(d[x - 1]);
