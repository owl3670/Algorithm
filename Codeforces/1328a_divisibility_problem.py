from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

t = int(input())
for _ in range(t):
    a, b = (int(x) for x in input().split())
    r = a % b
    if r != 0 :
        print(b - r)
    else:
        print(0)