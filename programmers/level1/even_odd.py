def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(solution(4))


# 다른사람
def solution1(num):
    return "Odd" if num % 2 else "Even"


print(solution1(4))
