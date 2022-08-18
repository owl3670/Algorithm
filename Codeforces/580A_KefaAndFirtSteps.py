from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n = int(input())
a = list(map(int, input().split()))

result = 0
non_decreasing = 0
before = 0
for val in a:
    if val >= before:
        non_decreasing += 1
    else:
        non_decreasing = 1
    before = val
    result = max(result, non_decreasing)

print(result)