input()
stones = input()
before = ""
cnt = 0
for stone in stones:
    if before != stone:
        before = stone
    else:
        cnt += 1
        
print(cnt)