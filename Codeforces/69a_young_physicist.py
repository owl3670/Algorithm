case = int(input())
suma, sumb, sumc = 0, 0, 0
for i in range(case):
    a, b, c = map(int, input().split())
    suma += a
    sumb += b
    sumc += c
if (suma, sumb, sumc) == (0, 0, 0):
    print('YES')
else:
    print('NO')