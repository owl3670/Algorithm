from sys import stdin

input = stdin.readline

n, k, l, c, d, p, nl, np = map(int, input().split())
liter = k*l
cup = liter // nl
lime = c*d
salt = p // np

print(min(cup, lime, salt) // n)