# https://www.acmicpc.net/problem/17835

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float("inf")


def dijkstra(start: list) -> list:
    pq = []
    dist = [INF] * (N + 1)
    for s in start:
        heappush(pq, (0, s))
        dist[s] = 0

    while pq:
        now_dist, now_node = heappop(pq)

        if now_dist > dist[now_node]:
            continue

        for adj_node, adj_dist in graph[now_node]:
            cost = now_dist + adj_dist

            if cost < dist[adj_node]:
                dist[adj_node] = cost
                heappush(pq, (cost, adj_node))

    return dist


N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    graph[v].append((u, c))
interview = list(map(int, input().split()))

dist = dijkstra(interview)

target, ans = -1, -1
for i in range(1, N + 1):
    if ans < dist[i]:
        ans = dist[i]
        target = i

print(target)
print(ans)

"""
17835. 면접보는 승범이네
    - 다익스트라 알고리즘의 시간 복잡도는 ElogV 모든 노드에서 다익스트라 알고리즘을 수행하면 VElogV가 되고, TLE가 되는 것이 당연하다.
    
    - 때문에 그래프를 역방향으로 받아서 '면접장->각각 도시'로의 다익스트라 알고리즘을 돌리려 했으나, K의 범위가 K<=N 인것을 보고 잠깐 생각이 멈춤.
    - 이후 모든 면접장이 담긴 'interview'를 전부 pq에 넣고 해결함. 
      면접장과 도시가 같은 경우 가중치 0으로 논리적으로 문제가 없기 때문
"""