# https://www.acmicpc.net/problem/14728

import sys

input = sys.stdin.readline

N, T = map(int, input().split())

dp = [[0] * (T + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    K, S = map(int, input().split())

    for j in range(T + 1):
        if j < K:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - K] + S)

print(dp[N][T])
