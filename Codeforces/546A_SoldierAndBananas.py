k, n, w = map(int, input().split())

cost = w * (k + k * w) / 2
result = int(cost - n)
print(result if result > 0 else 0)