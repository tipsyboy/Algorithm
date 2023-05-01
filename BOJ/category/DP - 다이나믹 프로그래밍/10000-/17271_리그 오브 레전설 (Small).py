# https://www.acmicpc.net/problem/17271

import sys

input = sys.stdin.readline
DIV = 1_000_000_007

N, M = map(int, input().split())
dp = [1] * M

for i in range(M, N + 1):
    dp.append((dp[i - 1] + dp[i - M]) % DIV)

print(dp[N])