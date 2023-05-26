# https://www.acmicpc.net/problem/17086

import sys
from collections import deque

input = sys.stdin.readline
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def bfs(start: list) -> int:
    q = deque(start)
    visited = [[0] * M for _ in range(N)]

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] or grid[nx][ny] == 1:
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    # maxv = -1
    # for i in range(N):
    #     for j in range(M):
    #         maxv = max(maxv, visited[i][j])

    return max(map(max, visited))


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

start = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            start.append((i, j))

print(bfs(start))