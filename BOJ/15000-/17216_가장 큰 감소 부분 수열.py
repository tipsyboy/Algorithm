# 2025.02.24 MON
# https://www.acmicpc.net/problem/17216

import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N
for i in range(N):
    dp[i] = arr[i]
    for j in range(i - 1, -1, -1):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])
print(max(dp))
