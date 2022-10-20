from sys import stdin

def main():
    n, a, b, c = map(int, stdin.readline().split())
    li = [a, b, c]
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if dp[i] != 0:
            for j in li:
                if i + j <= n:
                    dp[i + j] = max(dp[i + j], dp[i] + 1)
        else:
            for j in li:
                if i % j == 0:
                    dp[i] = max(dp[i], i // j)
            if dp[i] != 0:
                for j in li:
                    if i + j <= n:
                        dp[i + j] = max(dp[i + j], dp[i] + 1)
    print(dp[n])
    

if __name__ == '__main__':
    main()