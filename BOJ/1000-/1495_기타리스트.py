# 2025.01.08 WED
# https://www.acmicpc.net/problem/1495

import sys

input = sys.stdin.readline


N, S, M = map(int, input().split())
V = list(map(int, input().split()))
# dp[i][j] = i번 곡을 j음량으로 연주할 수 있는가?
dp = [[0] * (M + 1) for _ in range(N + 1)]

dp[0][S] = 1
for i in range(N):
    for j in range(M + 1):
        if dp[i][j]:
            if j + V[i] <= M:
                dp[i + 1][j + V[i]] = 1

            if j - V[i] >= 0:
                dp[i + 1][j - V[i]] = 1

ans = -1
for vol in range(M + 1):
    if dp[N][vol]:
        ans = vol
print(ans)
