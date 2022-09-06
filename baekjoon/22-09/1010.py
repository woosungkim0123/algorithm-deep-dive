import sys
sys.stdin = open('1010.txt')

testcase = int(sys.stdin.readline().rstrip())


def fac(n):
    if n == 0 or n == 1:
        return 1

    return n * fac(n-1)


def comb(a, b):
    return int(fac(a) / (fac(b) * fac(a-b)))


def solve():
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(comb(b, a))


for _ in range(testcase):
    solve()


# n! / (n-r)! 모든 경우의 수
# n! / (r! * (n-r)!) // 순서가 정해진 경우의수
