from sys import stdin

def main():
    n, a, b, c = map(int, stdin.readline().split())
    li = [a, b, c]
    dp = [0] * (n + 1)
    print(dp[n])
    

if __name__ == '__main__':
    main()