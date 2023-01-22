def solution(a, b):
    if a == b:
        return a

    return sum(range(min(a, b), max(a, b) + 1))


print(solution(3, 5))


def adder(a, b):
    # 함수를 완성하세요
    if a > b:
        a, b = b, a

    return sum(range(a, b+1))
