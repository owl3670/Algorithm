nums = [8, 10, 1, 9, 5, 7, 3, 6, 2, 4]

print("before sort", nums)

counts = [0 for i in range(len(nums) + 1)]
for num in nums:
    counts[num] += 1

nums = []
for i, count in enumerate(counts):
    for j in range(count):
        nums.append(i)

print("after sort", nums)

