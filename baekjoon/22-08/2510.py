import sys
sys.stdin = open('3460.txt')

read = sys.stdin.readline

n, m = map(int, read().rstrip().split())

array = []
for i in range(1, n+1):
    if n % i == 0:
        array.append(i)

if len(array) < m:
    print(0)
else:
    print(array[m - 1])
