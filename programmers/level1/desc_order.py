def solution(n):
    word = str(n)
    list = []
    for i in word:
        list.append(i)
    list.sort(reverse=True)

    string = "".join(list)
    return int(string)


print(solution(118372))

# 다른 사람풀이


def solution(n):
    ls = list(str(n))
    ls.sort(reverse=True)
    return int("".join(ls))
