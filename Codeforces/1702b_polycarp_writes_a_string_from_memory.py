from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n = int(input())
for _ in range(n):
    letters = input().replace('\n', '')
    idx = 0
    days = 0
    letters_len = len(letters)
    mem = []
    while idx < letters_len:
        if len(mem) != 3 and letters[idx] not in mem:
            mem.append(letters[idx])
        if letters[idx] in mem:
            idx+=1
        else:
            mem.clear()
            days += 1
    days += 1

    print(f'{days}\n')