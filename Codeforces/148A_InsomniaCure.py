from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.writeline(f'{val}\n')

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

damaged = [False] * (d + 1)
li = [k, l, m, n]
cnt = 0
for v in li:
    for i in range(v, d, v):
        if damaged == False:
            damaged[i] = True
            cnt += 1

print(cnt)
