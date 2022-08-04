let fs = require("fs");
let input = fs.readFileSync("./7-3.txt").toString().trim().split("\n");
//let [n, ...arr] = fs.readFileSync("/dev/stdin").toString().split("\n");

function binarySearch(array, target, start, end) {
  while (start <= end) {}
  return "None";
}

const n = +input.shift();
console.log(n);
const array = input[0].split(" ").map((a) => +a);
array.sort();
console.log(array);
const m = +input[1];
console.log(m);
