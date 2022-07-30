from sys import stdin, stdout

input = stdin.readline
def prin(val):
    stdout.write(f'{val}\n')

n = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
a = 0
b = sum(nums)
for i in range(len(nums)):
    a += nums[i]
    b -= nums[i]
    if a > b:
        print(i + 1)
        break