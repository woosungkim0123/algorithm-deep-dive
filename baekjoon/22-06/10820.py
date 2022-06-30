import sys

sys.stdin = open('10820.txt')

while True:
    words = sys.stdin.readline().rstrip('\n')
    if not words:
        break
    l, u, d, s = 0, 0, 0, 0
    for word in words:
        if word.islower():
            l += 1
        elif word.isupper():
            u += 1
        elif word.isdigit():
            d += 1
        elif word.isspace():
            s += 1

    print(l, u, d, s)
