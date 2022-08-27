from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n = int(input())
s = input()
s.replace('\n', '')
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for c in s:
    a = c.lower()
    if a in alphabets:
        alphabets.remove(c.lower())

if len(alphabets) == 0:
    print('YES')
else:
    print('NO')