# 2024.06.17 MON
# https://www.acmicpc.net/problem/16967

import sys

input = sys.stdin.readline


def is_overlap(r, c):
    return X <= r <= H and Y <= c <= W


H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H + X)]
A = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if is_overlap(i, j):
            A[i][j] = B[i][j] - A[i - X][j - Y]
        else:
            A[i][j] = B[i][j]

for i in range(H):
    print(*A[i])
