from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = int(input())
for _ in range(n):
    num = int(input())
    print('2\n')
    uses = [False] * (num + 1)
    for i in range(1, num + 1, 2):
        j = i
        while j <= num:
            print(f'{j} ')
            uses[j] = True
            j *= 2
    for i in range(1, num+1):
        if not uses[i]:
            print(f'{i} ')
    print('\n')