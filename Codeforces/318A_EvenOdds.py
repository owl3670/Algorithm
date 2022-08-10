import math
from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

nums = list(map(int, input().split()))
n = nums[0]
k = nums[1]
mid = math.ceil(n/2)
if k <= mid:
    print(2 * k - 1)
else:
    print(2 * (k - mid))