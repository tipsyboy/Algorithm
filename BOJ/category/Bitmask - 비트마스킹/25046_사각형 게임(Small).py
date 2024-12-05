# 2024.11.18 MON
# https://www.acmicpc.net/problem/25046

import sys

input = sys.stdin.readline
INF = float("inf")

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

ans = -INF
for minwoo_pick in range(1 << N):
    minwoo = 0
    for col in range(N):
        total = 0
        score = 0
        for row in range(N):
            total += grid[row][col]
            if minwoo_pick & (1 << row):
                score += grid[row][col]

        minwoo += min(score, total - score)

    ans = max(ans, minwoo)

print(ans)
