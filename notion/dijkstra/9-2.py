import sys
import heapq

sys.stdin = open('9-1.txt')
read = sys.stdin.readline

INF = int(1e9)
n, m = map(int, read().split())

start = int(input())

graph = [[] for i in range(n + 1)]  # 일부러 하나 더 만들어서 인덱스 맞춤
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

print(graph)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    distance[start] = 0

    while q:

        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            print(q)
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
