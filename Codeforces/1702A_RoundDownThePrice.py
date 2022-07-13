from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = int(input())
for _ in range(n):
    num = int(input())
    round = 1
    while round <= num:
        round *= 10
    round //= 10
    print(f'{num - round}\n')
