let fs = require("fs");
let input = fs.readFileSync("./2606.txt").toString().split("\n");
//let input = fs.readFileSync("/dev/stdin").toString().split("\n");

const bfs = (graph, startNode) => {
  const visited = [];
  let needVisit = [];

  needVisit.push(startNode);

  while (needVisit.length !== 0) {
    const node = needVisit.shift();
    if (!visited.includes(node)) {
      visited.push(node);
      needVisit = [...needVisit, ...graph[node]];
    }
  }

  return visited;
};

let N = Number(input.shift());
let M = Number(input.shift());
let grph = [...Array(N + 1)].map((e) => []);

for (let i = 0; i < M; i++) {
  let [x, y] = input[i].split(" ").map(Number);
  grph[x].push(y);
  grph[y].push(x);
}

console.log(bfs(grph, 1).length - 1);
