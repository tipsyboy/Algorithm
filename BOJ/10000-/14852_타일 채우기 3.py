# https://www.acmicpc.net/problem/14852

import sys

input = sys.stdin.readline
DIV = 1_000_000_007

N = int(input())
dp = [1, 2, 7] + [0] * (N - 2)
psum = 1
for i in range(3, N + 1):
    dp[i] = ((dp[i - 1] * 2) % DIV + (dp[i - 2] * 3) % DIV + (psum * 2) % DIV) % DIV
    psum = (psum + dp[i - 2]) % DIV

print(dp[N])