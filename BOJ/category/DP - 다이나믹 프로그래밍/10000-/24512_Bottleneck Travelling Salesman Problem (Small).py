# 2024.10.29 TUE
# https://www.acmicpc.net/problem/24512

import sys

input = sys.stdin.readline
INF = float("inf")


def tsp(cur, visited):
    if visited == (1 << N) - 1:
        dp[cur][visited] = cost[cur][0]
        return dp[cur][visited]

    if dp[cur][visited] != INF:
        return dp[cur][visited]

    rst = INF
    for adj_node, adj_cost in graph[cur]:
        if visited & (1 << adj_node):
            continue

        rst = min(rst, max(adj_cost, tsp(adj_node, visited | (1 << adj_node))))

    dp[cur][visited] = rst
    return dp[cur][visited]


def get_route(cur, visited, visited_order):
    route[visited_order] = cur
    if visited_order == N:
        return

    for adj_node, adj_cost in graph[cur]:
        if visited & (1 << adj_node):
            continue

        if dp[cur][visited] == max(adj_cost, dp[adj_node][visited | (1 << adj_node)]):
            return get_route(adj_node, visited | (1 << adj_node), visited_order + 1)


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
cost = [[INF] * N for _ in range(N)]

for _ in range(M):
    u, v, c = map(int, input().split())
    graph[u - 1].append((v - 1, c))
    cost[u - 1][v - 1] = c

dp = [[INF] * (1 << N) for _ in range(N)]
route = [INF] * N
ans = tsp(0, 1)
if ans == INF:
    print(-1)
else:
    print(ans)
    get_route(0, 1, 0)
    print(*list(map(lambda x: x + 1, route)))
