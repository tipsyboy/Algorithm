# 2024.07.18 THU
# https://www.acmicpc.net/problem/28075

import sys

input = sys.stdin.readline


def dfs(lv, prev, prg):
    global ans

    if lv == N:
        if prg >= M:
            ans += 1
        return

    for i in range(3):
        info_value = info[i] if i != prev else info[i] // 2
        obs_value = obs[i] if i != prev else obs[i] // 2

        dfs(lv + 1, i, prg + info_value)
        dfs(lv + 1, i, prg + obs_value)


N, M = map(int, input().split())
info = list(map(int, input().split()))
obs = list(map(int, input().split()))
ans = 0
dfs(0, -1, 0)
print(ans)
