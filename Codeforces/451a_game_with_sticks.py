from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n, m = map(int, input().split())
if min(n, m) % 2 == 0:
    print('Malvika')
else:
    print('Akshat')

