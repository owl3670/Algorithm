from sys import stdin, stdout

input = stdin.readline


def print(val):
    stdout.write(f'{val}\n')


n = int(input())
a = list(map(int, input().split()))

even = []
odd = []
for idx, val in enumerate(a):
    if val % 2 == 0:
        even.append(idx + 1)
    else:
        odd.append(idx + 1)
    if len(even) > 1 and len(odd) == 1:
        print(odd[-1])
        break
    elif len(odd) > 1 and len(even) == 1:
        print(even[-1])
        break
