# https://www.acmicpc.net/problem/1584

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float("inf")


def dijkstra(start: int, dest: int, graph: list) -> list:
    pq = []
    heappush(pq, (0, start))
    dist = [INF] * len(graph)
    dist[start] = 0

    while pq:
        now_cost, now_node = heappop(pq)

        if now_cost > dist[now_node]:
            continue

        for adj_node, adj_cost in graph[now_node]:
            cost = now_cost + adj_cost

            if cost < dist[adj_node]:
                dist[adj_node] = cost
                heappush(pq, (cost, adj_node))

    return dist[dest]


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
s, t = map(int, input().split())

print(dijkstra(s, t, graph))