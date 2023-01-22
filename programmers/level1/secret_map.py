def solution(n, arr1, arr2):
    stack = []

    for i in range(n):
        bin_result = str(int(bin(arr1[i])[2:]) +
                         int(bin(arr2[i])[2:])).zfill(n)
        string = ""
        for i in str(bin_result):
            if i == '0':
                string += " "
            else:
                string += "#"
        stack.append(string)

    return stack


print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))

# 다른 사람 풀이


def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    return answer
