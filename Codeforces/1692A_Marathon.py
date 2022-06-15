from sys import stdin, stdout

input = stdin.readline
print = stdout.write

cnt = int(input())

for i in range(cnt):
    runners = list(map(int, input().split()))
    timur = runners[0]
    runners = runners[1:]
    front = 0
    for runner in runners:
        if timur <= runner:
            front += 1

    print(f'{front}\n')