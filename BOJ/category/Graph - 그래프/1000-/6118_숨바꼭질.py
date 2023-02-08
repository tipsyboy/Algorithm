# https://www.acmicpc.net/problem/6118

import sys
from collections import deque

input = sys.stdin.readline


def bfs(start: int) -> list:
    q = deque([start])
    dist = [-1] * (N + 1)
    dist[start] = 0
    while q:
        for _ in range(len(q)):
            now = q.popleft()

            for adj in graph[now]:
                if dist[adj] != -1:
                    continue
                q.append(adj)
                dist[adj] = dist[now] + 1

    return dist


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


dist = bfs(1)
maxv = max(dist)
ans = []
for i in range(1, N + 1):
    if dist[i] == maxv:
        ans.append(i)
print(ans[0], maxv, len(ans))