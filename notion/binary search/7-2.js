// 이진 탐색
// 정렬되어 있어야 사용 가능

function binarySearch(array, target, start, end) {
  if (start > end) return "none";
  let mid = parseInt((start + end) / 2);
  if (array[mid] === target) {
    return mid;
  } else if (array[mid] > target) {
    return binarySearch(array, target, 0, mid - 1);
  } else {
    return binarySearch(array, target, mid + 1, end);
  }
}

const n = 10;
const target = 7;
const array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19];
const result = binarySearch(array, target, 0, n - 1);

if (result === "none") {
  console.log("원소 없음");
} else {
  console.log(result + 1);
}
