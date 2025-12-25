# https://www.acmicpc.net/problem/2665

import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float("inf")
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dijkstra(sx: int, sy: int) -> int:
    pq = []
    visited = [[INF] * n for _ in range(n)]
    heappush(pq, (0, sx, sy))
    visited[sx][sy] = 0

    while pq:
        now_cost, x, y = heappop(pq)
        if now_cost > visited[x][y]:
            continue

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            cost = now_cost if graph[nx][ny] == 1 else now_cost + 1
            if cost < visited[nx][ny]:
                visited[nx][ny] = cost
                heappush(pq, (cost, nx, ny))

    return visited[n - 1][n - 1]


n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
print(dijkstra(0, 0))