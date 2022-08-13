# 지금은 이해헀는데 다음에 한번더 보자
# 배낭
import sys
sys.stdin = open('12865.txt')

read = sys.stdin.readline


def solve():
    n, k = [int(x) for x in read().split()]
    table = [0] * (k + 1)

    for _ in range(n):
        w, v = [int(x) for x in read().split()]
        if w <= k:  # 예외처리 w가 k보다 높아서 에러가 뜸
            for j in range(k, 0, -1):

                if j + w <= k and table[j] != 0:  # k 안에 들어와야함
                    table[j + w] = max(table[j + w], table[j] + v)
            table[w] = max(table[w], v)  # if문이 없으면 이 부분이 에러

    print(max(table))


solve()
