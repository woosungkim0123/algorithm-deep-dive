def solution(dartResult):
    dartResult = dartResult.replace("10", "A")
    bonus = {"S": 1, "D": 2, "T": 3}
    stack = []
    for i in dartResult:
        if i.isdigit() or i == "A":
            stack.append(10 if i == 'A' else int(i))
            print(stack)
        elif i in bonus:
            num = stack.pop()
            stack.append(num ** bonus[i])
        elif i == '#':
            stack[-1] *= -1
        elif i == '*':
            num = stack.pop()
            if len(stack):
                stack[-1] *= 2
            stack.append(2 * num)

    return sum(stack)


print(solution("1D2S#10S"))
