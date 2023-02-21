# https://www.acmicpc.net/problem/1956

import sys

input = sys.stdin.readline
INF = float("inf")

V, E = map(int, input().split())
graph = [[INF] * (V + 1) for _ in range(V + 1)]
for i in range(1, V + 1):
    graph[i][i] = 0
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

#
for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

ans = INF
for i in range(1, V + 1):
    for j in range(1, V + 1):
        if i == j:
            continue
        if ans > graph[i][j] + graph[j][i]:
            ans = graph[i][j] + graph[j][i]

if ans == INF:
    ans = -1
print(ans)
