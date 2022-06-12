inputs = list(map(int, input().split()))
items = list(map(int, input().split()))
items.sort(reverse=True)

sums = [0]
for i in range(len(items)):
    sums.append(sums[i] + items[i])

for i in range(inputs[1]):
    query = list(map(int, input().split()))
    purchase = sums[query[0]]
    print(purchase - sums[query[0] - query[1]])