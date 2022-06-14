def com_div(n, m):
    while m > 0:
        temp = m
        m = n % m
        n = temp
    return n


def com_mul(n, m):
    return (n * m) / com_div(n, m)


def solution(n, m):
    max_n = max(n, m)
    min_n = min(n, m)
    return [com_mul(min_n, max_n), com_div(min_n, max_n)]


print(solution(3, 12))


# 다른 사람 풀이
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
        print(c, d)
    answer = [c, int(a*b/c)]

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(23, 5))
