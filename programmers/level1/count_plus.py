def solution(left, right):
    result = 0
    for i in range(left, right + 1):
        count = 0

        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count % 2 == 0:
            result += i
        else:
            result -= i
    return result


print(solution(13, 17))


# 다른 사람 풀이
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if int(i**0.5) == i**0.5:
            print(int(i**0.5))
            print(i**0.5)
            answer -= i
        else:
            print(int(i**0.5))
            print(i**0.5)
            answer += i
    return answer


print(solution(13, 17))
