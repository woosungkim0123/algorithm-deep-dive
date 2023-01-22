import math


def solution(n):
    print(n)
    if math.sqrt(n).is_integer():
        return math.trunc((math.sqrt(n) + 1) * (math.sqrt(n) + 1))
    return -1


print(solution(121))


# 다른사람 풀이
def nextSqure(n):
    sqrt = n ** (1/2)
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'


print(nextSqure(3))
