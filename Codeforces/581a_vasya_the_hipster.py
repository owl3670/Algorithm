from sys import stdin, stdout

def main():
    a, b = map(int, stdin.readline().split())
    if a > b:
        a, b = b, a
    print(a, (b - a) // 2)

if __name__ == '__main__':
    main()