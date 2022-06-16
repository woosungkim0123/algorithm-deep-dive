def solution(s, n):
    answer = ""
    for i in s:
        if i != " ":
            if ord(i) + n > 122:
                answer += chr(ord(i) + n - 26)
            elif ord(i) >= 65 and ord(i) <= 90 and ord(i) + n > 90:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
        else:
            answer += i
    return answer


solution("a B z", 4)
