from sys import stdin, stdout

input = stdin.readline
print = stdout.write

year = int(input())

while True:
    year += 1
    temp = year
    nums = []
    while temp > 0:
        nums.append(temp % 10)
        temp //= 10
    distinct = set(nums)
    if len(distinct) == len(nums):
        print(f'{year}')
        break