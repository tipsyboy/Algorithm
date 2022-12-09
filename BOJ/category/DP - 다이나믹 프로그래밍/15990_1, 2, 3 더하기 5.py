# https://www.acmicpc.net/problem/15990

import sys

input = sys.stdin.readline
DIV = 1_000_000_009
MAXV = 100_000


def init_dp() -> list:
    dp = [[0, 0, 0] for _ in range(MAXV)]
    dp[0], dp[1], dp[2] = [1, 0, 0], [0, 1, 0], [1, 1, 1]
    for i in range(3, MAXV):
        dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % DIV
        dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % DIV
        dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % DIV

    return dp


N = int(input())
dp = init_dp()
for _ in range(N):
    print(sum(dp[int(input()) - 1]) % DIV)
