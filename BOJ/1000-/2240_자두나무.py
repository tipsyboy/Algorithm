# 2024.08.22 THU
# https://www.acmicpc.net/problem/2240

import sys

input = sys.stdin.readline


def eat(time, pos, chance):
    if chance < 0:
        return -1

    if time == T:
        return 0

    if dp[time][pos][chance]:
        return dp[time][pos][chance]

    eat_now = 1 if plum[time] == pos else 0
    dp[time][pos][chance] = max(eat(time + 1, pos, chance), eat(time + 1, pos ^ 1, chance - 1)) + eat_now

    return dp[time][pos][chance]


T, W = map(int, input().split())
plum = []
for _ in range(T):
    # pos => 1: 0, 2: 1
    plum.append(int(input()) - 1)


dp = [[[0] * (W + 1) for _ in range(2)] for __ in range(T + 1)]
print(max(eat(0, 0, W), eat(0, 1, W - 1)))
