from collections import deque
import sys
sys.stdin = open('10845.txt')

command_count = int(sys.stdin.readline().rstrip())

dq = deque()
for _ in range(command_count):
    command = sys.stdin.readline().rstrip().split()

    if command[0] == "push":
        dq.append(command[1])
    elif command[0] == "pop":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif command[0] == "size":
        print(len(dq))
    elif command[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif command[0] == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
