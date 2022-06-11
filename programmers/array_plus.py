
def solution(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list1[0])):
            list1[i][j] += list2[i][j]

    print(list1)

    return list1


solution([[1, 2], [2, 3]], [[3, 4], [5, 6]])


def sumMatrix(A, B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))


for a, b in zip([[1, 2], [2, 3]], [[3, 4], [5, 6]]):
    print(a)
    print(b)
