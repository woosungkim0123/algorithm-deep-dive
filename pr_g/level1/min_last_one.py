
def solution(n):
    for i in range(1, n):
        if n % i == 1:
            return i


print(solution(10))

# 다른사람 풀이


def solution(n):
    return [x for x in range(1, n+1) if n % x == 1][0]
