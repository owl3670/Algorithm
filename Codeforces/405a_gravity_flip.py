from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n = int(input())
a = list(map(int, input().split()))
a.sort()
temp = map(str, a)
print(' '.join(temp))