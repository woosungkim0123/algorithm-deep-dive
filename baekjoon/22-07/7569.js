let fs = require("fs");
let input = fs.readFileSync("./7569.txt").toString().split("\n");
//let input = fs.readFileSync("/dev/stdin").toString().split("\n");

// [x, y, z]
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
let visit = [...Array(H)].map(() => [...Array(N)].map(() => Array(M).fill(0)));
let count = M * N * H;
let z = 0;
let answer;

// 초기 상태 세팅
for (let i = 0; i < input.length; i++) {
  let box = input[i].split(" ").map(Number);
  box.forEach((tomato, pos) => {
    if (tomato === 1) {
      queue.push([pos, i % N, z, 0]);
      visit[z][i % N][pos] = 1;
      count--;
    } else if (tomato === -1) {
      visit[z][i % N][pos] = 1;
      count--;
    }
  });
  if ((i + 1) % N === 0) ++z;
}

let idx = 0;
while (queue.length != idx) {
  const [x, y, z, pos] = queue[idx]; // shift 쓰면 시간초과됨
  for (let i = 0; i < ds.length; i++) {
    const xPos = x + ds[i][0];
    const yPos = y + ds[i][1];
    const zPos = z + ds[i][2];

    if (xPos < 0 || yPos < 0 || zPos < 0 || xPos >= M || yPos >= N || zPos >= H)
      continue;
    if (!visit[zPos][yPos][xPos]) {
      visit[zPos][yPos][xPos] = 1;
      queue.push([xPos, yPos, zPos, pos + 1]);
      count--;
    }
  }

  idx++;
  answer = pos;
}

console.log(count ? -1 : answer);
