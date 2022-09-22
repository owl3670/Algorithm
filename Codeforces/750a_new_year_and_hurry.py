from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n, k = map(int, input().split())
time = 240 - k
problems = 0
for i in range(1, n + 1):
    time -= 5 * i
    if time < 0:
        break
    problems += 1

print(str(problems))