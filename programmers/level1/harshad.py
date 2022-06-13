
def solution(x):
    num_str = str(x)
    result = 0
    for i in range(len(num_str)):
        result += int(num_str[i])

    if x % result == 0:
        return True
    else:
        return False


solution(13)

# 다른 사람 답


def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Harshad(18))
