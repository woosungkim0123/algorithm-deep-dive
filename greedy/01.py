# 거스름돈
# 500, 100, 50, 10
# 거슬러 주는 돈 N원
# 동전 최소 개수
# 거슬러 주는 돈 N은 항상 10의 배수

# 화폐 개수(K) 만큼 반복 0(K)

n = 1260
count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin
    n %= coin


print(count)
