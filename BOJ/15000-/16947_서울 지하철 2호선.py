# https://www.acmicpc.net/problem/16947

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def dfs(start: int, cur: int, cnt: int, route: set) -> None:
    global cycle_nodes

    visited[cur] = True
    for adj in graph[cur]:
        if not visited[adj]:
            route.add(cur)
            dfs(start, adj, cnt + 1, route)
            route.remove(cur)
        elif adj == start and cnt > 1:
            cycle_nodes |= route
            return


def bfs() -> list:
    q = deque()
    dist = [-1] * (N + 1)
    for cycle_node in cycle_nodes:
        q.append(cycle_node)
        dist[cycle_node] = 0

    while q:
        cur = q.popleft()

        for adj in graph[cur]:
            if dist[adj] != -1:
                continue

            dist[adj] = dist[cur] + 1
            q.append(adj)

    return dist[1:]


N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cycle_nodes = set()
for i in range(1, N + 1):
    if i in cycle_nodes:
        continue

    visited = [False] * (N + 1)
    dfs(i, i, 0, set())

print(*bfs())
