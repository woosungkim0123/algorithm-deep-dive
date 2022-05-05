array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

result = sorted(array)

print(result)

array.sort()

print(array)

array_key = [('바나나', 2), ('메론', 10), ('사과', 4), ('당근', 3), ('고추', 1)]


def setting(data):
    return data[1]


result = sorted(array_key, key=setting)

print(result)
