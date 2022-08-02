from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n = int(input())
nums = list(map(int, input().split()))

gifts = [''] * n
for idx, num in enumerate(nums):
    gifts[num-1] = f'{idx + 1}'

print(' '.join(gifts))