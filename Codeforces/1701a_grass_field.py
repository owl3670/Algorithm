from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = int(input())
for _ in range(n):
    cnt = 0
    for _ in range(2):
        for val in input().split():
            if val == '1':
                cnt += 1
    print(f'{max(cnt // 2, cnt % 2)}\n')