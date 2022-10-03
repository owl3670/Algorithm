from sys import stdin

def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = stdin.readline().strip()
        n = n[::-1]
        ans = []
        for i in range(len(n)):
            if n[i] != '0':
                ans.append(int(n[i] + '0' * i))
        print(len(ans))
        print(*ans)

if __name__ == '__main__':
    main()