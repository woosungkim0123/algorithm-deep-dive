# 틀림 힙써야한데

import sys
sys.stdin = open('1655.txt')

read = sys.stdin.readline


n = int(read())

array = []

for i in range(1, n + 1):

    array.append(int(read()))
    array.sort()
    if i % 2 == 0:
        print(array[(i // 2) - 1])
    else:
        print(array[(i // 2)])
