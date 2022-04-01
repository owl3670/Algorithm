s = input()

upper = 0
lower = 0
for c in s:
    if ord(c) < 97:
        upper += 1
    else:
        lower += 1
        
print(s.upper() if upper > lower else s.lower())