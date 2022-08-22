from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n = int(input())
a = list(map(int, input().split()))

min_idx = 0
min = a[0]
for i, v in enumerate(a):
    if v <= min:
        min = v
        min_idx = i

max_idx = n - 1
max = a[-1]
for i, v in enumerate(a[::-1]):
    if v >= max:
        max = v
        max_idx = n - 1 - i

print(max_idx)
print(min_idx)
if min_idx < max_idx:
    print(max_idx + (n - min_idx - 1) - 1)
else:
    print(max_idx + (n - min_idx - 1))