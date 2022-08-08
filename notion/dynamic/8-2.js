const d = Array(100).fill(0);
/*
function fibo(x) {
  // 호출되는 함수
  console.log("f", x);
  if (x === 1 || x === 2) return 1;
  if (d[x] !== 0) return d[x];

  d[x] = fibo(x - 1) + fibo(x - 2);
  return d[x];
}

console.log(fibo(6));
*/
// 보텀업 방식 사용

d[1] = 1;
d[2] = 1;
const n = 6;

for (let i = 3; i < n + 1; i++) {
  d[i] = d[i - 1] + d[i - 2];
}
console.log(d[n]);
