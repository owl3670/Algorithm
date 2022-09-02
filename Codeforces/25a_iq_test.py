from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n = int(input())
a = list(map(int, input().split()))

for idx, val in enumerate(a):
    input