import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(2e9)


def search(start) -> list:
    pq = [(0, start)]  # time, start
    dist = [INF] * (n + 1)
    dist[start] = 0

    while pq:
        now_cost, now_node = heappop(pq)

        if now_cost < dist[now_node]:
            continue

        for adj_node, adj_cost in graph[now_node]:
            cost = now_cost + adj_cost

            if cost >= dist[adj_node]:
                continue
            heappush(pq, (cost, adj_node))
            dist[adj_node] = cost

    cnt = 0
    max_time = 0
    for i in range(1, n + 1):
        if dist[i] >= INF:
            continue

        cnt += 1
        max_time = max(max_time, dist[i])

    return [cnt, max_time]


TC = int(input())
for _ in range(TC):
    n, d, c = map(int, input().split())  # com, depen, start
    graph = [[] for _ in range(n + 1)]
    for __ in range(d):
        a, b, s = map(int, input().split())  # b -> a, time
        graph[b].append((a, s))

    print(*search(c))


"""
10282. 해킹
    - 그냥 간단한 다익스트라임
"""
