# https://www.acmicpc.net/problem/11048

import sys

input = sys.stdin.readline
directions = [(1, 0), (0, 1), (1, 1)]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = grid[0][0]
for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue

        if i == 0:
            dp[i][j] = dp[i][j - 1] + grid[i][j]
        elif j == 0:
            dp[i][j] = dp[i - 1][j] + grid[i][j]
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + grid[i][j]
print(dp[N - 1][M - 1])
