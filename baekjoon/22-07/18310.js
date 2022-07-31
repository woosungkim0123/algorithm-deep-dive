let fs = require("fs");
let input = fs.readFileSync("./18310.txt").toString().trim().split("\n");
//let [n, ...arr] = fs.readFileSync("/dev/stdin").toString().split("\n");
const n = +input.shift();
const house = input
  .toString()
  .split(" ")
  .map((v) => +v)
  .sort();
console.log(house[(n - 1) % 2]);
