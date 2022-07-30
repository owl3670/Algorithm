from math import ceil
from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

input()
nums = list(map(int, input().split()))
cnts = [0, 0, 0, 0, 0]
for num in nums:
    cnts[num] += 1

taxi = 0
taxi += cnts[4]
taxi += cnts[3]
taxi += ceil(cnts[2] / 2)
cnts[1] = max(cnts[1] - cnts[3] - ((cnts[2] % 2) * 2), 0)
taxi += ceil(cnts[1] / 4)

print(taxi)