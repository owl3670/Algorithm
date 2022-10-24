from sys import stdin

input = stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        if a == b:
            print(0)
        else:
            if a > b:
                a, b = b, a
            print((b - a + 9) // 10)

if __name__ == '__main__':
    main()