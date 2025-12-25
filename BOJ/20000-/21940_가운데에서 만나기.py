# https://www.acmicpc.net/problem/21940

import sys

input = sys.stdin.readline
INF = float("inf")

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0
for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u][v] = t

#
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]


K = int(input())
friends = list(map(int, input().split()))

minv = INF
time = [0] * (N + 1)
for x in range(1, N + 1):
    maxv = -1
    for friend in friends:
        if maxv < graph[friend][x] + graph[x][friend]:
            maxv = graph[friend][x] + graph[x][friend]

    time[x] = maxv

minv = INF
ans = []
for i in range(1, N + 1):
    if minv > time[i]:
        minv = time[i]
        ans = [i]
    elif minv == time[i]:
        ans.append(i)

print(*ans)


"""
21940. 가운데에서 만나기
    - 플로이드-워셜 이후 문제 조건에 맞게 처리
"""