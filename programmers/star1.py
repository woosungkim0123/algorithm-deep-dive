import sys
sys.stdin = open('star1.txt')

a, b = map(int, sys.stdin.readline().strip().split(' '))

result = ""
for _ in range(b):
    for _ in range(a):
        result += '*'
    print(result)
    result = ""


# 가장 효율적인 방법
answer = ('*'*a + '\n')*b
print(answer)
