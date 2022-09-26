from sys import stdin

def main():
    t = int(stdin.readline())
    for _ in range(t):
        n = int(stdin.readline())
        x = list(map(int, stdin.readline().split()))
        times = list(map(int, stdin.readline().split()))
        dic = {}
        m = -1
        m_idx = 0
        for i in range(n):
            if x[i] in dic:
                dic[x[i]] = max(dic[x[i]], times[i])
            else:
                dic[x[i]] = times[i]
            if m < times[i]:
                m = times[i]
                m_idx = x[i]
        min_pos = 1000000000
        max_pos = -1
        for set in dic.items():
            min_pos = min(min_pos, min(m_idx, set[0] + (m - set[1])))
            max_pos = max(max_pos, max(m_idx, set[0] - (m - set[1])))
        print((min_pos + max_pos) / 2)

if __name__ == '__main__':
    main()