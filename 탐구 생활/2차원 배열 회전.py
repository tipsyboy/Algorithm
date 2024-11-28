def rotate_matrix_90(mat: list) -> list:
    row = len(mat)
    col = len(mat[0])
    new_mat = [[0] * row for _ in range(col)]

    for i in range(row):
        for j in range(col):
            new_mat[j][row - i - 1] = mat[i][j]

    return new_mat


N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
for _ in range(4):
    print(*mat, sep="\n")
    print()
    mat = rotate_matrix_90(mat)

"""
9 9
7 3 6 4 2 9 5 8 1
5 8 9 1 6 7 3 2 4
2 1 4 5 8 3 6 9 7
8 4 7 9 3 6 1 5 2
1 5 3 8 4 2 9 7 6
9 6 2 7 5 1 8 4 3
4 2 1 3 9 8 7 6 5
3 9 5 6 7 4 2 1 8
6 7 8 2 1 5 4 3 9

2 5
1 1 1 1 1
0 0 0 1 0
"""
