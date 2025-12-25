# 2024.12.08 SUN
# https://www.acmicpc.net/problem/4097

import sys

input = sys.stdin.readline
INF = float("inf")

while True:
    N = int(input())
    if N == 0:
        break

    d = [-INF] * (N + 1)
    for i in range(1, N + 1):
        P = int(input())
        d[i] = max(d[i - 1] + P, P)

    print(max(d))
