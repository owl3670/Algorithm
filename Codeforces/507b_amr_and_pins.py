from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

r, x1, y1, x2, y2 = map(int, input().split())

distance = distance(x1, y1, x2, y2)
if distance == 0:
    print(0)
else:
    print(int(distance / (2 * r)) + 1 if distance % (2 * r) else int(distance / (2 * r)))