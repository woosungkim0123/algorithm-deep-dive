def solution(n):
    string = str(n)
    answer = []
    for i in range(len(string)):
        answer.append(int(string[len(string) - 1 - i]))

    return answer


print(solution(12345))


# 다른 사람 풀이


def digit_reverse(n):
    return list(map(int, reversed(str(n))))
