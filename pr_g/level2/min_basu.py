
import math


def solution(arr):
    answer = 1
    # 유클리드 호재법을 이용한 최대공약수 구하기 함수

    def gcd(n, m):
        while m:
            n, m = m, n % m  # 나머지
        return n
    # 최대공약수를 구하고 최소 공배수를 구하려면?
    for i in arr:
        answer *= i//gcd(answer, i)  # 몫
        print(answer)

    return answer


print(solution([2, 6]))


# 다른사람풀이


def nlcm(num):
    answer = num[0]
    for n in num:
        answer = (n * answer) // math.gcd(n, answer)

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2, 6, 8, 14]))

print(6 % 2)
