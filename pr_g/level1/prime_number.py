def solution(n):
    num = set(range(2, n+1))  # {2, 3, 4, 5, 6, 7, 8, 9, 10}
    for i in range(2, n+1):
        a = set(range(i*2, n+1, i))
        print(a)
        num -= a
        print(num)

    return len(num)


solution(10)
