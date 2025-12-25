# 2024.10.26 SAT
# https://www.acmicpc.net/problem/1503

import sys

input = sys.stdin.readline
MAXV = 1000
INF = float("inf")

N, M = map(int, input().split())
S = set(list(map(int, input().split())))

ans = INF
for x in range(1, MAXV + 2):
    if x in S:
        continue
    for y in range(1, MAXV + 2):
        if y in S:
            continue
        for z in range(1, MAXV + 2):
            if z in S:
                continue

            xyz = abs(N - x * y * z)
            if xyz < ans:
                ans = xyz

            if xyz > N:
                break
        if x * y > N:
            break
    if x > N:
        break

print(ans)
