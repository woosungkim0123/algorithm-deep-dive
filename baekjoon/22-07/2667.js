let fs = require("fs");
let input = fs.readFileSync("./2667.txt").toString().split("\n");
//let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input.shift());

const squareMap = [];

for (let i = 0; i < n; i++) {
  squareMap.push(
    input[i]
      .replace(/\r/g, "")
      .split("")
      .map((v) => Number(v))
  );
}
console.log(squareMap);

let count = 0;
let sizeArray = [];
let size = 0;
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
const dfs = (x, y) => {
  squareMap[x][y] = 0;
  size += 1;
  for (let i = 0; i < 4; i++) {
    let nx = x + dx[i];
    let ny = y + dy[i];
    if (nx >= 0 && ny >= 0 && (nx < n) & (ny < n)) {
      if (squareMap[nx][ny] !== 0) {
        dfs(nx, ny);
      }
    }
  }
};

for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (squareMap[i][j] === 1) {
      count += 1;
      size = 0;
      dfs(i, j);
      sizeArray.push(size);
    }
  }
}
console.log(count);
sizeArray.sort((a, b) => a - b).forEach((x) => console.log(x));
