from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n = int(input())
for _ in range(n):
    s1 = input()
    s1 = s1.replace('\n', '')
    s2 = input()
    s2 = s2.replace('\n', '')

    di = {}
    for c in s1:
        if c in di:
            di[c] += 1
        else:
            di[c] = 1
    for c in s2:
        if c in di:
            di[c] += 1
        else:
            di[c] = 1
    print(len(di) - 1)