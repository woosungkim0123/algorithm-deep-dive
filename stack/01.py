import sys
sys.stdin = open('01.txt')


n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    data = sys.stdin.readline().split()
    order = data[0]
    if order == 'push':
        stack.append(data[1])
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order == 'top':
        if len(stack) == 0:
            print(-1)

        else:
            print(stack[-1])
