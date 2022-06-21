def solution(participant, completion):
    if len(participant) > len(completion):
        participant, completion = completion, participant
    for parti in participant:
        if parti not in completion:
            return parti


print(solution(["mislav", "stanko", "mislav", "ana"],
      ["stanko", "ana", "mislav"]))
