from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{str(val)}\n')

p = input()
is_program = False
programs = ['H', 'Q', '9']
for val in p:
    if val in programs:
        print('YES')
        is_program = True
        break

if not is_program:
    print('NO')