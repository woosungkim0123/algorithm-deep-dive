import sys
sys.stdin = open('10809.txt')

word = sys.stdin.readline().rstrip()
list = [-1 for _ in range(ord('a'), ord('z')+1)]

for i in word:
    list[ord(i) - ord('a')] = word.index(i)

print(*list)
