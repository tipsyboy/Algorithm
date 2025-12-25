# https://www.acmicpc.net/problem/9370

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float("inf")


def dijkstra(graph: list, start: int) -> list:
    dist = [INF] * len(graph)
    dist[start] = 0
    pq = []
    heappush(pq, (0, start))

    while pq:
        now_cost, now_node = heappop(pq)

        if now_cost > dist[now_node]:
            continue

        for adj_node, adj_cost in graph[now_node]:
            cost = now_cost + adj_cost

            if cost < dist[adj_node]:
                dist[adj_node] = cost
                heappush(pq, (cost, adj_node))

    return dist


def sol(ss: list, gs: list, hs: list, candidates: list, s: int, g: int, h: int) -> list:
    rst = []
    for candidate in candidates:
        if ss[candidate] == INF:  # 1) 후..
            continue

        if ss[candidate] == ss[g] + gs[h] + hs[candidate] or ss[candidate] == ss[h] + hs[g] + gs[candidate]:
            rst.append(candidate)

    return sorted(rst)


TC = int(input())
for _ in range(TC):
    n, m, t = map(int, input().split())  # 노드, 간선, 후보지
    s, g, h = map(int, input().split())  # start, 반드시 지나야 하는 g->h 도로

    graph = [[] for _ in range(n + 1)]
    for __ in range(m):
        a, b, d = map(int, input().split())

        graph[a].append((b, d))
        graph[b].append((a, d))

    candidates = []
    for __ in range(t):
        candidates.append(int(input()))

    ss = dijkstra(graph, s)  # start s
    gs = dijkstra(graph, g)  # start g
    hs = dijkstra(graph, h)  # start h
    print(*sol(ss, gs, hs, candidates, s, g, h))


"""
9370. 미확인 도착지
    - 주석 1)의 경우를 생각하지 않아서 개삽질함
      INF를 float("inf")로 설정해놨기 때문에 해당 경로로 도달할 수 없는 경우에 좌우변이 inf로 같은 값을 같게됨
      때문에 답이 아닌 값이 rst로 들어감.

    - 이외는 간단하다
      (g-h) 간선은 문제에 의해 지나가야 하는 경로로 지정되어 있으므로 각각의 start 지점을 다익스트라로 구해준 후 최단거리가 되는지 판단함. 
"""