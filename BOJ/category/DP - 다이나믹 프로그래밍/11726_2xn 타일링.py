# https://www.acmicpc.net/problem/11726

import sys

input = sys.stdin.readline
DIV = 10_007


def sol1(n: int) -> int:
    if n < 2:
        return 1

    dp = [0] * n
    dp[0], dp[1] = 1, 2

    for i in range(2, n):
        dp[i] = (dp[i - 1] + dp[i - 2]) % DIV

    return dp[n - 1] % DIV


n = int(input())
print(sol1(n))