import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, n, graph):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = []
    heappush(pq, (0, start))

    while pq:
        now_cost, now_node = heappop(pq)

        if now_cost > dist[now_node]:
            continue

        for adj in graph[now_node]:
            if now_cost + 1 < dist[adj]:
                dist[adj] = now_cost + 1
                heappush(pq, (now_cost + 1, adj))

    return dist


def solution_dijkstra():
    n, m = map(int, input().split())  # node, edge
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())

        # undirected graph
        graph[a].append(b)
        graph[b].append(a)

    x, k = map(int, input().split())  # 도착지, 경유지

    answer = 0

    # 1 -> k
    dist = dijkstra(1, n, graph)
    answer += dist[k]

    # k -> x
    dist = dijkstra(k, n, graph)
    answer += dist[x]

    if answer >= INF:
        return -1

    return answer


def floyd_warshall():
    n, m = map(int, input().split())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        graph[i][i] = 0

    for _ in range(m):
        a, b = map(int, input().split())

        # undirected graph, cost == 1
        graph[a][b] = 1
        graph[b][a] = 1

    x, k = map(int, input().split())  # 도착지 경유지

    for w in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][w] + graph[w][j]:
                    graph[i][j] = graph[i][w] + graph[w][j]

    if graph[1][k] + graph[k][x] >= INF:
        return -1

    return graph[1][k] + graph[k][x]


print(solution_dijkstra())

# print(floyd_warshall())