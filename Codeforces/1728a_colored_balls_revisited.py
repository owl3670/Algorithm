from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

t = int(input())

for _ in range(t):
    n = int(input())
    cnts = list(map(int, input().split()))
    max_idx = 0
    max_cnt = cnts[0]
    for idx, cnt in enumerate(cnts):
        if max_cnt < cnt:
            max_idx = idx
            max_cnt = cnt
    print(max_idx + 1)