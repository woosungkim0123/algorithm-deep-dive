def solution(n):
    result = ''
    while n:
        result += str(n % 3)
        n = n // 3

    return int(result, 3)


solution(45)

# 3진법 제대로 출력시 result[::-1]
# print(int(result[::-1], 3))
