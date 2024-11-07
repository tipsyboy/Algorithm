# 2024.10.31 THU
# https://www.acmicpc.net/problem/18430

import sys

input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_valid(x, y):
    return 0 <= x < N and 0 <= y < M and not visited[x][y]


def cal_power(center, o1, o2):
    x, y = center
    ox1, oy1 = o1
    ox2, oy2 = o2
    return grid[x][y] * 2 + grid[ox1][oy1] + grid[ox2][oy2]


def bt(cur, power):
    global ans

    if cur == N * M:
        ans = max(ans, power)
        return

    x, y = cur // M, cur % M

    if not is_valid(x, y):
        return

    for d1, d2 in [(0, 2), (1, 2), (0, 3), (1, 3)]:
        nx1, ny1 = x + directions[d1][0], y + directions[d1][1]
        nx2, ny2 = x + directions[d2][0], y + directions[d2][1]

        if is_valid(x, y) and is_valid(nx1, ny1) and is_valid(nx2, ny2):
            visited[x][y] = True
            visited[nx1][ny1] = True
            visited[nx2][ny2] = True
            for nxt in range(cur + 1, N * M + 1):
                bt(nxt, power + cal_power((x, y), (nx1, ny1), (nx2, ny2)))
            visited[x][y] = False
            visited[nx1][ny1] = False
            visited[nx2][ny2] = False


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

ans = 0
for start in range(N * M):
    bt(start, 0)
print(ans)
