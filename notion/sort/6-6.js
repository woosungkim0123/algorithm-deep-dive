// 계수정렬

const array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2];

let count = new Array(Math.max(...array) + 1).fill(0);

for (let i = 0; i < array.length; i++) {
  count[array[i]] += 1;
}
let result = "";
for (let i = 0; i < count.length; i++) {
  for (let j = 0; j < count[i]; j++) {
    result += `${i} `;
  }
}
console.log(result);
