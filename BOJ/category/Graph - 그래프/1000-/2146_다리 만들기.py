# https://www.acmicpc.net/problem/2146

import sys
from collections import deque

input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
INF = float("inf")


def div_island(N: int, grid: list) -> int:
    visited = [[False] * N for _ in range(N)]

    label = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] or grid[i][j] == 0:
                continue

            label += 1
            q = deque([(i, j)])
            grid[i][j] = label
            visited[i][j] = True

            while q:
                x, y = q.popleft()

                for d in range(4):
                    nx, ny = x + directions[d][0], y + directions[d][1]

                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue
                    if visited[nx][ny] or grid[nx][ny] == 0:
                        continue

                    grid[nx][ny] = label
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return label


def is_edge(x: int, y: int) -> bool:
    for i in range(4):
        nx, ny = x + directions[i][0], y + directions[i][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if grid[nx][ny] == 0:
            return True

    return False


def shortest_bridge(label: int) -> list:
    def bfs(sx: int, sy: int, now: int) -> int:
        q = deque([(sx, sy, 0)])
        visited = [[False] * N for _ in range(N)]

        while q:
            x, y, c = q.popleft()

            for i in range(4):
                nx, ny = x + directions[i][0], y + directions[i][1]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue

                if visited[nx][ny] or grid[nx][ny] == now:
                    continue

                if grid[nx][ny] != now and grid[nx][ny] != 0:
                    return c

                q.append((nx, ny, c + 1))
                visited[nx][ny] = True

        return INF

    dist = [INF] * label
    for i in range(N):
        for j in range(N):
            if not is_edge(i, j) or grid[i][j] == 0:
                continue

            now = grid[i][j]
            dist[now - 1] = min(dist[now - 1], bfs(i, j, now))

    return dist


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
label = div_island(N, grid)
print(min(shortest_bridge(label)))