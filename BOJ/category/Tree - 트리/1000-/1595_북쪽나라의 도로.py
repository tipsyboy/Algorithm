# 2024.10.10 THU
# https://www.acmicpc.net/problem/1595

"""
1595. 북쪽나라의 도로
  - dfs/bfs or 다익스트라
  - 트리의 지름
"""

import sys

input = sys.stdin.readline
INF = float("inf")
MAXV = 10_000


def dfs(cur, cost):
    visited[cur] = True

    rst = (cur, cost)
    for c, nxt in graph[cur]:
        if visited[nxt]:
            continue

        temp = dfs(nxt, cost + c)
        if temp[1] > rst[1]:
            rst = temp

    return rst


graph = [[] for _ in range(MAXV + 1)]
node_set = set()
while True:
    x = input().rstrip()

    if x == "":
        break

    u, v, d = map(int, x.split())
    node_set.add(u)
    node_set.add(v)

    graph[u].append((d, v))
    graph[v].append((d, u))


visited = [False] * (MAXV + 1)
x, _ = dfs(1, 0)
visited = [False] * (MAXV + 1)
y, ans = dfs(x, 0)

print(ans)
