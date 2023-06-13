# https://www.acmicpc.net/problem/1219

"""
1219. 오민식의 고민
    - bellman-ford + BFS
    
    - https://www.acmicpc.net/board/view/43130 를 보고 잘못된 점을 찾았다..
"""

import sys
from collections import deque

input = sys.stdin.readline
INF = float("inf")


def can_go(start: int, end: int) -> bool:
    q = deque([start])
    visited = [False] * N
    visited[start] = True

    while q:
        now = q.popleft()

        if now == end:
            return True

        for adj_node, _ in graph[now]:
            if visited[adj_node]:
                continue

            q.append(adj_node)
            visited[adj_node] = True

    return False


def BF(start: int, end: int) -> int:
    money = [-INF] * N
    money[start] = get_pay[start]
    cycle, c_node = False, []

    for i in range(N):
        for now_node in range(N):
            if money[now_node] == -INF:
                continue

            for adj_node, adj_cost in graph[now_node]:
                cost = money[now_node] - adj_cost + get_pay[adj_node]  # 현재 소지금 - 가는 비용 + 가면 버는 돈
                if cost > money[adj_node]:
                    money[adj_node] = cost

                    if i == N - 1:
                        cycle = True
                        c_node.append(now_node)

    # print(c_node)
    if cycle:
        for c in c_node:  # 다른 종류의 사이클이 존재 할 수 있으니 판단해줘야함.
            if can_go(c, end):
                return INF

    return money[E]


N, S, E, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
get_pay = list(map(int, input().split()))

if not can_go(S, E):
    print("gg")
else:
    ans = BF(S, E)
    if ans == INF:
        print("Gee")
    else:
        print(ans)
"""
4 0 3 4
0 1 0
1 2 0
2 1 0
0 3 10
10 10 10 10

4 1 3 4
0 1 0
1 2 0
2 1 0
0 3 10
10 10 10 10

3 0 2 4
0 1 9999
1 2 9999
1 1 9999
0 2 0
10000 10000 10000
"""