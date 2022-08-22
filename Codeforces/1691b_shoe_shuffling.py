cnt = int(input())

for i in range(cnt):
    input()
    nums = list(map(int, input().split()))
    dic = {}
    for idx, num in enumerate(nums):
        if num in dic:
            dic[num].append(idx)
        else:
            dic[num] = [idx]

    shuffle = ['0'] * len(nums)   
    valid = True 
    for idxs in dic.values():
        if len(idxs) == 1:
            print(-1)
            valid = False
            break
        for i in range(len(idxs)):
            shuffle[idxs[i]] = str(idxs[i - 1] + 1)

    if valid:
        print(' '.join(shuffle))