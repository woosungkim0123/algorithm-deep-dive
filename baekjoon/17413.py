import sys
sys.stdin = open('17413.txt')

words = sys.stdin.readline().rstrip()

tag = False
word = ''
result = ''
for i in words:
    # 뒤집어서 출력
    if tag == False:
        if i == '<':
            tag = True
            word += i
        # 중간점검
        elif i == ' ':
            word += i
            result = result+word
            word = ''
        else:
            word = i+word

    # 정상적으로 출력
    elif tag == True:
        word = word+i
        if i == '>':
            tag = False
            result = result+word
            word = ''

print(result+word)
