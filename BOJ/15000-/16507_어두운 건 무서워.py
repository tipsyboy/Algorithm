# 2024.07.26 FRI
# https://www.acmicpc.net/problem/16507

import sys

input = sys.stdin.readline

R, C, Q = map(int, input().split())
pixels = [list(map(int, input().split())) for _ in range(R)]

psum = [[0] * (C + 1) for _ in range(R + 1)]
for i in range(1, R + 1):
    for j in range(1, C + 1):
        psum[i][j] = (psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1]) + pixels[i - 1][j - 1]

ans = []
for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    sumv = psum[r2][c2] - psum[r2][c1 - 1] - psum[r1 - 1][c2] + psum[r1 - 1][c1 - 1]
    pixels_cnt = (r2 - r1 + 1) * (c2 - c1 + 1)
    ans.append(sumv // pixels_cnt)
print(*ans, sep="\n")
