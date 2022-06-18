
def solution(s):
    index = len(s) // 2
    if len(s) % 2 == 0:
        return s[index-1] + s[index]
    else:
        return s[index]


solution("abcd")


# 다른 사람 풀이
def solution(str):
    return str[(len(str)-1)//2:len(str)//2+1]
