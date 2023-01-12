# https://www.acmicpc.net/problem/1600

import sys
from collections import deque

input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
directions_horse = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]


def OOB(nx: int, ny: int) -> bool:
    return nx < 0 or nx >= H or ny < 0 or ny >= W


def bfs() -> int:
    q = deque([(0, 0, 0)])
    visited = [[[0 for _ in range(K + 1)] for __ in range(W)] for ___ in range(H)]

    while q:
        x, y, horse = q.popleft()

        if x == H - 1 and y == W - 1:
            return visited[x][y][horse]

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if OOB(nx, ny) or visited[nx][ny][horse]:
                continue

            if grid[nx][ny] == 1:
                continue

            q.append((nx, ny, horse))
            visited[nx][ny][horse] = visited[x][y][horse] + 1

        # 말 짬푸 기회 x
        if horse >= K:
            continue

        for i in range(8):
            nx, ny = x + directions_horse[i][0], y + directions_horse[i][1]

            if OOB(nx, ny) or visited[nx][ny][horse + 1]:
                continue

            if grid[nx][ny] == 1:
                continue

            q.append((nx, ny, horse + 1))
            visited[nx][ny][horse + 1] = visited[x][y][horse] + 1

    return -1


K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

print(bfs())
