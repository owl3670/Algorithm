from sys import stdin

def main():
    n = list(map(int, stdin.readline().split()))
    n.sort()
    print(n[3] - n[0], n[3] - n[1], n[3] - n[2])

if __name__ == '__main__':
    main()