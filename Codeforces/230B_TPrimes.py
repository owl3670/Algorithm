import math

n = int(input())
nums = list(map(int, input().split()))
m = 1000001
t = int(math.sqrt(m))
primes = [True] * m
for i in range(2, t + 1):
    if primes[i]:
        for j in range(i + i, m, i):
            primes[j] = False
primes[0] = False
primes[1] = False
for num in nums:
    s = math.sqrt(num)
    if s == int(s) and primes[int(s)]:
        print('YES')
    else:
        print('NO')