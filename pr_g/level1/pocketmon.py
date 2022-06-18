def solution(nums):
    arr = set(nums)
    if len(arr) > len(nums) // 2:
        return len(nums) // 2
    else:
        return len(arr)


print(solution([3, 3, 3, 2, 2, 4]))


# 다른사람 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
