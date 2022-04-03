n = int(input())

result = 0
cur = 0
for i in range(n):
    a, b = map(int, input().split())
    cur -= a
    cur += b
    result = max(result, cur)

print(result)