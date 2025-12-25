# https://www.acmicpc.net/problem/1388

import sys

input = sys.stdin.readline


def judge(x: int, y: int, shape: str) -> None:
    visited[x][y] = True

    if shape == "-":
        for i in range(y + 1, M):
            if grid[x][i] != "-":
                break
            visited[x][i] = True
    else:
        for i in range(x + 1, N):
            if grid[i][y] != "|":
                break
            visited[i][y] = True


N, M = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            judge(i, j, grid[i][j])
            ans += 1

print(ans)