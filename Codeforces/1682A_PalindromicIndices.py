from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = int(input())

for _ in range(n):
    length = int(input())
    mid = length // 2

    str = input()[:mid][::-1] if length % 2 == 0 else input()[:mid+1][::-1]
    cnt = 0
    for c in str:
        if c == str[0]:
            cnt += 1
        else:
            break
    print(f'{cnt * 2 if length % 2 == 0 else cnt * 2 - 1}\n')