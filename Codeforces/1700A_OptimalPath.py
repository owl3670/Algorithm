from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = int(input())
for i in range(n):
    inputs = list(map(int, input().split()))
    nums = []
    width = inputs[1]
    height = inputs[0]
    sum_width = (0 + width) * (width + 1) // 2
    sum_height = (0 + (width * height)) * (height + 1) // 2
    print(f'{sum_width + sum_height - width}\n')