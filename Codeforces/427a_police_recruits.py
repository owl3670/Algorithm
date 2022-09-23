from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = int(input())
events = list(map(int, input().split()))
police = 0
crimes = 0
for event in events:
    if event > 0:
        police += event
    else:
        if police > 0:
            police -= 1
        else:
            crimes += 1

print(str(crimes))