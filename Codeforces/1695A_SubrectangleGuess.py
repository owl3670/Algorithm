from sys import stdin, stdout

input = stdin.readline
print = stdout.write

from_left_upper = 0
from_right_upper = 1
from_left_lower = 2
from_right_lower = 3

n = int(input())

for _ in range(n):
    (height, width) = map(int, input().split())
    max_num = - (10**9) - 1
    h, w = 0, 0
    for i in range(height):
        for j, num in enumerate(list(map(int, input().split()))):
            if max_num < num:
               h, w = i, j
               max_num = num
    height += 1
    width += 1
    h += 1
    w += 1
    lst = [0, 0, 0, 0]
    lst[from_left_upper] = h * w
    lst[from_right_upper] = h * (width - w)
    lst[from_left_lower] = (height - h) * w
    lst[from_right_lower] = (height - h) * (width - w)

    print(f'{max(lst)}\n')