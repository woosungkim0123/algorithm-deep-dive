import sys
sys.stdin = open('1158.txt')

n, k = sys.stdin.readline().rstrip().split()
list = []
count = 0
numbers = [i for i in range(1, int(n) + 1)]

# 도전중
while numbers:
   if count >= 6:
        count = count - 6

    count += 2

    list.append(numbers[count])
    del numbers[count]
    print(numbers)

print(numbers)
# while len(numbers) == 0:
