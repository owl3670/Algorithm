cnt = int(input())

for i in range(cnt):
    num_cnt = int(input())
    num_str = input().split()
    if num_cnt % 2 != 0:
        print('NO')
        continue
    nums = list(map(int, num_str))
    nums.sort()
    right = len(nums) // 2
    new_nums = [nums[0], nums[right]]
    left = 1 
    right += 1 
    while(right < len(nums)):
        if new_nums[-1] <= nums[left] or nums[left] >= nums[right]:
            print('NO')
            break
        new_nums.append(nums[left])
        new_nums.append(nums[right])
        left += 1
        right += 1
    if len(new_nums) == len(nums):
        print('YES')
        print(' '.join(list(map(str, new_nums))))
