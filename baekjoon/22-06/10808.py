import sys

sys.stdin = open('10808.txt')
word = sys.stdin.readline().rstrip()
results = [0 for _ in range(ord('a'), ord('z') + 1)]

for i in word:
    results[ord(i) - ord('a')] += 1

print(*results)
