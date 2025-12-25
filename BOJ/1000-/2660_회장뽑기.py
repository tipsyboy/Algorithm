# https://www.acmicpc.net/problem/2660
# bfs / floyd-warshall

import sys
from collections import deque

input = sys.stdin.readline
INF = float("inf")


def sol1():
    def bfs(start: int) -> int:
        q = deque([start])
        vis = [False] * (N + 1)
        vis[start] = True

        rst = 0
        while q:
            for _ in range(len(q)):
                now = q.popleft()

                for friend in graph[now]:
                    if vis[friend]:
                        continue

                    q.append(friend)
                    vis[friend] = True

            rst += 1

        return rst - 1

    N = int(input())
    graph = [[] for _ in range(N + 1)]

    while True:
        u, v = map(int, input().split())
        if u == -1 and v == -1:
            break

        graph[u].append(v)
        graph[v].append(u)

    minv = INF
    ans = []
    for i in range(1, N + 1):
        temp = bfs(i)

        if temp < minv:
            ans = []
            ans.append(i)
            minv = temp
        elif temp == minv:
            ans.append(i)

    print(minv, len(ans))
    print(*ans)


def sol2():
    N = int(input())
    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    while True:
        u, v = map(int, input().split())
        if u == -1 and v == -1:
            break

        graph[u][v] = 1
        graph[v][u] = 1

    for i in range(1, N + 1):
        graph[i][i] = 0

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    score = INF
    ans = []
    for i in range(1, N + 1):
        M = max(graph[i][1:])
        if M < score:
            score = M
            ans = [i]
        elif M == score:
            ans.append(i)
    print(score, len(ans))
    print(*ans)


# sol1()
sol2()


"""
2660. 회장뽑기
    - bfs로 거리 재던지

    - 플로이드 워셜로 해결
"""