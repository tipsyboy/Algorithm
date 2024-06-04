# https://www.acmicpc.net/problem/1996

import sys

input = sys.stdin.readline
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

N = int(input())
grid = [list(input().rstrip()) for _ in range(N)]

ans = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if grid[i][j] == ".":
            continue

        for d in range(8):
            ni, nj = i + directions[d][0], j + directions[d][1]

            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue

            ans[ni][nj] += int(grid[i][j])

for i in range(N):
    temp = list(map(str, ans[i]))
    for j in range(N):
        if int(temp[j]) > 9:
            temp[j] = "M"
        if grid[i][j] != ".":
            temp[j] = "*"

    print("".join(temp))
