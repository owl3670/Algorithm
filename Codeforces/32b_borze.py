from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

borze = input().replace('\n', '')

decodes = ''
idx = 0
while idx < len(borze):
    if borze[idx] == '.':
        decodes = f'{decodes}0'
    else: 
        idx += 1
        if borze[idx] == '.':
            decodes = f'{decodes}1'
        else:
            decodes = f'{decodes}2'
    idx += 1

print(decodes)
