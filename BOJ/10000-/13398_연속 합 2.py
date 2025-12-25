# 2025.01.22 WED
# https://www.acmicpc.net/problem/13398

import sys

input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

dp = [[0] * N for _ in range(2)]
dp[0][0] = dp[1][0] = seq[0]

ans = seq[0]
for i in range(1, N):
    dp[0][i] = max(dp[0][i - 1] + seq[i], seq[i])
    dp[1][i] = max(dp[1][i - 1] + seq[i], seq[i], dp[0][i - 1])

    ans = max(ans, dp[0][i], dp[1][i])

print(*dp, sep="\n")
print(ans)
