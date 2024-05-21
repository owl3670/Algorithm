# Codeforces 363b Fence
# https://codeforces.com/problemset/problem/363/B

from sys import stdin, stdout

def print(val):
    stdout.write(f'{val}\n')

input = stdin.readline

[n, k] = list(map(int, input().split()))
h = list(map(int, input().split()))

dp = [0] * n
dp[0] = h[0]
for i in range(1, n):
    dp[i] = dp[i - 1] + h[i]
    if i > k - 1:
        dp[i] = dp[i] - h[i - k]

idx = 0
temp = 101 * k
for i in range(k - 1, len(dp)):
    if temp > dp[i]:
        idx = i + 1
        temp = dp[i]

print(idx - (k - 1))