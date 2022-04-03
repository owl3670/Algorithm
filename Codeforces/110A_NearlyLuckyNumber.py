s = input()

lucky_cnt = s.count('4') + s.count('7')
if lucky_cnt == 4 or lucky_cnt == 7:
    print('YES')
else:
    print('NO')