nums = [8, 10, 1, 9, 5, 7, 3, 6, 2, 4]

print("before sort", nums)

for i in range(1, len(nums)):
    for j in range(i, 0, -1):
        if nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
        else:
            break
        

print("after sort", nums)

