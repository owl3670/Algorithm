from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

inputs = list(map(int, input().split()))
lanterns = list(map(int, input().split()))
lanterns.sort()

dist = 2 * max(lanterns[0], inputs[1] - lanterns[-1])
for idx in range(1, len(lanterns)):
    dist = max(dist, lanterns[idx] - lanterns[idx - 1])
print(dist/2)