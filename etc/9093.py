import sys
sys.stdin = open('9093.txt')

input = sys.stdin.readline

n = int(input())


for _ in range(n):

    words = list(input().split())
    array = []

    for word in words:
        array.append(word[::-1])

    print(" ".join(array))
