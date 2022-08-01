from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

int(input())

nums = list(map(int, input().split()))
hard = False
for num in nums:
    if num == 1:
        hard = True
        break

if hard:
    print('HARD')
else:
    print('EASY')