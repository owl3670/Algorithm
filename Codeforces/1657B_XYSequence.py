case = int(input())
for i in range(case):
    n, B, x, y = map(int, input().split())
    result = 0
    before = 0
    for j in range(n):
        if before + x <= B:
            before = before + x
            result += before
        else:
            before = before - y
            result += before
    print(result)
