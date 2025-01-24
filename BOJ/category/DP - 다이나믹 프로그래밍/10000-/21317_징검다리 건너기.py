# 2025.01.14 TUE
# https://www.acmicpc.net/problem/21317

import sys

input = sys.stdin.readline
MAXV = 5001

N = int(input())
jump = []
for _ in range(N - 1):
    s, l = map(int, input().split())
    jump.append((s, l))
K = int(input())

dp = [[MAXV] * 2 for _ in range(N)]
dp[0][0] = dp[0][1] = 0
for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + jump[i - 1][0]
    dp[i][1] = dp[i - 1][1] + jump[i - 1][0]

    if i > 1:
        dp[i][0] = min(dp[i][0], dp[i - 2][0] + jump[i - 2][1])
        dp[i][1] = min(dp[i][1], dp[i - 2][1] + jump[i - 2][1])

    if i > 2:
        dp[i][1] = min(dp[i][1], dp[i - 3][0] + K)

print(min(dp[N - 1]))
