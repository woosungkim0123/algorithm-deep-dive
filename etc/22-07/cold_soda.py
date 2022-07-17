import sys
sys.stdin = open('cold_soda.txt')

# N x M 얼음틀

# 구멍 뚤린 부분은 0 칸막이가 존재하는 부분은 1

N, M = map(int, sys.stdin.readline().split())

print(N, M)

graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))


def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


result = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)
