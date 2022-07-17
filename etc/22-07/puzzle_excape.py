from collections import deque
import sys
sys.stdin = open('puzzle_excape.txt')

# N x M 얼음틀

# 구멍 뚤린 부분은 0 칸막이가 존재하는 부분은 1

N, M = map(int, sys.stdin.readline().split())

print(N, M)

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

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

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1]


print(bfs(0, 0))
