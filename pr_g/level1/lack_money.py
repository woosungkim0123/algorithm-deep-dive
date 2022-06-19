def solution(price, money, count):
    sum_price = 0
    for i in range(1, count + 1):
        sum_price += price * i

    if sum_price > money:
        return sum_price - money
    else:
        return 0


print(solution(3, 20, 4))  # 10

# 다른사람 풀이


def solution(price, money, count):
    return max(0, price*(count+1)*count//2-money)


print(solution(3, 20, 4))
# price *
# 1~ n 까지 정수합 수학 => n(n+1) // 2
# 3 (1 + 2 + 3 + 4)
