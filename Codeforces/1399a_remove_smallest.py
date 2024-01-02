from sys import stdin, stdout

def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        a = list(map(int, stdin.readline().split()))
        a.sort()
        ans = True
        for i in range(1, n):
            if a[i] - a[i-1] > 1:
                ans = False
                break
        if ans:
            stdout.write('YES\n')
        else:
            stdout.write('NO\n')

if __name__ == '__main__':
    main()