let fs = require("fs");
let input = fs.readFileSync("./7-4.txt").toString().trim().split("\n");

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

const [n, m] = input[0].split(" ").map((v) => +v);
const dduk = input[1].split(" ").map((v) => +v);
let start = 0;
let end = Math.max.apply(null, dduk);
let result = 0;

while (start <= end) {
  let total = 0;
  let mid = parseInt((start + end) / 2);
  for (let i = 0; i < dduk.length; i++) {
    if (dduk[i] > mid) {
      total += dduk[i] - mid;
    }
  }

  if (total < m) {
    end = mid - 1;
  } else {
    result = mid;
    start = mid + 1;
  }
}
console.log(result);
