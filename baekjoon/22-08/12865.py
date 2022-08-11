import sys
sys.stdin = open('12865.txt')

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
print(n, k)
dp = [0] * (k + 1)
for _ in range(n):
    w, v = map(int, input().split())
    print(w, v)
