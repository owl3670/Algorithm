from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]
f = list(map(int, input().split()))

f.sort()
result = 1000
for i in range(n - 1, len(f)):
    result = min(result, f[i] - f[i-(n-1)])

print(result)