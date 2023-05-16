# https://www.acmicpc.net/problem/14940

import sys
from collections import deque

input = sys.stdin.readline
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(start: tuple) -> list:
    q = deque([start])
    visited = [[0] * m for _ in range(n)]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] or grid[nx][ny] != 1:
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    return exc(visited)


def exc(visited: list) -> list:
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and grid[i][j] == 1:
                visited[i][j] = -1

    return visited


def get_start(grid: list) -> tuple:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                return (i, j)


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = bfs(get_start(grid))
for i in range(n):
    print(" ".join(map(str, ans[i])))
