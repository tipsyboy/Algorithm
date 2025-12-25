# https://www.acmicpc.net/problem/2617

import sys

input = sys.stdin.readline
INF = float("inf")

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1

for i in range(1, N + 1):
    graph[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

mid = (N - 1) // 2
ans = 0
for i in range(1, N + 1):
    low, high = 0, 0

    for j in range(1, N + 1):
        if graph[i][j] == 0 or graph[i][j] == INF:
            continue
        low += 1

    for j in range(1, N + 1):
        if graph[j][i] == 0 or graph[j][i] == INF:
            continue
        high += 1

    if low > mid or high > mid:
        ans += 1

print(ans)