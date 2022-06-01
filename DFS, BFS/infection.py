from collections import deque


input_data1 = '3 3'

n, m = map(int, input_data1.split())

data = []
virus_info = []

input_data2 = ['1 0 2', '0 0 0', '3 0 0']

for i in range(n):
    data.append(list(map(int, input_data2[i].split())))
    for j in range(n):
        if data[i][j] != 0:
            virus_info.append((data[i][j], 0, i, j))

virus_info.sort()
q = deque(virus_info)

target = '2 3 2'
target_s, target_x, target_y = map(int, target.split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:

    virus, s, x, y = q.popleft()

    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < m:

            if data[nx][ny] == 0:
                data[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(data[target_x - 1][target_y - 1])
