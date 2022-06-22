from itertools import combinations


def sosu(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def solution(nums):
    count = 0
    array = [sum(num) for num in combinations(nums, 3)]
    print(array)
    for i in array:
        if sosu(i):
            count += 1
    return count


print(solution([1, 2, 3, 4]))

# 다른사람풀이

# else문을 for문과 같은 줄에 쓰게되면,
# for문의 반복이 끝나고나서 else문이 실행되게 됩니다(break로 빠져나가지 않는다면)


def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand % j == 0:
                break
        else:
            answer += 1
    return answer
