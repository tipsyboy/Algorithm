import sys
from collections import deque

input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(sx: int, sy: int) -> int:
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    s, w = 0, 0

    while q:
        x, y = q.popleft()

        if grid[x][y] == "v":
            w += 1
        elif grid[x][y] == "o":
            s += 1

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if grid[nx][ny] == "#" or visited[nx][ny]:
                continue

            q.append((nx, ny))
            visited[nx][ny] = True

    if s > w:
        return s

    return -w


R, C = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
sheep, wolves = 0, 0

for i in range(R):
    for j in range(C):
        if grid[i][j] == "#" or visited[i][j]:
            continue

        val = bfs(i, j)
        if val < 0:
            wolves += abs(val)
        else:
            sheep += val

print(sheep, wolves)
