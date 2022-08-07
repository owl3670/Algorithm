from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    even_err = 0
    odd_err = 0
    even = True
    for val in a: 
        if even and val % 2 != 0:
            even_err += 1
        elif not even and val % 2 == 0:
            odd_err += 1
        even = not even
    print(-1 if even_err != odd_err else even_err) 
    