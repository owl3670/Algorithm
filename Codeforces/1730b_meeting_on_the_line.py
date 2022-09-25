from sys import stdin

def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        x = list(map(int, stdin.readline().split()))
        times = list(map(int, stdin.readline().split()))
        dic = {}
        m = 0
        for i in range(n):
            if x[i] in dic:
                dic[x[i]] = max(dic[x[i]], times[i])
            else:
                dic[x[i]] = times[i]
            m = max(m, times[i])
        dic = sorted(dic.items(), key=lambda x: x[0])
        sets = dic
        l = len(dic)
        min_pos = 1000000000
        max_pos = -1
        for idx, set in enumerate(sets):
            if set[1] == m:
                min_pos = min(min_pos, set[0])
                max_pos = max(max_pos, set[0])
                continue
            else:
                for i in range(1, l):
                    if idx + i < l:
                        if sets[idx + i][1]==m:
                            temp = sets[idx + i]
                            calc = abs((temp[0]) - set[0]) + set[1]
                            if calc > m:
                                min_pos = min(min_pos, set[0] + (m - set[1]))
                    if idx - i > -1:
                        if sets[idx - i][1]==m:
                            temp = sets[idx - i]
                            calc = abs((temp[0]) - set[0]) + set[1]
                            if calc > m:
                                max_pos = max(max_pos, set[0] - (m - set[1]))
        print((min_pos + max_pos) / 2)

if __name__ == '__main__':
    main()