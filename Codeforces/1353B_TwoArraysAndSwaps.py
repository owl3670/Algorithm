from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')
    
t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    k = nums[1]
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr1.sort()
    arr2.sort(reverse=True)
    for i in range(k):
        if arr1[i] < arr2[i]:
            arr1[i] = arr2[i]
    print(sum(arr1))