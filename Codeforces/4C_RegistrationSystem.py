from sys import stdin, stdout

input = stdin.readline
def prin(val):
    stdout.write(f'{val}\n')

names = {}
n = int(input())
for _ in range(n):
    name = input().replace('\n', '')
    if name in names:
        print(f'{name}{names[name]}')
        names[name] += 1
    else:
        names[name] = 1
        print('OK')