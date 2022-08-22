from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

levels = [False] * (n + 1)
for lev in p[1:]:
    levels[lev] = True

for lev in q[1:]:
    levels[lev] = True

is_all_passed = True
for i in range(1, n + 1):
    if not levels[i]:
        is_all_passed = False
        print("Oh, my keyboard!")
        break

if is_all_passed:
    print("I become the guy.")
