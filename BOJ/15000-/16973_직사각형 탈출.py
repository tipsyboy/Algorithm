# https://www.acmicpc.net/problem/16973

"""
16973. 직사각형 탈출
    - 2차원 누적합 + BFS

    - 매번 이동 때마다, 모든 직사각형의 칸이 벽이 있는 칸과 겹치는지 확인하면 TLE를 받게됨

    - 범위 내에 이동이 불가한 위치(벽)을 2차원 누적합으로 계산해 놓은 후 매번 이동에서 
      범위 내부 벽의 개수를 찾아내면 된다. 
"""

import sys
from collections import deque

input = sys.stdin.readline
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def OOB(nx: int, ny: int) -> bool:
    if nx < 0 or nx > N - H or ny < 0 or ny > M - W:
        return True
    return False


def check_WALL(nx: int, ny: int) -> bool:
    sx, sy = nx + 1, ny + 1
    fx, fy = sx + H - 1, sy + W - 1
    return psum[fx][fy] - psum[sx - 1][fy] - psum[fx][sy - 1] + psum[sx - 1][sy - 1]


def bfs(sx: int, sy: int) -> int:
    q = deque([(sx, sy)])
    visited = [[-1] * M for _ in range(N)]
    visited[sx][sy] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]

            if OOB(nx, ny) or check_WALL(nx, ny):
                continue

            if visited[nx][ny] != -1:
                continue

            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    return visited[fr][fc]


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
H, W, sr, sc, fr, fc = map(lambda x: int(x) - 1, input().split())
H, W = H + 1, W + 1

psum = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        psum[i][j] = psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1] + grid[i - 1][j - 1]

print(bfs(sr, sc))