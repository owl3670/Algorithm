from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n = int(input())

dollars = [100, 20, 10, 5, 1]
cnt = 0
for dollar in dollars:
    cnt += n // dollar
    n %= dollar

print(cnt)