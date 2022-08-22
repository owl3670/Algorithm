cnt = int(input())

for i in range(cnt):
    input()
    nums = list(map(int, input().split()))
    nums.sort()
    before = nums[0]
    even = 0
    odd = 0
    for num in nums:
        if num % 2 == 0:
           even += 1
        else:
            odd += 1    
    print(min(even, odd))