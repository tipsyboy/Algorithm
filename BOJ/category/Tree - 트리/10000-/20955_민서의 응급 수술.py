# https://www.acmicpc.net/problem/20955

import sys
from collections import deque

input = sys.stdin.readline


def bfs(start: int) -> None:
    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()

        for adj in graph[cur]:
            if visited[adj]:
                continue
            q.append(adj)
            visited[adj] = True


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


visited = [False] * (N + 1)
each = 0
for i in range(1, N + 1):
    if visited[i]:
        continue
    bfs(i)
    each += 1

print((each - 1) + (each - 1 + M) - (N - 1))

"""
- 연결그래프로 만드는 비용
- (현재 간선) - (필요간선) = 불필요 간선
"""