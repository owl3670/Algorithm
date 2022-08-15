from sys import stdin, stdout

input = stdin.readline


def print(val):
    stdout.write(f'{str(val)}\n')


a = input().replace('\n', '')
b = input().replace('\n', '')

result = ''
for idx in range(len(a)):
    if a[idx] == b[idx]:
        result = f'{result}0'
    else:
        result = f'{result}1'

print(result)
