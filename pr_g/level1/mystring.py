def solution(strings, n):
    array = []
    for string in strings:
        array.append(string[n] + string)
    array.sort()
    return [i[1:] for i in array]


print(solution(["sun", "bed", "car", "cad"], 1))


# 다른 사람 풀이

def strange_sort(strings, n):
    #'''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])


strings = ["sun", "bed", "car"]
print(strange_sort(strings, 1))
