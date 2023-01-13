# https://www.acmicpc.net/problem/12852

import sys

input = sys.stdin.readline

N = int(input())
dp = [[0] * 2 for _ in range(N + 1)]
dp[1][0], dp[1][1] = 0, 0

for i in range(2, N + 1):
    dp[i][0], dp[i][1] = dp[i - 1][0] + 1, i - 1

    if i % 3 == 0 and dp[i // 3][0] + 1 < dp[i][0]:
        dp[i][0], dp[i][1] = dp[i // 3][0] + 1, i // 3

    if i % 2 == 0 and dp[i // 2][0] + 1 < dp[i][0]:
        dp[i][0], dp[i][1] = dp[i // 2][0] + 1, i // 2

cnt = dp[N][0]
print(cnt)
for _ in range(cnt + 1):
    print(N, end=" ")
    N = dp[N][1]
