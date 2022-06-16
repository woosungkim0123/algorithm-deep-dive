def solution(n):
    string = list(str(n))
    answer = 0
    for i in range(len(string)):
        answer += int(string[i])
    return answer


print(solution(123))

# 다른사람 풀이


def sum_digit(number):
    return sum([int(i) for i in str(number)])


def sum_digit(number):
    if number < 10:
        return number
    return (number % 10) + sum_digit(number // 10)
