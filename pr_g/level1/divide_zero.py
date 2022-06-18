def solution(arr, divisor):
    arr.sort()
    answer = list(i for i in arr if i % divisor == 0)
    print(answer)
    if len(answer) == 0:
        return [-1]
    return answer


print(solution([5, 9, 7, 10], 5))


# 다른 사람 풀이

def solution(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]
