# https://www.acmicpc.net/problem/2579

import sys

input = sys.stdin.readline


def sol1(N: int, scores: list) -> int:
    dp = [0] * 300
    dp[0], dp[1], dp[2] = scores[0], scores[0] + scores[1], scores[2] + max(scores[0], scores[1])

    for i in range(3, N):
        dp[i] = scores[i] + max(dp[i - 3] + scores[i - 1], dp[i - 2])

    return dp[N - 1]


def sol2(N: int, scores: list) -> int:
    dp = [[0 for _ in range(3)] for __ in range(300)]

    if N == 1:
        return scores[0]

    dp[0][1] = scores[0]
    dp[1][1], dp[1][2] = scores[1], scores[0] + scores[1]
    for i in range(2, N):
        dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + scores[i]
        dp[i][2] = dp[i - 1][1] + scores[i]

    return max(dp[N - 1])


N = int(input())
scores = [0] * 300
for i in range(N):
    scores[i] = int(input())

# print(sol1(N, scores))
print(sol2(N, scores))