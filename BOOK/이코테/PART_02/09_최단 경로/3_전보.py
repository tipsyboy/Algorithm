import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)


def dijkstara(start):
    dist = [INF] * (n + 1)
    pq = []
    dist[start] = 0
    heappush(pq, (0, start))

    while pq:
        now_cost, now_node = heappop(pq)

        if now_cost > dist[now_node]:
            continue

        for adj in graph[now_node]:
            adj_node, adj_cost = adj
            cost = adj_cost + now_cost

            if cost < dist[adj_node]:
                dist[adj_node] = cost
                heappush(pq, (cost, adj_node))

    return dist


n, m, c = map(int, input().split())  # 노드, 간선, 시작점
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, z = map(int, input().split())

    # directed graph
    graph[x].append((y, z))

dist = dijkstara(c)
count = 0
max_dist = 0
for d in dist:
    if d < INF and d != 0:
        count += 1
        max_dist = max(max_dist, d)

print(count, max_dist)
