def solution(absolutes, signs):
    sum = 0

    for i in range(len(absolutes)):
        if signs[i]:
            sum += absolutes[i]
        else:
            sum += absolutes[i] * -1
    return sum


print(solution([4, 7, 12], [True, False, True]))

# 다른사람


def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
