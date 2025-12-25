# https://www.acmicpc.net/problem/14495

import sys

input = sys.stdin.readline

n = int(input())
dp = [1, 1, 1]
for i in range(3, n):
    dp.append(dp[i - 1] + dp[i - 3])

print(dp[n - 1])
