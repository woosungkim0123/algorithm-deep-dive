
from collections import deque
import sys
sys.stdin = open('3197.txt')

read = sys.stdin.readline

maps = []
birds = []
R, C = map(int, read().split())

# 백조위치, 맵
for i in range(R):
    arr = list(read().strip())
    maps.append(arr)
    for x in range(len(arr)):
        if arr[x] == "L":
            birds.append((i, x))

# 녹는 시간
time = [[0 for _ in range(C)] for _ in range(R)]

print(time)


def melt_time_set(maps):
    visited = [[False for _ in range(C)] for _ in range(R)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque()
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == '.' or maps[y][x] == 'L':
                queue.append((y, x))
                time[y][x] = 0
                visited[y][x] = True

    last_time = 0

    while queue:
        y, x = queue.popleft()
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx] and maps[ny][nx] != "L":
                queue.append((ny, nx))
                time[ny][nx] = time[y][x] + 1
                visited[ny][nx] = True
                last_time = time[ny][nx]

    return last_time


def bfs(start, maps, mid, end):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()
    queue.append(start)
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]

    while queue:
        y, x = queue.popleft()
        visited[y][x] = True
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx]:
                visited[ny][nx] = True
                if ny == end[0] and nx == end[1]:
                    return True
                if time[ny][nx] <= mid:
                    queue.append((ny, nx))

    return False


min, max = 0, melt_time_set(maps)

answer = max

while min <= max:
    mid = (min + max) // 2
    if bfs(birds[0], maps, mid, birds[1]):
        answer = mid
        max = mid - 1
    else:
        min = mid + 1

print(answer)
