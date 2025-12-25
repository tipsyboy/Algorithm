# Nov 29, Sat 2025
# https://www.acmicpc.net/problem/1245

import sys
from collections import deque

input = sys.stdin.readline
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True

    peak = 1
    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:  # A.
                continue

            if grid[x][y] < grid[nx][ny]:  # 1. 인접 봉우리보다 낮으면 봉우리가 아님
                peak = 0

            if visited[nx][ny]:  # 2. 위 조건(1)보다 방문 조건을 먼저 하는 경우(A 조건) 봉우리 조건을 제대로 판단 X
                continue

            if grid[x][y] == grid[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

    return peak


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        ans += bfs(i, j)
print(ans)

"""
1245. 농장 관리

1. 같은 높이의 위치는 함께 봉우리가 될 수 있다. -> 문제를 잘 읽고 조건을 파악 해야함. 
2. 조건 순서에 따라서 답이 달라질 수 있다. -> 방문 조건은 nxt에는 포함되지 않으나 봉우리를 체크할 땐 상관 없으므로 봉우리 조건은 꼭 체크 해야한다. 
"""
