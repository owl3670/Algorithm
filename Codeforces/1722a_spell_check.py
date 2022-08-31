from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

t = int(input())
for _ in range(t):
    spell = {'T': 0, 'i': 0, 'm': 0, 'u': 0, 'r': 0}
    n = int(input())
    s = input().replace('\n', '')
    if n != 5:
        print('NO')
        continue
    
    ok = True
    for c in s:
        if c not in spell:
            print('NO')
            ok = False
            break
        else:
            del spell[c]
    if ok:
        print('YES')