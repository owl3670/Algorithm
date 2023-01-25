from sys import stdin

def main():
    n, a, b, c = map(int, stdin.readline().split())
    max_pieces = 0
    for i in range(0, (n // a) + 1):
        for j in range(0, (n // b) + 1):
            for k in range(0, (n // c) + 1):
                if i*a + j*b + k*c == n:
                    max_pieces = max(max_pieces, i + j + k)
    print(max_pieces)

if __name__ == '__main__':
    main()