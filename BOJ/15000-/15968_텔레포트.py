# 2024.12.29 SUN
# https://www.acmicpc.net/problem/16958

"""
15968. 텔레포트

뚫긴 뚫었는데, 이게 맞나..?
N<=1000인데
"""

import sys

input = sys.stdin.readline


N, T = map(int, input().split())
cities = []
for _ in range(N):
    s, x, y = map(int, input().split())
    cities.append((s, x, y))

dist = [[0] * N for _ in range(N)]
for i in range(N - 1):
    si, xi, yi = cities[i]
    for j in range(i + 1, N):
        sj, xj, yj = cities[j]

        d = abs(xi - xj) + abs(yi - yj)
        if si == sj == 1 and d > T:
            d = T

        dist[i][j] = d
        dist[j][i] = d

for k in range(N):
    for i in range(N - 1):
        for j in range(i + 1, N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                dist[j][i] = dist[i][k] + dist[k][j]

M = int(input())
for _ in range(M):
    A, B = map(int, input().split())
    print(dist[A - 1][B - 1])
