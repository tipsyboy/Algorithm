# 2024.10.09 WED
# https://www.acmicpc.net/problem/5582

# LCS
import sys

input = sys.stdin.readline

S1 = input().rstrip()
S2 = input().rstrip()
dp = [[0] * (len(S1) + 1) for _ in range(len(S2) + 1)]

ans = 0
for i in range(1, len(S2) + 1):
    for j in range(1, len(S1) + 1):
        if S1[j - 1] == S2[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

            if dp[i][j] > ans:
                ans = dp[i][j]
print(ans)
