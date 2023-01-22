def solution(board, moves):
    backet = []
    count = 0
    for move in moves:
        pick = move - 1
        for list in board:
            if list[pick] != 0:
                if len(backet) != 0:
                    if backet[-1] == list[pick]:
                        backet.pop()
                        count += 2
                        list[pick] = 0
                        break
                backet.append(list[pick])
                list[pick] = 0
                break
    return count


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
      4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))


# 다른사람풀이

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19


def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break

    return answer
