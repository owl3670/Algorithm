from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

s1 = input().strip()
s2 = input().strip()
s3 = input().strip()
s = s1 + s2
s = sorted(s)
s3 = sorted(s3)
if s == s3:
    print('YES')
else:
    print('NO')