# https://www.acmicpc.net/problem/11051
# 2022-08-23 TUE

import sys

input = sys.stdin.readline
DIV = 10_007


def bino_coef(N: int, K: int) -> int:
    K = K if N - K > K else N - K

    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = 1
    for i in range(K + 1):
        dp[i][i] = 1

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % DIV

    return dp[N][K] % DIV


def bino_coef2(N: int, K: int) -> int:
    r = K if N - K > K else N - K

    nCk = 1
    for i in range(N, N - r, -1):
        nCk *= i
    for i in range(r, 0, -1):
        nCk //= i

    return nCk % DIV


N, K = map(int, input().split())
print(bino_coef(N, K))