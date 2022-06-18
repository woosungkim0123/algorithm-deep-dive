def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()


solution("1234")


def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False
