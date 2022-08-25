from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

s = input()
s = s.replace('{', '')
s = s.replace('}', '')
s = s.replace('\n', '')
s = s.replace(' ', '')

a = s.split(',')
d = set()
for c in a:
    if c:
        d.add(c)

print(len(d))