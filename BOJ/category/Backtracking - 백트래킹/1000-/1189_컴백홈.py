# https://www.acmicpc.net/problem/1189

import sys

input = sys.stdin.readline
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def dfs(x: int, y: int, move: int) -> None:
    global ans

    if visited[x][y] or move > K:
        return

    if x == 0 and y == C - 1:
        if move == K - 1:
            ans += 1
        return

    visited[x][y] = True
    for i in range(4):
        nx, ny = x + directions[i][0], y + directions[i][1]

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue

        if visited[nx][ny] or grid[nx][ny] == "T":
            continue

        dfs(nx, ny, move + 1)
    visited[x][y] = False


R, C, K = map(int, input().split())
grid = list(list(input().rstrip()) for _ in range(R))
visited = [[False] * C for _ in range(R)]
ans = 0
dfs(R - 1, 0, 0)
print(ans)
