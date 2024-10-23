# 2024.10.17 THU
# https://www.acmicpc.net/problem/12786

import sys

input = sys.stdin.readline
MAX_HEIGHT = 20
INF = float("inf")


def go(cur, height):
    if cur == N:
        return 0

    if dp[cur][height] != INF:
        return dp[cur][height]

    rst = INF

    # OABC
    for nxt in [height, height + 1, min(MAX_HEIGHT, height * 2), height - 1]:
        if nxt < 1 or nxt > MAX_HEIGHT:
            continue

        if not tree[cur + 1][nxt]:
            continue

        rst = min(rst, go(cur + 1, nxt))

    # T
    for nxt in range(1, MAX_HEIGHT + 1):
        if tree[cur + 1][nxt]:
            rst = min(rst, go(cur + 1, nxt) + 1)

    dp[cur][height] = rst
    return dp[cur][height]


N = int(input())
K = int(input())

tree = [[False] * (MAX_HEIGHT + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    M, *holes = map(int, input().split())
    for hole in holes:
        tree[i][hole] = True
tree[0][1] = True

dp = [[INF] * 21 for _ in range(N + 1)]

ans = go(0, 1)
print(-1) if ans == INF or ans > K else print(ans)
