# 2024.09.12 THU
# https://www.acmicpc.net/problem/24419

import sys

input = sys.stdin.readline
DIV = 1_000_000_007

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

d = [[1] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0:
            continue
        d[i][j] = d[i - 1][j] + d[i][j - 1]

print(sum(d[n - 1]) * 2 % DIV, n**2)
