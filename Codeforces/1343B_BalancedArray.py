from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

t = int(input())
for _ in range(t):
    n = int(input())
    if (n // 2) % 2 != 0:
        print('NO')
    else:
        print('YES')
        arr = [2 * i for i in range(1, (n//2)+1)]
        for idx in range(n // 4):
            arr.append(arr[idx] - 1)
        for idx in range(n//4, n//2):
            arr.append(arr[idx] + 1)
        print(' '.join(list(map(str, arr))))