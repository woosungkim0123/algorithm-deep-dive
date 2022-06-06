import sys
sys.stdin = open('Q01.txt')


n = int(input())
# 5

data = list(map(int, input().split()))
# [2, 3, 1, 2, 2]
data.sort()
# [1, 2, 2, 2, 3]

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
