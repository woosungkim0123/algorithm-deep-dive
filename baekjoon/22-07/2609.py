import sys
sys.stdin = open('2609.txt')

arr = list(map(int, sys.stdin.readline().split()))


def gcd(n, m):
    while m:
        n, m = m, n % m  # 나머지
    return n


print(gcd(arr[1], arr[0]))


def solution(arr1):
    answer = 1

    # 최대공약수를 구하고 최소 공배수를 구하려면?
    for i in arr1:
        answer *= i//gcd(answer, i)  # 몫

    return answer


print(solution(arr))
