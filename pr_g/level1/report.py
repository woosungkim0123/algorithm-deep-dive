
from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    user = defaultdict(set)
    cnt = defaultdict(int)
    for r in report:
        a, b = r.split()
        user[a].add(b)
        cnt[b] += 1

    for i in id_list:
        result = 0
        for u in user[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo",
                                                    "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))

# 다른사람 풀이


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        print(r)
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo",
                                                    "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
