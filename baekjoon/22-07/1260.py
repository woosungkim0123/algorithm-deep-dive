# 22-07-21 [1, 2]


from collections import deque
import sys
sys.stdin = open('1260.txt')

input = sys.stdin.readline

n, m, v = map(int, input().rstrip().split())


graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(len(graph)):
    graph[i].sort()


visited = [False] * (n+1)


def dfs(start):
    print(start, end=" ")
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        num = q.popleft()
        print(num, end=" ")
        for i in graph[num]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


dfs(v)
visited = [False] * (n+1)
print()
bfs(v)
