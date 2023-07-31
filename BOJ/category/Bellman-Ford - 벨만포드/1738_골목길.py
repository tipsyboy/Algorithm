# https://www.acmicpc.net/problem/1738
"""
1739. 골목길
    - 벨만-포드
"""
import sys
from collections import deque

input = sys.stdin.readline
INF = float("inf")


def can_go(start: int, end: int) -> bool:
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        cur = q.popleft()

        if cur == end:
            return True

        for adj_node, _ in graph[cur]:
            if visited[adj_node]:
                continue

            q.append(adj_node)
            visited[adj_node] = True

    return False


def get_route(prev: list) -> list:
    route = [n]

    cur = n
    while prev[cur]:
        route.append(prev[cur])
        cur = prev[cur]

    return route


def BF(start: int) -> list:
    if not can_go(start, n):
        return [-1]

    money = [-INF] * (n + 1)
    money[start] = 0
    prev = [0] * (n + 1)
    cycle = set()

    for i in range(n):
        for cur_node in range(1, n + 1):
            for adj_node, adj_cost in graph[cur_node]:
                cost = money[cur_node] + adj_cost

                if cost > money[adj_node]:
                    money[adj_node] = cost
                    prev[adj_node] = cur_node

                    if i == n - 1:
                        cycle.add(cur_node)

    if cycle:
        for c in cycle:
            if can_go(c, n):
                return [-1]

    return get_route(prev)[::-1]


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))

print(*BF(1))


"""
4 4
1 4 3
2 3 1
3 2 1
4 2 1
"""