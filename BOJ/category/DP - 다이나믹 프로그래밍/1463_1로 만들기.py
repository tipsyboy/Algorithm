# https://www.acmicpc.net/problem/1463

import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)  # dp[i] : i 가 1이 되는데
dp[1] = 0
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[N])