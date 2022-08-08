from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n = int(input())
before = ''
cnt = 0
for _ in range(n):
    i = input()
    if before != i:
        cnt += 1
    before = i
print(cnt)
