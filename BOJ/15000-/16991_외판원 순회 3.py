# 2024.10.29 TUE
# https://www.acmicpc.net/problem/16991

import sys

input = sys.stdin.readline
INF = float("inf")


def tsp(cur, visited):
    if visited == (1 << N) - 1:
        return get_distance(graph[cur], graph[0])

    if dp[cur][visited]:
        return dp[cur][visited]

    rst = INF
    for nxt in range(N):
        if cur == nxt:
            continue

        if visited & (1 << nxt):
            continue

        rst = min(rst, tsp(nxt, visited | (1 << nxt)) + get_distance(graph[cur], graph[nxt]))

    dp[cur][visited] = rst
    return rst


def get_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


N = int(input())
graph = []
for _ in range(N):
    x, y = map(int, input().split())
    graph.append((x, y))

dp = [[0] * (1 << N) for _ in range(N)]

ans = tsp(0, 1)
print(f"{ans:.6f}")
