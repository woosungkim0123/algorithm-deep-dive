import sys
sys.stdin = open('11655.txt')

words = sys.stdin.readline().rstrip()
print(words[3])
result = ""
for word in words:
    if word.isalpha():
        if word.isupper():
            print('U')
            print(word)
        else:
            print('L')
            print(word)

        result += chr(ord(word) + 13)
    else:
        result += word

print(result)
