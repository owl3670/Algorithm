import math

case = int(input())
for i in range(case):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        print(0)
    else:
        calc = math.sqrt(math.pow((x - 0), 2) + math.pow((y - 0), 2))
        int_calc = int(calc)
        if calc == int_calc:
            print(1)
        else:
            print(2)
