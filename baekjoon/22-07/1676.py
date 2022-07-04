import sys
sys.stdin = open('1676.txt')

n = int(sys.stdin.readline())

count = 0
while n >= 5:
    count += n // 5
    n //= 5

print(count)