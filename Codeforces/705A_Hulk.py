from sys import stdin, stdout

input = stdin.readline

def print(val):
    stdout.write(f'{val}\n')
    
n = int(input())

s = 'I hate'
hate = False
for _ in range(n - 1):
    s = f'{s} that'
    if hate:
        s = f'{s} I hate'
    else:
        s = f'{s} I love'
    hate = not hate

print(f'{s} it')
