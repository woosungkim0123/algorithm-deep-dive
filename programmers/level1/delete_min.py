def solution(array):
    if len(array) == 1:
        return [-1]
    array.pop(array.index(min(array)))
    return array


print(solution([4, 3, 2, 1]))
