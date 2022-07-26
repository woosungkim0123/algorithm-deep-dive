let fs = require("fs");
let input = fs.readFileSync("./7569.txt").toString().split("\n");
//let input = fs.readFileSync("/dev/stdin").toString().split("\n");
/*
const [M, N, H] = input
  .shift()
  .split(" ")
  .map((v) => +v);
*/

const ds = [
  [-1, 0, 0],
  [1, 0, 0],
  [0, 1, 0],
  [0, -1, 0],
  [0, 0, 1],
  [0, 0, -1],
];
const [M, N, H] = input.shift().split(" ").map(Number);
let queue = [];
let visit = [...Array(H)].map((h) =>
  [...Array(N)].map((n) => Array(M).fill(0))
);
let count = M * N * H;
let z = 0;
let answer;

// 초기 상태 세팅
for (let i = 0; i < input.length; i++) {
  let box = input[i].split(" ").map(Number);
  console.log(box);
  box.forEach((tomato, pos) => {
    if (tomato === 1) {
      queue.push([i % N, pos, z, 0]);
      visit[z][i % N][pos] = 1;
      count--;
    } else if (tomato === -1) {
      visit[z][i % N][pos] = 1;
      count--;
    }
  });
  if ((i + 1) % N === 0) ++z;
}
