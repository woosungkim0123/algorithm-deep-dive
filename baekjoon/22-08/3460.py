import sys
sys.stdin = open('3460.txt')

read = sys.stdin.readline

n = int(read())

for i in range(n):
    m = bin(int(read())) + ""
    count = 0
    for j in range(len(m) - 1, 0, -1):
        if m[j] == '1':
            print(count, end=" ")
        count += 1
