import datetime


def solution(a, b):
    d = datetime.datetime(2016, a, b)
    return d.strftime('%a')


print(solution(10, 24))
