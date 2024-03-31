# https://www.acmicpc.net/problem/14494

import sys

input = sys.stdin.readline
DIV = 10**9 + 7

n, m = map(int, input().split())
dp = [[0] * m for _ in range(n)]

dp[0][0] = 1
for i in range(n):
    for j in range(m):
        if i != 0 and j != 0:
            dp[i][j] += dp[i - 1][j - 1] % DIV

        if i != 0:
            dp[i][j] += dp[i - 1][j] % DIV

        if j != 0:
            dp[i][j] += dp[i][j - 1] % DIV

print(dp[n - 1][m - 1] % DIV)
