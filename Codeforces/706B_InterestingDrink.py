from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

n = int(input())
x = list(map(int, input().split()))
x.sort()
q = int(input())
for _ in range(q):
    m = int(input())
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if x[mid] <= m:
            start = mid + 1
        else:
            end = mid - 1
    print(start)