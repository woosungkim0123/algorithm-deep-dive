def solution(s):
    asc = [int(ord(i)) for i in s]
    asc.sort(reverse=True)
    array = [chr(i) for i in asc]
    return "".join(array)


print(solution("ABDCEFvr"))
# vrFEDCBA


def solution(s):
    return ''.join(sorted(s, reverse=True))


print(solution("ABDCEFvr"))
