# https://www.acmicpc.net/problem/10164

"""
10164. 격자상의 경로
    1. 조합론
    2. dp를 사용
    3. 2.에서 동시사건 사용하기
"""

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())


def sol(st: tuple, en: tuple, f: int) -> int:
    r1, c1 = st
    r2, c2 = en
    row, col = r2 - r1 + 1, c2 - c1 + 1
    mat = [[0] * (col) for _ in range(row)]

    for i in range(row):
        mat[i][0] = f

    for i in range(col):
        mat[0][i] = f

    for i in range(1, row):
        for j in range(1, col):
            mat[i][j] = mat[i - 1][j] + mat[i][j - 1]

    return mat[row - 1][col - 1]


if K == 0:
    print(sol((0, 0), (N - 1, M - 1), 1))
else:
    q, r = divmod(K, M)
    if r == 0:
        q -= 1
        r = M - 1
    else:
        r -= 1

    f1 = sol((0, 0), (q, r), 1)
    print(sol((q, r), (N - 1, M - 1), f1))
