def solution(answers):
    answer = []
    person = [0] * 3
    supoja = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(len(answers)):
        if answers[i] == supoja[0][i % 5]:
            person[0] += 1
        if answers[i] == supoja[1][i % 8]:
            person[1] += 1
        if answers[i] == supoja[2][i % 10]:
            person[2] += 1

    max_count = max(person)
    for i in range(len(person)):
        if person[i] == max_count:
            answer.append(i + 1)

    return answer
