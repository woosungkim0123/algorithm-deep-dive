import sys
sys.stdin = open('17298.txt')

n = int(input())  # 4
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []


stack.append(0)
for i in range(1, n):  # 1,2,3
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(stack)  # [0, 1,2]

print(*answer)

# 4
# 9 5 4 8
