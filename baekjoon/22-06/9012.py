import sys
sys.stdin = open('9012.txt')

n = int(input())

for _ in range(n):
    words = input()
    count = 0
    if len(words) % 2 != 0:
        print('NO')
        continue
    for word in words:
        if word == "(":
            count += 1
        else:
            count -= 1

        if count < 0:
            break

    if count == 0:
        print("YES")
    else:
        print("NO")
