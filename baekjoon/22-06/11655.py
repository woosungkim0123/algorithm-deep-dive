import sys
sys.stdin = open('11655.txt')

words = sys.stdin.readline().rstrip()
result = ""
for word in words:
    if word.isalpha():
        if word.isupper():
            trans_word = ord(word) + 13
            if trans_word > ord('Z'):
                result += chr(trans_word - ord('Z') + ord('A') - 1)
            else:
                result += chr(trans_word)
        else:
            trans_word = ord(word) + 13
            if trans_word > ord('z'):
                result += chr(trans_word - ord('z') + ord('a') - 1)
            else:
                result += chr(trans_word)

    else:
        result += word

print(result)
