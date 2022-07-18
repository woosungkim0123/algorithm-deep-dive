
from collections import deque
import sys
sys.stdin = open('city.txt')

N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

print(N, M, K, X)
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)

distance = [-1] * (N + 1)
distance[X] = 0

q = deque([X])
print(q)

while q:
    now = q.popleft()
    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)

print(distance)
check = False
for i in range(N + 1):
    if distance[i] == K:
        check = True
        print(i)

if check == False:
    print(-1)
