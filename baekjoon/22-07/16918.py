
from collections import deque
import sys
sys.stdin = open('16918.txt')
input = sys.stdin.readline

r, c, n = map(int, input().split())
board = [list(input().strip()) for i in range(r)]
zero_board = board = [[0] * r for _ in range(r)]
count = 1
q = []
print(board)
while count != 3:
    if count == 1:
        q = deque()
        for i in range(r):
            for j in range(c):
                if board[i][j] != ".":
                    print(i, j)
                    q.append((i, j))

        count += 1
    elif count == 2:
        board = zero_board
    elif count == 3:
        while q:
            x, y = q.popleft()
            print(x, y)
