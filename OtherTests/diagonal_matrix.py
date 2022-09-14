def solution():
    c = int(input())
    r = int(input())
    matrix = [[0 for _ in range(c)] for _ in range(r)]
    li = [int(x) for x in input().split(',')]
    for i in range(r):
        for j in range(c):
            matrix[i][j] = li[i * c + j]

    tmp = []
    is_upper_right = True
    i = 0
    j = 0
    k = 0
    while k < r * c:
        if is_upper_right:
            while i >= 0 and j < c:
                tmp.append(matrix[i][j])
                i -= 1
                j += 1
                k += 1
            if i < 0 and j <= c - 1:
                i = 0
            if j == c:
                i = i + 2
                j -= 1
        else:
            while i < r and j >= 0:
                tmp.append(matrix[i][j])
                i += 1
                j -= 1
                k += 1
            if j < 0 and i <= r - 1:
                j = 0
            if i == r:
                j = j + 2
                i -= 1
        is_upper_right = not is_upper_right

    print(','.join(map(str, tmp)))

def main():
    solution()