# 2024.11.02 SAT
# https://www.acmicpc.net/problem/29704

import sys

input = sys.stdin.readline

N, T = map(int, input().split())

dp = [[0] * (T + 1) for _ in range(N + 1)]
total = 0
for i in range(1, N + 1):
    d, m = map(int, input().split())
    total += m

    for j in range(T + 1):
        if j < d:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - d] + m)

print(total - dp[N][T])
