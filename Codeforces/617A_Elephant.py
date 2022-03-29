x = int(input())

result = x // 5
result += 0 if x % 5 == 0 else 1
print(result)