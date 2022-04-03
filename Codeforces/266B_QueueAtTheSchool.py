n, t = map(int, input().split())
s = list(input())
for i in range(t):
    idxs = []
    for j in range(1, len(s)):
        if s[j-1] == 'B' and s[j] == 'G':
            idxs.append(j)
    for idx in idxs:
        s[idx-1], s[idx] = s[idx], s[idx-1]

print(''.join(s))