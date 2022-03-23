case = int(input())
for i in range(case):
    input()
    brackets = input()
    remain = []
    stack = []
    reverse = []
    cnt = 0
    for bracket in brackets:
        remain.append(bracket)

        if bracket == '(':
            stack.append(bracket)
        else:
            if len(stack) != 0:
                t = stack.pop()
                if t != '(':
                    stack.append(t)
                if len(stack) == 0:
                    remain.clear()
                    cnt += 1
                    continue
            else:
                stack.append(bracket)

        if len(remain) >= 2:
            if bracket == remain[0]:
                remain.clear()
                stack.clear()
                cnt += 1
    print(f'{cnt} {len(remain)}')
