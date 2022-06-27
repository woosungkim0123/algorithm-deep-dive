import sys
sys.stdin = open('1158.txt')

n, k = sys.stdin.readline().split()
answer = []
count = 0
arr = [i for i in range(1, int(n) + 1)]

for i in range(int(n)):
    count += int(k)-1
    if count >= len(arr):
        count = count % len(arr)
    answer.append(str(arr.pop(count)))
print("<", ", ".join(answer), ">", sep='')
