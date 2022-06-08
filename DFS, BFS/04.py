from collections import deque
import sys
sys.stdin = open('04.txt')

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                print('들어옴?')
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                print(queue)
    return graph[n-1][m-1]


print(bfs(0, 0))
