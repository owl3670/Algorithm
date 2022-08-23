from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

s = input().replace('\n', '')

wrong = True
for i in range(1, len(s)):
    if s[i].islower():
        wrong = False
        break

if wrong:
    new_s = ''
    for c in s:
        if c.isupper():
            new_s += c.lower()
        else:
            new_s += c.upper()
    print(new_s)
else:
    print(s)