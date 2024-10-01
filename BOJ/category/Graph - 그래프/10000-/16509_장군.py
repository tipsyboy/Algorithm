# 2024.09.27 FRI
# https://www.acmicpc.net/problem/16509

import sys
from collections import deque

input = sys.stdin.readline
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
move = [(0, 7, 7), (0, 1, 1), (2, 1, 1), (2, 3, 3), (4, 3, 3), (4, 5, 5), (6, 5, 5), (6, 7, 7)]


def bfs(sx, sy, fx, fy):
    q = deque([(sx, sy)])
    visited = [[0] * 9 for _ in range(10)]

    while q:
        x, y = q.popleft()

        if x == fx and y == fy:
            break

        for m in move:
            able = True
            nx, ny = x, y
            for i in range(3):
                nx, ny = nx + directions[m[i]][0], ny + directions[m[i]][1]

                if nx < 0 or nx >= 10 or ny < 0 or ny >= 9 or (i < 2 and nx == fx and ny == fy):
                    able = False
                    break

            if not able or visited[nx][ny]:
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    return visited[fx][fy] if visited[fx][fy] else -1


R1, C1 = map(int, input().split())  # 상
R2, C2 = map(int, input().split())  # 궁

print(bfs(R1, C1, R2, C2))
