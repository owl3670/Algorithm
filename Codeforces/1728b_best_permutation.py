from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n = int(input())
for _ in range(n):
    p = int(input())
    li = [str(i + 1) for i in range(p)]
    remain = (p - 2) % 3
    if remain == 0:
        print(' '.join(li))
    elif remain == 1:
        li[-3], li[-4] = li[-4], li[-3]
        li[-5], li[-6] = li[-6], li[-5]
        print(' '.join(li))
    else:
        li[-3], li[-4] = li[-4], li[-3]
        print(' '.join(li))