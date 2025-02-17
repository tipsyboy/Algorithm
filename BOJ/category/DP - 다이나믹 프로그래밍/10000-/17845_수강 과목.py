# 2025.02.08 SAT
# https://www.acmicpc.net/problem/17845

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0] * (N + 1) for _ in range(K)]
I, T = map(int, input().split())
for i in range(T, N + 1):
    dp[0][i] = I

for i in range(1, K):
    I, T = map(int, input().split())
    for j in range(N + 1):
        if j >= T:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - T] + I)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[K - 1][N])
