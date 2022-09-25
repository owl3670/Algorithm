from sys import stdin, stdout

def main():
    t = int(stdin.readline())
    for i in range(t):
        n, c = map(int, stdin.readline().split())
        a = list(map(int, stdin.readline().split()))
        dic = {}
        for num in a:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        cost = 0 
        for key in dic:
            if dic[key] > c:
                cost += c
            else:
                cost += dic[key]
        print(cost)

if __name__ == '__main__':
    main()