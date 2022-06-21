from re import A


def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a = array[commands[i][0] - 1:commands[i][1]]
        a.sort()
        answer.append(a[commands[i][2] - 1])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
(lambda x, y: x + y)(10, 20)

# 다른사람 풀이


def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
