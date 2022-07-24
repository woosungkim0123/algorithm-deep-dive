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
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (squareMap[i][j] === 0) continue;
    count += 1;
  }
}
console.log(count);
