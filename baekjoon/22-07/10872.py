import sys
sys.stdin = open('1676.txt')

n = int(sys.stdin.readline())


result = 1
for i in range(1, n+1):
    result *= i

print(result)