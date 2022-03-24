def check_danger(str):
    before = ''
    cnt = 1
    for c in str:
        if before != c:
            cnt = 1
            before = c
        else:
            cnt+=1
        if cnt == 7:
            print("YES")
            return
    print("NO")
    
str = input()
check_danger(str)