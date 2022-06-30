import sys
sys.stdin = open('14279.txt')


n = int(sys.stdin.readline().rstrip())
word = sys.stdin.readline().rstrip()
num_lst = [0] * n

for i in range(n):
    num_lst[i] = int(sys.stdin.readline().rstrip())


stack = []

for i in word:
    if 'A' <= i <= 'Z':
        stack.append(num_lst[ord(i)-ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+':
            stack.append(str1+str2)
        elif i == '-':
            stack.append(str1-str2)
        elif i == '*':
            stack.append(str1*str2)
        elif i == '/':
            stack.append(str1/str2)

print(format(stack[0], ".2f"))
