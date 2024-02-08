# https://www.acmicpc.net/problem/15975

import sys

input = sys.stdin.readline

N = int(input())
colors = [[] for _ in range(N + 1)]
for _ in range(N):
    d, p = map(int, input().split())

    colors[p].append(d)

ans = 0
for p in range(1, N + 1):
    colors[p].sort()

    if len(colors[p]) < 2:
        continue

    for i in range(len(colors[p])):
        if i == 0:
            ans += colors[p][i + 1] - colors[p][i]
        elif i == len(colors[p]) - 1:
            ans += colors[p][i] - colors[p][i - 1]
        else:
            ans += min(colors[p][i] - colors[p][i - 1], colors[p][i + 1] - colors[p][i])

print(ans)
