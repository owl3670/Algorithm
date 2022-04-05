def main():
    s = input()

    hello = list("hello")
    idx = 0
    for c in s:
        if c == hello[idx]:
            idx += 1
        if idx == 5:
            print("YES")
            return
    
    print("NO")
    
main()