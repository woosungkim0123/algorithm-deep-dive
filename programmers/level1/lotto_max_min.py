def solution(lottos, win_nums):
    win = [6, 6, 5, 4, 3, 2, 1]
    count = 0
    rank = 0

    while 0 in lottos:
        lottos.remove(0)
        count += 1
    for lotto in lottos:
        if lotto in win_nums:
            rank += 1

    return [win[rank + count], win[rank]]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))

# 다른사람 풀이


def solution(lottos, win_nums):

    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans], rank[ans]
