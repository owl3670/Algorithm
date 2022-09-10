from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n = int(input())
ans = 0
for _ in range(n):
    s = input().strip()
    l = len(s)
    if l == 11:
        if s[0] == 'T':
            ans += 4
        else:
            ans += 20
    elif l == 4:
        ans += 6
    elif l == 10:
        ans += 8
    else:
        ans += 12

print(ans)