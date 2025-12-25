# 2024.09.21 SAT
# https://www.acmicpc.net/problem/17220

import sys
from collections import deque

input = sys.stdin.readline


def bfs(s, arrested):
    q = deque([s])
    visited = set([s])

    cnt = 0
    while q:
        cur = q.popleft()

        if cur not in graph:
            continue

        for adj in graph[cur]:
            if adj in arrested:
                continue
            if adj in visited:
                continue

            q.append(adj)
            visited.add(adj)
            cnt += 1

    return cnt


N, M = map(int, input().split())
indegree = [0] * N
graph = dict()
for _ in range(M):
    u, v = input().split()
    indegree[ord(v) - 65] += 1

    if u not in graph:
        graph[u] = []

    graph[u].append(v)

X, *arrested = input().split()

ans = 0
for i in range(N):
    if indegree[i]:
        continue

    root = chr(i + 65)
    if root in arrested:
        continue
    ans += bfs(root, arrested)

print(ans)
