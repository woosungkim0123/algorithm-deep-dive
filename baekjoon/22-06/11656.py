import sys
sys.stdin = open('11656.txt')


word = sys.stdin.readline().rstrip()
array = list(word[i: len(word)] for i in range(len(word)))
array.sort()
for word in array:
    print(word)
