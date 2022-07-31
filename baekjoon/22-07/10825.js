let fs = require("fs");
let [n, ...arr] = fs.readFileSync("./10825.txt").toString().trim().split("\n");
//let [n, ...arr] = fs.readFileSync("/dev/stdin").toString().split("\n");
const names = [];
const result = arr
  .map((v) => v.split(" ").map((vv) => +vv || vv))
  .sort((a, b) => {
    console.log(a, b);
    if (a[1] < b[1]) return 1;
    else if (a[1] > b[1]) return -1;
    else {
      if (a[2] > b[2]) return 1;
      else if (a[2] < b[2]) return -1;
      else {
        if (a[3] < b[3]) return 1;
        else if (a[3] > b[3]) return -1;
        else {
          if (a[0] > b[0]) return 1;
          else if (a[0] < b[0]) return -1;
          else return 0;
        }
      }
    }
  });

result.forEach((v) => names.push(v[0]));

console.log(names.join("\n"));
