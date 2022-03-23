str = input()
uniques = {}
for c in str:
    if c not in uniques:
        uniques[c] = ''

uniques_len = len(uniques)

if uniques_len % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")