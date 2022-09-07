import sys
sys.stdin = open('1018.txt')

input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

print(a, b)
