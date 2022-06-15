def solution(array):
    if len(array) == 1:
        return [-1]
    array.pop(array.index(min(array)))
    return array


print(solution([4, 3, 2, 1]))

# 다른사람 코드


def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]
