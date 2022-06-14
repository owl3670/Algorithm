from sys import stdin, stdout

input = stdin.readline
print = stdout.write

inputs = list(map(int, input().split()))
items = list(map(int, input().split()))
items = sorted(items, reverse=True)

sums = [0]
for i in range(len(items)):
    sums.append(sums[i] + items[i])

for i in range(inputs[1]):
    query = list(map(int, input().split()))
    purchase = sums[query[0]]
    print(str(purchase - sums[query[0] - query[1]]) + "\n")