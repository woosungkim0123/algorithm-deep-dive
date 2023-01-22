def solution(n):
    answer = ""
    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else:
            answer += "박"
    return answer


solution(3)

# 다른사람풀이


def water_melon(n):
    return ("수박" * n)[:n]


print("수박" * 1)
