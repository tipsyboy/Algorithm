# https://www.acmicpc.net/problem/12026

import sys

input = sys.stdin.readline
nxt = {"B": "O", "O": "J", "J": "B"}
INF = float("inf")

N = int(input())
blocks = list(input().rstrip())
energy = [INF] * N

energy[0] = 0
for s in range(N - 1):
    if energy[s] == INF:
        continue

    start, v = blocks[s], energy[s]
    for d in range(s + 1, N):
        if blocks[d] == nxt[start]:
            energy[d] = min(energy[d], v + (d - s) ** 2)

print(energy[N - 1] if energy[N - 1] != INF else -1)


"""
12026. BOJ 거리
    - N이 10^3으로 매우 널널하므로 O(N^2)으로 모두 살펴서 해결
"""