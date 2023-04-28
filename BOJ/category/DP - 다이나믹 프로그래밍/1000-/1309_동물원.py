# https://www.acmicpc.net/problem/1309

import sys

input = sys.stdin.readline
DIV = 9901

N = int(input())
dp = [[1, 1, 1], [0, 0, 0]]
for i in range(1, N):
    dp[1][0], dp[1][1], dp[1][2] = dp[0][0], dp[0][0], dp[0][0]

    dp[1][0] += (dp[0][1] + dp[0][2]) % DIV
    dp[1][1] += dp[0][2] % DIV
    dp[1][2] += dp[0][1] % DIV

    dp[0] = dp[1]
    dp[1] = [0, 0, 0]

print(sum(dp[0]) % DIV)