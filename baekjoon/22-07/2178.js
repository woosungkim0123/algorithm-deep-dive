// 로컬에서 테스트
let fs = require("fs");
let input = fs.readFileSync("./2178.txt").toString().trim();
input = input.split("\n");

const sol = (input) => {
  const [N, M] = input[0].split(" ").map((v) => Number(v));
  const graph = [];
  for (let i = 1; i <= N; i++)
    graph.push(
      input[i]
        .replace(/\r/g, "")
        .split("")
        .map((v) => Number(v))
    );

  function bfs(x, y) {
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];
    const queue = [];
    queue.push([x, y]);
    while (queue.length) {
      const [x, y] = queue.shift();
      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y + dy[i];
        if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
        if (graph[nx][ny] === 0) continue;
        if (graph[nx][ny] === 1) {
          graph[nx][ny] = graph[x][y] + 1;
          queue.push([nx, ny]);
        }
      }
    }
  }
  bfs(0, 0);
  return graph[N - 1][M - 1];
};
console.log(sol(input));
/*
// 백준 제출 코드
const input = [];
require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", (line) => {
    input.push(line);
  })
  .on("close", () => {
    console.log(sol(input));
    process.exit();
  });
*/
