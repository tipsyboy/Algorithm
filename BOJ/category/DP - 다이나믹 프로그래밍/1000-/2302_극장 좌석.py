# https://www.acmicpc.net/problem/2302

import sys

input = sys.stdin.readline


def sol(N: int, M: int, vips: list) -> int:
    dp = [0] * (N + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    if M == 0:
        return dp[N]

    ans, p = 1, 0
    for i in range(M):
        ans *= dp[vips[i] - p - 1]
        p = vips[i]

    ans *= dp[N - p]
    return ans


N = int(input())
M = int(input())
vips = []
for _ in range(M):
    vips.append(int(input()))

print(sol(N, M, vips))