# https://www.acmicpc.net/problem/18808

import sys

input = sys.stdin.readline


def rotate_90_matrix(mat: list) -> list:
    row = len(mat)
    col = len(mat[0])
    new_mat = [[0] * row for _ in range(col)]

    for i in range(row):
        for j in range(col):
            new_mat[j][row - i - 1] = mat[i][j]

    return new_mat


def is_possible(sticker: list, sx: int, sy: int) -> bool:
    for i in range(sx, sx + len(sticker)):
        for j in range(sy, sy + len(sticker[0])):
            if sticker[i - sx][j - sy] == 0:
                continue

            if sticker[i - sx][j - sy] & grid[i][j]:
                return False

    return True


def sticker_on(sticker: list, sx: int, sy: int) -> None:
    for i in range(sx, sx + len(sticker)):
        for j in range(sy, sy + len(sticker[0])):
            if sticker[i - sx][j - sy] == 0:
                continue
            grid[i][j] = sticker[i - sx][j - sy]


def put_sticker(sticker: list) -> None:
    for _ in range(4):
        for i in range(N - len(sticker) + 1):
            for j in range(M - len(sticker[0]) + 1):
                if not is_possible(sticker, i, j):
                    continue
                sticker_on(sticker, i, j)
                return

        sticker = rotate_90_matrix(sticker)


N, M, K = map(int, input().split())
grid = [[0] * M for _ in range(N)]

stickers = []
for _ in range(K):
    R, C = map(int, input().split())
    s = [list(map(int, input().split())) for _ in range(R)]
    stickers.append(s)

for i in range(K):
    put_sticker(stickers[i])

ans = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            ans += 1
print(ans)