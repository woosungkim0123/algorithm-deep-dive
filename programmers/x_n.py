
def solution(x, n):
    answer = []
    plus_x = 0
    for _ in range(n):
        plus_x += x
        answer.append(plus_x)

    return answer


print(solution(2, 5))
