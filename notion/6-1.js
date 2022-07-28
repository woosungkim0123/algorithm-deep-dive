// 선택정렬

let array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8];

for (let i = 0; i < array.length; i++) {
  min_index = i;
  for (let j = i + 1; j < array.length; j++) {
    if (array[min_index] > array[j]) {
      min_index = j;
    }
  }
  if (min_index !== i) {
    let swap = array[min_index];
    array[min_index] = array[i];
    array[i] = swap;
  }
}
console.log(array);
