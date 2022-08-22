from sys import stdin, stdout

input = stdin.readline
print = stdout.write

cnt = int(input())

for i in range(cnt):
    n = int(input())
    nums = list(map(int, input().split()))
    num_dict = {}
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    result = len(num_dict)
    if (n - result) % 2:
        result -= 1
    
    print(f'{result}\n')