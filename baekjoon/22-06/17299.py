import sys
from collections import Counter

sys.stdin = open('17299.txt')

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
nums_count = Counter(nums)
print(nums_count)
result = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and nums_count[nums[stack[-1]]] < nums_count[nums[i]]:
        result[stack.pop()] = nums[i]
    stack.append(i)


print(*result)

# 4
# 9 5 4 8
