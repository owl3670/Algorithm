nums = [8, 10, 1, 9, 5, 7, 3, 6, 2, 4]

print("before sort", nums)

for i in range(len(nums)):
    min_idx = i
    for j in range(i, len(nums)):
       if nums[j] < nums[min_idx]:
           min_idx = j
    nums[i], nums[min_idx] = nums[min_idx], nums[i]

print("after sort", nums)