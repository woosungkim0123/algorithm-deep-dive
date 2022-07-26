let fs = require("fs");
let input = fs.readFileSync("./2644.txt").toString().split("\n");
//let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input.shift());
const [A, B] = input
  .shift()
  .split(" ")
  .map((v) => Number(v));
const m = Number(input.shift());

const grph = Array.from(Array(n + 1), () => new Array());

for (let i = 0; i < m; i++) {
  const [x, y] = input[i].split(" ").map((v) => Number(v));
  grph[x].push(y);
  grph[y].push(x);
}

const bfs = (graph, startNode, targetNode) => {
  const visited = [];
  let needVisit = [[startNode, 0]];
  console.log(needVisit);
  while (needVisit.length !== 0) {
    const [node, cnt] = needVisit.shift();
    if (node === targetNode) return cnt;
    if (!visited.includes(node)) {
      visited.push(node);
      let nodes = graph[node].map((e) => [e, cnt + 1]);
      needVisit = [...needVisit, ...nodes];
    }
  }

  return -1;
};

console.log(bfs(grph, A, B));
