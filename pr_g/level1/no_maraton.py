import collections


def solution(participant, completion):
    dict = {}
    for name in participant:
        if dict.get(name):
            dict[name] += 1
        else:
            dict[name] = 1

    for name in completion:
        dict[name] -= 1

    for key in dict:

        if dict[key] > 0:
            return key


print(solution(["mislav", "stanko", "mislav", "ana"],
      ["stanko", "ana", "mislav"]))

# 다른사람 풀이


def solution(participant, completion):
    print(collections.Counter(completion))
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


print(solution(["mislav", "stanko", "mislav", "ana"],
      ["stanko", "ana", "mislav"]))
