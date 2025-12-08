# Nov 30, Sun 2025
# https://www.acmicpc.net/problem/17141

import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
INF = float("inf")
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_all_visited(visited):
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 1 and visited[i][j] == -1:
                return False
    return True


def bfs(virus):
    q = deque(virus)
    visited = [[-1] * N for _ in range(N)]
    for x, y in virus:
        visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] != -1 or grid[nx][ny] == 1:
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    if not is_all_visited(visited):
        return INF

    mx = -1
    for i in range(N):
        for j in range(N):
            if mx < visited[i][j]:
                mx = visited[i][j]
    return mx


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

virus_cand = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            virus_cand.append((i, j))

ans = INF
for virus in combinations(virus_cand, M):
    ans = min(ans, bfs(virus))
print(ans) if ans != INF else print(-1)
