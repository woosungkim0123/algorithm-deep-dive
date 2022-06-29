import sys
sys.stdin = open('17299.txt')

n = sys.stdin.readline().rstrip()
print(n)
m = list(map(int, input().split()))
print(m)
