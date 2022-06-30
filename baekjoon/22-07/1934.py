import sys
sys.stdin = open('1934.txt')

n = int(sys.stdin.readline())


def gcd(n, m):
    while m:
        n, m = m, n % m
    return n


for _ in range(n):
    answer = 1
    arr = list(map(int, sys.stdin.readline().split()))
    for j in arr:
        answer *= j // gcd(answer, j)

    print(answer)
