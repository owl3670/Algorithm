nums = [8, 10, 1, 9, 5, 7, 3, 6, 2, 4]

print("before sort", nums)

def quick_sort(start, end, nums):
    if start < end:
        pivot = nums[start]
        pivot_idx = start
        left = start + 1
        right = end
        while left <= right:
            while nums[left] < pivot:
                left += 1
            while nums[right] > pivot:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
            else:
                nums[end], nums[pivot_idx] = nums[pivot_idx], nums[end]
    
    quick_sort(start, right - 1, nums)
    quick_sort(right + 1, end, nums)

quick_sort(0, len(nums), nums) 
        

print("after sort", nums)

