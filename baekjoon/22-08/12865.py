import sys
sys.stdin = open('12865.txt')

read = sys.stdin.readline


def solve():
    n, k = [int(x) for x in read().split()]
    table = [0] * (k + 1)

    for _ in range(n):
        w, v = [int(x) for x in read().split()]
        for j in range(k, 0, -1):

            if j + w <= k and table[j] != 0:  # k 안에 들어와야함
                table[j + w] = max(table[j + w], table[j] + v)
        table[w] = max(table[w], v)
        print(table)

    print(max(table))


solve()
