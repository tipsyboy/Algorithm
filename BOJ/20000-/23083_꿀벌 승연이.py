# https://www.acmicpc.net/problem/23083

import sys

input = sys.stdin.readline
MOD = 10 ** 9 + 7
directions = {0: [(1, 0), (0, 1), (-1, 1)], 1: [(1, 0), (1, 1), (0, 1)]}


N, M = map(int, input().split())
grid = [[0] * M for _ in range(N)]
K = int(input())
for _ in range(K):
    x, y = map(lambda x: int(x) - 1, input().split())
    grid[x][y] = -1

grid[0][0] = 1
for col in range(M):
    for row in range(N):
        if grid[row][col] == -1:
            continue

        for d in range(3):
            if col % 2 == 0:
                nr, nc = row + directions[0][d][0], col + directions[0][d][1]
            else:
                nr, nc = row + directions[1][d][0], col + directions[1][d][1]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if grid[nr][nc] == -1:
                continue

            grid[nr][nc] += grid[row][col] % MOD

print(grid[N - 1][M - 1] % MOD)
