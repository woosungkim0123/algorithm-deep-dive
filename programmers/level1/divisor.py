def solution(n):
    return sum(i for i in range(1, n + 1) if n % i == 0)


print(solution(12))


# 다른사람풀이

def solution(n):
    return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])
