from collections import deque

#n, m, k, x = map(int, input().split())
n = 4
m = 4
k = 2
x = 1

graph = [[] for _ in range(n+1)]


graph[1].append(2)
graph[1].append(3)
graph[2].append(3)
graph[2].append(4)
print(graph)

distance = [-1] * (n + 1)
distance[x] = 0
print(distance)

q = deque([x])

while q:
    now = q.popleft()

    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

print(distance)
check = False

for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
