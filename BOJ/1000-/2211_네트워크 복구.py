# https://www.acmicpc.net/problem/2211

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float("inf")


def dijkstra(start: int, graph: list) -> dict:
    pq = []
    heappush(pq, (0, start))
    dist = [INF] * len(graph)
    dist[start] = 0
    ans = dict()

    while pq:
        now_cost, now_node = heappop(pq)

        if now_cost > dist[now_node]:
            continue

        for adj_node, adj_cost in graph[now_node]:
            cost = now_cost + adj_cost

            if cost < dist[adj_node]:
                dist[adj_node] = cost
                heappush(pq, (cost, adj_node))

                ans[adj_node] = (now_node, adj_node)

    return ans


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

ans = dijkstra(1, graph)
print(len(ans))
for edge in ans.values():
    print(*edge)


"""
2211. 네트워크 복구
    - MST로 해결할 수 있을줄 알고 처음에 MST로 접근했는데 WA
      반례
      3 3
      1 2 2
      1 3 2
      2 3 1

    - 다익스트라 진행중에 사용되는 간선을 추가/갱신하는 방식으로 해결함.
"""