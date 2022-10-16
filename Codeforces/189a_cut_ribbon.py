from sys import stdin

def main():
    n, a, b, c = map(int, stdin.readline().split())
    if a + b + c <= n:
        print(3)
        return
    if a + b <= n:
        print(2)
        return
    if a + c <= n:
        print(2)
        return
    if b + c <= n:
        print(2)
        return
    print(1)


if __name__ == '__main__':
    main()