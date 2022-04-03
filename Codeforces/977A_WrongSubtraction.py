n, k = map(int, input().split())

for i in range(k):
    mod = n % 10
    if mod == 0:
        n /= 10
    if mod != 0:
        n -= 1

print(int(n))