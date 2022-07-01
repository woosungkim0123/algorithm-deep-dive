import sys
sys.stdin = open('1978.txt')

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
count = 0
print(numbers)


def demical(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for num in numbers:
    if demical(num):
        count += 1

print(count)
