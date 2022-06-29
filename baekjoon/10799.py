import sys
sys.stdin = open('10799.txt')

words = sys.stdin.readline().rstrip()

stack = []
result = 0
for i in range(len(words)):
    if words[i] == '(':
        stack.append(words[i])
    elif words[i] == ')':
        if words[i-1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1


print(result)
