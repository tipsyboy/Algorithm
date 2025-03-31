# 2025.03.14 FRI
# https://www.acmicpc.net/problem/14650

import sys

input = sys.stdin.readline


def pick_number(depth, picked):
    global ans
    if N == depth:
        if sum(picked) % 3 == 0:
            ans += 1
        return

    for i in [0, 1, 2]:
        if depth == 0 and i == 0:
            continue

        picked.append(i)
        pick_number(depth + 1, picked)
        picked.pop()


N = int(input())
ans = 0
pick_number(0, [])
print(ans)
