from sys import stdin

input = stdin.readline

n = int(input())
scores = list(map(int, input().split()))
best = scores[0]
worst = scores[0]
amazing = 0
for i in range(1, n):
    if scores[i] > best:
        amazing += 1
        best = scores[i]
    elif scores[i] < worst:
        amazing += 1
        worst = scores[i]

print(amazing)