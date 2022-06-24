words = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
         'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def solution(s):
    for word in words:
        if s.find(word) != -1:
            s = s.replace(word, str(words[word]))

    return int(s)


solution("one4seveneight")


# 다른 사람 풀이

num_dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
