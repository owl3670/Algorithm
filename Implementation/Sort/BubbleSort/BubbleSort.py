nums = [8, 10, 1, 9, 5, 7, 3, 6, 2, 4]

print("before sort", nums)

for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print("after sort", nums)

