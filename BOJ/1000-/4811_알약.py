# 2025.01.16 THU
# https://www.acmicpc.net/problem/4811

import sys

input = sys.stdin.readline
MAXV = 30


def eat_pill(one, half):
    if dp[one][half] != -1:
        return dp[one][half]

    rst = 0
    if one:
        rst += eat_pill(one - 1, half + 1)

    if half:
        rst += eat_pill(one, half - 1)

    dp[one][half] = rst
    return rst


dp = [[-1] * (MAXV * 2 + 1) for _ in range(MAXV + 1)]
dp[1][0] = 1
dp[0][1] = 1
while True:
    N = int(input())
    if N == 0:
        break

    if dp[N][0] == -1:
        eat_pill(N, 0)

    print(dp[N][0])
