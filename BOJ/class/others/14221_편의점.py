import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(cvs):
    pq = []
    for c in cvs:
        dist[c] = 0
        heappush(pq, (0, c))

    while pq:
        now_cost, now_node = heappop(pq)

        if now_cost > dist[now_node]:
            continue

        for adj in graph[now_node]:
            adj_node, adj_cost = adj
            cost = now_cost + adj_cost

            if cost < dist[adj_node]:
                dist[adj_node] = cost
                heappush(pq, (cost, adj_node))

    return dist


n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())

    # undigraph
    graph[a].append((b, c))
    graph[b].append((a, c))

p, q = map(int, input().split())  # 집 후보 수 / 편의점 개수
house_candidate = list(map(int, input().split()))  # 집 후보군
cvs = list(map(int, input().split()))  # 편의점
dist = [INF] * (n + 1)

dijkstra(cvs)

rst, min_value = INF, INF
house_candidate = sorted(house_candidate)

for house in house_candidate:
    if dist[house] < min_value:
        min_value = dist[house]
        rst = house

print(rst)
