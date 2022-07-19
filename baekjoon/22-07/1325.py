
from collections import deque
import sys
sys.stdin = open('1325.txt')

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[y].append(x)

maxCnt = 1
ans = []


def bfs(start):
    q = deque([start])
    count = 1
    visit = [False for _ in range(n+1)]
    visit[start] = True
    while q:
        num = q.popleft()
        for nx in graph[num]:
            if not visit[nx]:
                visit[nx] = True
                count += 1
                q.append(nx)
    return count


for j in range(1, n+1):
    cnt = bfs(j)
    if cnt > maxCnt:
        maxCnt = cnt
        ans.clear()
        ans.append(j)
    elif cnt == maxCnt:
        ans.append(j)

print(*ans)
