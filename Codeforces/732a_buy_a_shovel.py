from sys import stdin

def main():
    k, r = map(int, stdin.readline().split())
    for i in range(1, 10):
        if (k * i) % 10 == 0 or (k * i - r) % 10 == 0:
            print(i)
            break

if __name__ == '__main__':
    main()