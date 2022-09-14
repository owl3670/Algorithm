from sys import stdin, stdout

def main():
    s, n = map(int, stdin.readline().split())
    dragons = []
    for i in range(n):
        x, y = map(int, stdin.readline().split())
        dragons.append((x, y))
    dragons.sort()
    for i in range(n):
        if s > dragons[i][0]:
            s += dragons[i][1]
        else:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    main()