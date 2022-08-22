cnt = input()
wins = input()

a = 0
d = 0
for win in wins:
    if win == 'A':
        a += 1
    else:
        d += 1

if  a > d:
    print('Anton')
elif d > a:
    print('Danik')
else:
    print('Friendship')