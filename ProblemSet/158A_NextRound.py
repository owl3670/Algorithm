k = int(input().split()[1])
scores = list(map(int, input().split()))
temp = scores[k-1]
print(len(list(filter(lambda x : x >= temp and x != 0, scores))))