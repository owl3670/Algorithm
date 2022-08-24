from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

s = input()
s = s.replace('WUB', ' ')
print(s.strip())