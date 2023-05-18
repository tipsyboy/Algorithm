# https://www.acmicpc.net/problem/1719

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float("inf")


def dijkstra(graph: list, start: int) -> list:
    pq = []
    heappush(pq, (0, start))
    dist = [INF] * len(graph)
    dist[start] = 0

    rst = [0] * len(graph)

    while pq:
        now_cost, now_node = heappop(pq)

        if now_cost > dist[now_node]:
            continue

        for adj_node, adj_cost in graph[now_node]:
            cost = now_cost + adj_cost

            if cost < dist[adj_node]:
                dist[adj_node] = cost
                heappush(pq, (cost, adj_node))

                if now_node == start:
                    rst[adj_node] = adj_node
                else:
                    rst[adj_node] = rst[now_node]

    return list(map(str, rst[1:]))


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

ans = []
for i in range(1, n + 1):
    rst = dijkstra(graph, i)
    rst[i - 1] = "-"
    ans.append(rst)

for i in range(len(ans)):
    print(" ".join(ans[i]))
