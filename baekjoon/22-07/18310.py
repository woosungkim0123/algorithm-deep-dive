from collections import deque
import sys
sys.stdin = open('18310.txt')
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

print(arr[(n - 1) // 2])
