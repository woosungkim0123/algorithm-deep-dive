def solution(s):
    answer = ''
    new_list = s.split(' ')
    print(new_list)
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
        print(answer)
    return answer[0:-1]


print(solution("try  hello  world"))
