
import sys
sys.stdin = open('18185.txt')

read = sys.stdin.readline


def buy_three(idx):
    global cost
    k = min(arr[idx: idx + 3])
    arr[idx] -= k
    arr[idx + 1] -= k
    arr[idx + 2] -= k
    cost += 7 * k


def buy_two(idx):
    global cost
    k = min(arr[idx: idx + 2])
    arr[idx] -= k
    arr[idx + 1] -= k
    cost += 5 * k


def buy_one(idx):
    global cost
    cost += 3 * arr[idx]


n = int(read().rstrip())

arr = list(map(int, read().rstrip().split())) + [0, 0]
cost = 0

for i in range(n):
    if arr[i + 1] > arr[i + 2]:
        k = min(arr[i], arr[i + 1] - arr[i + 2])
        arr[i] -= k
        arr[i + 1] -= k
        cost += 5 * k

        buy_three(i)

    else:

        buy_three(i)
        buy_two(i)

    buy_one(i)

print(cost)
