import sys
sys.stdin = open('10824.txt')

n = sys.stdin.readline().split()

print(int(n[0] + n[1]) + int(n[2] + n[3]))
