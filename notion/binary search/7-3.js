let fs = require("fs");
let input = fs.readFileSync("./7-3.txt").toString().trim().split("\n");
//let [n, ...arr] = fs.readFileSync("/dev/stdin").toString().split("\n");

function binarySearch(array, target, start, end) {
  while (start <= end) {
    let mid = parseInt((start + end) / 2);
    if (array[mid] === target) {
      return mid;
    } else if (array[mid] > target) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return "None";
}

const n = +input.shift();

const array = input[0].split(" ").map((a) => +a);
array.sort();
const m = +input[1];
const x = input[2].split(" ").map((a) => +a);

for (let i = 0; i < x.length; i++) {
  let result = binarySearch(array, x[i], 0, n - 1);

  if (result !== "None") {
    process.stdout.write("yes");
  } else {
    process.stdout.write("no");
  }
  process.stdout.write(" ");
}
