# https://www.acmicpc.net/problem/6593

import sys
from collections import deque

input = sys.stdin.readline
directions = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]  # 동서남북상하


def get_target(L: int, R: int, C: int, grid: list) -> list:
    start, end = tuple(), tuple()
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if grid[i][j][k] == "S":
                    start = (i, j, k)
                elif grid[i][j][k] == "E":
                    end = (i, j, k)

    return [start, end]


def bfs(L: int, R: int, C: int, grid: list) -> int:
    start, end = get_target(L, R, C, grid)
    ex, ey, ez = end
    visited = list(list([0] * C for _ in range(R)) for __ in range(L))
    visited[start[0]][start[1]][start[2]] = True
    q = deque([start])

    time = 0
    while q:
        for _ in range(len(q)):
            x, y, z = q.popleft()

            if x == ex and y == ey and z == ez:
                return time

            for i in range(6):
                nx, ny, nz = x + directions[i][0], y + directions[i][1], z + directions[i][2]

                if nx < 0 or nx >= L or ny < 0 or ny >= R or nz < 0 or nz >= C:
                    continue

                if visited[nx][ny][nz] or grid[nx][ny][nz] == "#":
                    continue

                q.append((nx, ny, nz))
                visited[nx][ny][nz] = True

        time += 1

    return -1


while True:
    L, R, C = map(int, input().split())  # 층 / 행 / 열

    if L == 0 and R == 0 and C == 0:
        break

    grid = []
    for i in range(L):
        grid.append([list(input().rstrip()) for _ in range(R)])
        input()  # 빈 줄 입력

    ans = bfs(L, R, C, grid)
    if ans == -1:
        print("Trapped!")
    else:
        print("Escaped in %d minute(s)." % ans)