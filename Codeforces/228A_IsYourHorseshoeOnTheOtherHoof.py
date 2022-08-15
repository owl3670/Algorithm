from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

s = list(map(int, input().split()))

di = {}
for val in s:
    if val in di:
        di[val] += 1
    else:
        di[val] = 1

print(4 - len(di.keys()))
