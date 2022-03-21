for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        j = row.index(1)
        print(abs(2 - i) + abs(2 - j))
        break