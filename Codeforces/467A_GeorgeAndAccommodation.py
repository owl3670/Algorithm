from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n = int(input())
result = 0
for _ in range(n):
    nums = list(map(int, input().split()))
    p = nums[0]
    q = nums[1]
    if q - p >= 2:
        result += 1

print(result)