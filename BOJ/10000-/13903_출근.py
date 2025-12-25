# 2024.08.24 SAT
# https://www.acmicpc.net/problem/13903

import sys
from collections import deque

input = sys.stdin.readline
INF = float("inf")


def bfs(R, C):
    q = deque()
    visited = [[INF] * C for _ in range(R)]
    for col in range(C):
        if grid[0][col] == 1:
            q.append((0, col))
            visited[0][col] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if visited[nx][ny] != INF or grid[nx][ny] != 1:
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    return min(visited[R - 1])


R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
N = int(input())
directions = [tuple(map(int, input().split())) for _ in range(N)]

ans = bfs(R, C)
print(ans) if ans != INF else print(-1)
