
from itertools import combinations


def solution(numbers):
    # sorted를 앞에 써줘야함
    # 왜냐하면 list(set(a))는 정렬된 리스트가 나옴을 보장하지 않습니다.
    # 왜냐하면 Python의 set은 해시셋이기 때문입니다.
    return sorted(list(set(x+y for x, y in combinations(numbers, 2))))


print(solution([2, 1, 3, 4, 1]))
