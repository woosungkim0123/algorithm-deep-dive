import sys
sys.stdin = open('17413.txt')

words = sys.stdin.readline().rstrip()
print(words)
a = ""
answer = ""
# 도전중
for i in range(len(words)):

    if words[i] == " " or i > len(words):
        answer += a[::-1]
        a = ""
    else:

        a += words[i]
    print(a)

print(answer)
