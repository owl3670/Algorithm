from sys import stdout, stdin

print = stdout.write
input = stdin.readline

inputs = list(map(int, input().split()))

peoples = list(map(int, input().split()))

result = 0
h = inputs[1]
for people in peoples:
    if people <= h:
        result += 1
    else:
        result += 2

print(f'{result}\n')