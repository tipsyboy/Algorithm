# https://www.acmicpc.net/problem/2669

import sys

input = sys.stdin.readline
MAXV = 101

grid = [[0] * MAXV for _ in range(MAXV)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1 - 1, x2 - 1):
        for j in range(y1 - 1, y2 - 1):
            grid[i][j] = 1

print(sum(map(sum, grid)))