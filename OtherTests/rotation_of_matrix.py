def rotate(dir, matrix):
    new_matrix = []
    n = len(matrix)
    if dir == 'L':
        for i in range(n):
            tmp = []
            for j in range(n - 1, -1, -1):
                tmp.append(matrix[j][i])
            new_matrix.append(tmp)
    else:
        for i in range(n - 1, -1, -1):
            tmp = []
            for j in range(n):
                tmp.append(matrix[j][i])
            new_matrix.append(tmp) 
    return new_matrix

def reverse(matrix):
    new_matrix = []
    for row in matrix:
        new_matrix.append(row[::-1])
    return new_matrix

def solution():
    c = int(input())
    r = int(input())
    matrix = [[0 for _ in range(c)] for _ in range(r)]
    li = [int(x) for x in input().split(',')]
    for i in range(r):
        for j in range(c):
            matrix[i][j] = li[i * c + j]

    commands = input()
    pos = list(map(int, input().split(',')))
    for command in commands:
        if command == 'T':
            matrix = reverse(matrix)
        else:
            matrix = rotate(command, matrix)
    x = pos[0] - 1
    y = pos[1] - 1
    print(matrix[y][x])

solution()