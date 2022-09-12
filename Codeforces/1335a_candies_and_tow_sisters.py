from sys import stdin, stdout

input = stdin.readline
def print(val):
    stdout.write(f'{val}\n')

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(n // 2 if n % 2 else n // 2 - 1)

if __name__ == '__main__':
    main()