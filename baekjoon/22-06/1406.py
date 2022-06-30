from audioop import reverse
import sys
sys.stdin = open('1406.txt')

str1 = list(sys.stdin.readline().rstrip())
# [a, b, c, d]
str2 = []
# []

command_count = int(sys.stdin.readline())

for _ in range(command_count):
    print('i')
    command = list(sys.stdin.readline().split())

    if command[0] == 'L':
        if str1:
            str2.append(str1.pop())
    elif command[0] == 'D':
        if str2:
            str1.append(str2.pop())
    elif command[0] == 'B':
        if str1:
            str1.pop()
    else:
        str1.append(command[1])

str1.extend(reversed(str2))
print(''.join(str1))
