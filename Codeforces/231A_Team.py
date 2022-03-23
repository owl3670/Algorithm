len_problems = int(input())
cnt = 0
for i in range(len_problems):
    p, v, t = map(int, input().split())
    if p + v + t >= 2: 
        cnt += 1

print(cnt)