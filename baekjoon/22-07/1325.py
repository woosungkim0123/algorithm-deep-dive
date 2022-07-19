from collections import deque

import sys
sys.stdin = open('1325.txt')

n = int(sys.stdin.readline().rstrip())
l = int(sys.stdin.readline().rstrip())
print(n, l)
graph = [[False] * l for _ in range(l)]

x, y = map(int, sys.stdin.readline().rstrip().split())
graph[x][y] = True

print(graph)
