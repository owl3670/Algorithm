from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n, m = map(int, input().split())
a = list(map(int, input().split()))
t = 0
for i in range(m):
    if i == 0:
        t += a[0] - 1
    else:
        if a[i] >= a[i-1]:
            t += a[i] - a[i-1]
        else:
            t += n - a[i-1] + a[i]

print(t)