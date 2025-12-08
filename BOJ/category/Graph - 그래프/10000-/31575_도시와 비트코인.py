# Dec 01, Mon 2025
# https://www.acmicpc.net/problem/31575

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

visited = [[False] * N for _ in range(M)]
visited[0][0] = True
for x in range(M):
    for y in range(N):
        if not visited[x][y]:
            continue

        for dx, dy in [(0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy

            if nx >= M or ny >= N:
                continue
            if grid[nx][ny] == 0:
                continue

            visited[nx][ny] = True

print("Yes") if visited[M - 1][N - 1] else print("No")
