from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n = int(input())
s = []

for _ in range(n):
    arr = list(map(int, input().split()))
    h = arr[0]
    a = arr[1]
    s.append((h, a))

cnt = 0
for s1 in s:
    for s2 in s:
        if s1[0] == s2[1]:
            cnt += 1

print(cnt)