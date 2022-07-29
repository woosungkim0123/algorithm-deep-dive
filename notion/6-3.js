// 퀵정렬

let array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8];

function quick(array, start, end) {
  if (start >= end) {
    return;
  }
  let pivot = start;
  let left = start + 1;
  let right = end;

  while (left <= right) {
    while (left <= end && array[left] <= array[pivot]) {
      left += 1;
    }
    while (right > start && array[right] >= array[pivot]) {
      right -= 1;
    }
    if (left > right) {
      let temp = array[right];
      array[right] = array[pivot];
      array[pivot] = temp;
    } else {
      let temp = array[left];
      array[left] = array[right];
      array[right] = temp;
    }
  }
  quick(array, start, right - 1);
  quick(array, right + 1, end);
}
quick(array, 0, array.length - 1);

console.log(array);
